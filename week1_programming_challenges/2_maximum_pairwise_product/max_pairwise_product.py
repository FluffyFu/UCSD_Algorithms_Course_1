# python3


def max_pairwise_product(numbers):
    if numbers[0] > numbers[1]:
        x1 = numbers[0]
        x2 = numbers[1]
    else:
        x1 = numbers[1]
        x2 = numbers[0]
    for x in numbers[2:]:
        if x <= x2:
            continue
        elif x > x1:
            x2 = x1
            x1 = x
        else:
            x2 = x

    return x1 * x2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
