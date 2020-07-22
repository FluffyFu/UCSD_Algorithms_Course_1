# Uses python3
import sys


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if left >= right:
        return number_of_inversions
    ave = left + (right - left) // 2

    # count number of inversions in the sub-arrays
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave+1, right)

    # add the number of inversions by the combination of the two sub-arrays.
    number_of_inversions += merge_and_count(a, b, left, ave, ave+1, right)
    return number_of_inversions


def merge_and_count(a, b, l1, r1, l2, r2):
    """
    Merge the two sorted sub-arrays and count the number of inversions.

    Args:
        a (list): partially sorted array, [l1, r1] and [l2, r2] are the range of the
        two sub-arrays.

        b (list): auxiliary array for merge sort.

        l1 (int)

        r1 (int)

        l2 (int)

        r2 (int)

    Returns:
        int, number of inversions.
    """
    for i in range(l1, r1+1):
        b[i] = a[i]

    for i in range(l2, r2+1):
        b[i] = a[i]

    p1 = l1  # pointer for the first sub-array
    p2 = l2  # pointer for the second sub-arry
    index = l1  # pointer for the original array.
    n_inversions = 0

    while(p1 <= r1 and p2 <= r2):
        if b[p1] <= b[p2]:
            a[index] = b[p1]
            p1 += 1
        else:
            # b[p1] > b[p2], each element in the rest of the first sub-array
            # all contribute to one inversion.
            a[index] = b[p2]
            n_inversions += (r1 - p1 + 1)
            p2 += 1
        index += 1

    # append the rest of the array
    for i in range(p1, r1+1):
        a[index] = b[i]
        index += 1

    for i in range(p2, r2+1):
        a[index] = b[i]
        index += 1

    return n_inversions


def get_number_of_inversions_naive(a):
    """
    Use insertion sort to calculate the number of inversions. O(n**2)

    Args:
        a (list of int): the array upon which the number of inversions needs
        to be calculated.

    Returns:
        int, number of inversions.
    """
    n = len(a)
    n_inversions = 0

    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]
                n_inversions += 1
            else:
                break

    return n_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))
