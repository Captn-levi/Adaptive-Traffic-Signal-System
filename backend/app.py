from flask import Flask, request, jsonify, render_template
import os
from ultralytics import YOLO
from junction.road_detector import get_incoming_roads

app = Flask(__name__)

# ------------------------
# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ------------------------
# Load YOLO model (AUTO DOWNLOAD)
print("Loading YOLOv8 model...")
model = YOLO("yolov8n.pt")
print("YOLO model loaded successfully.")

# ------------------------
# Routes

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/junction", methods=["POST"])
def junction_info():
    data = request.json

    lat = float(data["lat"])
    lon = float(data["lon"])

    roads = get_incoming_roads(lat, lon)

    return jsonify({
        "road_count": len(roads),
        "roads": roads
    })


@app.route("/upload_images", methods=["POST"])
def upload_images():
    if not request.files:
        return jsonify({"error": "No files received"}), 400

    results = {}

    for road_name, file in request.files.items():
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        detections = model(filepath)

        vehicle_count = 0
        for r in detections:
            if r.boxes is not None:
                for cls in r.boxes.cls:
                    if int(cls) in [2, 5, 7]:  # car, bus, truck
                        vehicle_count += 1

        results[road_name] = {"vehicle_count": vehicle_count}

    # ------------------------
    # Adaptive signal timing
    total_vehicles = sum(v["vehicle_count"] for v in results.values())

    signal_times = {}
    for road, v in results.items():
        if total_vehicles > 0:
            signal_times[road] = max(10, int((v["vehicle_count"] / total_vehicles) * 120))
        else:
            signal_times[road] = 30

    # Use "results" key to match JS
    return jsonify({
        "results": results,
        "signal_times": signal_times
    })


if __name__ == "__main__":
    app.run(debug=True)
