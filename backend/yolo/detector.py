from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_vehicles(image_path):
    results = model(image_path)
    counts = {"car":0, "bus":0, "truck":0, "motorcycle":0}

    for r in results:
        for c in r.boxes.cls:
            cls = model.names[int(c)]
            if cls in counts:
                counts[cls] += 1

    return counts
