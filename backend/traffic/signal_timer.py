def calculate_signal_times(densities, total_cycle=120):
    total_density = sum(densities.values())
    signal_times = {}

    for road, density in densities.items():
        signal_times[road] = round(
            (density / total_density) * total_cycle, 2
        )

    return signal_times
