from car_fueling import compute_min_refills, compute_min_refills_v2


def test_compute_min_refills():
    distance = 950
    tank = 400
    stops = [200, 375, 550, 750]
    assert compute_min_refills(distance, tank, stops) == 2

    distance = 10
    tank = 3
    stops = [1, 2, 5, 9]
    assert compute_min_refills(distance, tank, stops) == -1

    distance = 200
    tank = 250
    stops = [100, 150]
    assert compute_min_refills(distance, tank, stops) == 0


def test_compute_min_refills_v2():
    distance = 950
    tank = 400
    stops = [200, 375, 550, 750]
    assert compute_min_refills_v2(distance, tank, stops) == 2

    distance = 10
    tank = 3
    stops = [1, 2, 5, 9]
    assert compute_min_refills_v2(distance, tank, stops) == -1

    distance = 200
    tank = 250
    stops = [100, 150]
    assert compute_min_refills_v2(distance, tank, stops) == 0
