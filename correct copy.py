def get_distance(lat_a, lat_b, long_a, long_b) -> float:
    """
    Calculate the distance between 2 cities
    """
    lat_a, lat_b, long_a, long_b = map(radians, [lat_a, lat_b, long_a, long_b])
    return 6370 * acos(sin(lat_a) * sin(lat_b) + cos(lat_a) * cos(lat_b) * cos(long_a - long_b))