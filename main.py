def pillars(num_pill: int, dist: int, width: int) -> int:
    """
    Given a number of pillars, determine the distance in cm between the first and last pillar
    :param num_pill: number of pillars
    :param dist: distance between pillars (in meters)
    :param width: width of one pillar (in cm)
    :return: distance in cm between first and last pillar
    """
    if num_pill == 1:
        return 0
    elif num_pill == 2:
        return dist * 100
    else:
        dist_cm = dist * 100
        total_dist = dist_cm * (num_pill-1)
        return total_dist + (width * (num_pill-2))
