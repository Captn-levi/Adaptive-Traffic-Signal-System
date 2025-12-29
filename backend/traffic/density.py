def calculate_density(vehicle_counts):
    return (
        vehicle_counts["car"] * 1 +
        vehicle_counts["motorcycle"] * 0.5 +
        vehicle_counts["bus"] * 2 +
        vehicle_counts["truck"] * 2.5
    )
