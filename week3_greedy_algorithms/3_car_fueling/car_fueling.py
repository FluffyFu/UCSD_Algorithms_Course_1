# python3
import sys


def compute_min_refills(distance, tank, stops):
    """
    Given the distance between the origin and destination and a list of gas stations. Find the
    minimum number of times to fill the tank. If it is impossible, return -1.

    Args:
        distance (float): the distance between origin and destination.

        tank (float): the distance can be traveled with a full tank.

        stops (list): the distance between the gas station and the origin. Sorted from close to far.

    Returns:
        int, the minimum number of fuel times if it's possible. Otherwise, returns -1.
    """
    # adding origin and destination simplifies the checking.
    # this is important.
    stops.insert(0, 0)  # add origin.
    stops.append(distance)  # add destination
    num_fuels = 0
    previous_stop = 0  # index of the previous filling gas station.
    current_stop = 1  # index to loop through the gas stations.

    while current_stop < len(stops):
        if stops[current_stop] - stops[previous_stop] > tank:
            # impossible config
            return -1

        while current_stop < len(stops) and (stops[current_stop] - stops[previous_stop] <= tank):
            current_stop += 1

        # there are two possibilities when the flow reaches here:
            # 1. current_stop == len(stops), this means destination has been reached in the previous step (current_stop - 1)
            #       and no extra fuel is needed.
            # 2. current_stop cannot be reached from previous_stop without fueling, we add one more fueling.
        if current_stop < len(stops):
            previous_stop = current_stop - 1
            num_fuels += 1

    return num_fuels


def compute_min_refills_v2(distance, tank, stops):
    """
    Cleaner version of compute_min_refills.
    """
    stops.insert(0, 0)
    stops.append(distance)
    current_stop = 1
    num_fuels = 0

    while current_stop < len(stops):
        previous_stop = current_stop - 1

        while (current_stop < len(stops)) and (stops[current_stop] - stops[previous_stop] <= tank):
            current_stop += 1

        if previous_stop == current_stop - 1:
            return -1
        if current_stop < len(stops):
            num_fuels += 1
    return num_fuels


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
