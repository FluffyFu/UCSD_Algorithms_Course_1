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
    num_fuels = 0
    previous_pos = 0  # the actual station that fill the tank.
    current_stop = 0  # index to loop through the gas stations.

    while current_stop < len(stops):
        if stops[current_stop] - previous_pos > tank:
            # impossible config
            return -1

        while current_stop < len(stops) and (stops[current_stop] - previous_pos <= tank):
            current_stop += 1

        if current_stop == len(stops):
            # the stops has been exhausted.
            if distance - previous_pos <= tank:
                # travel directly from previous_pos to distance
                return num_fuels
            elif distance - stops[-1] > tank:
                # impossible to reach the destination
                return -1
            else:
                # need one more fuel to reach the destination
                return num_fuels + 1

        else:
            # update the previous_pos
            previous_pos = stops[current_stop - 1]
            num_fuels += 1

    return num_fuels


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
