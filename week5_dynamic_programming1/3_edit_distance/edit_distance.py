# Uses python3
def edit_distance(s, t):
    """
    Measures the edit distance between the given two string s and t.

    The allowed operations are: delete a letter, insert a letter and substitute
    a letter. The edit distance is the minimum number of operations (there
    could be multiple ways for the minimum operations) it takes to
    transform a string from one to another.

    Args:
        s (str): of length at least one.

        t (str): of length at least one.

    Returns:
        int, the minimum number of operations.

    """
    n_s = len(s)
    n_t = len(t)

    # n[i][j] is the minimum operation for s[:i+1] and  t[:j+1]
    # the size is (ns + 1) * (n_t + 1) taking into account the
    # empty string.
    D = [[-1] * (n_t + 1) for _ in range(n_s + 1)]

    for i in range(n_s+1):
        D[i][0] = i

    for j in range(n_t+1):
        D[0][j] = j

    for i in range(1, n_s+1):
        for j in range(1, n_t+1):
            if s[i-1] == t[j-1]:
                # match, does not need operation.
                c1 = D[i-1][j-1]
            else:
                # mismatch, need substitute operation.
                c1 = D[i-1][j-1] + 1

            c2 = D[i-1][j] + 1  # insertion
            c3 = D[i][j-1] + 1  # deletion
            D[i][j] = min((c1, c2, c3))

    return D[n_s][n_t]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
