function selectJunction() {
    fetch("http://127.0.0.1:5000/junction", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            lat: 9.0054,
            lon: 38.7636
        })
    })
    .then(res => res.json())
    .then(data => {
        let html = `<h3>This junction has ${data.road_count} incoming roads</h3>`;
        html += `<p>Please upload one image for each road:</p><ul>`;

        data.roads.forEach(road => {
            html += `<li>${road}</li>`;
        });

        html += `</ul>`;
        document.getElementById("output").innerHTML = html;
    });
}
