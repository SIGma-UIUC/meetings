from itertools import product

# I hate globals but I am lazy
total = 0

# This code uses dummy values in lists for 1 indexing
# This better reflects how the cover problem is formulated in the slides

def is_langford(n, L):
    seen = set()
    for j in range(1, n + 1):
        i = L[j]
        k = j + i + 1
        if k <= 2 * n and i not in seen:
            if L[j] != L[k]:
                print(f"L[{j}] is {L[j]} and L[{k}] is {L[k]}")
                return False
        seen.add(i)
    return True


def langford_print(n, Cover):
    L = [None for _ in range(2 * n + 1)]
    for i, j, k in Cover:
        L[j] = i
        L[k] = i

    assert is_langford(n, L)
    global total
    total += 1
    print(L[1:])


def is_cover(n, Cover):
    L = [None for _ in range(2 * n + 1)]
    for i, j, k in Cover:
        L[j] = i
        L[k] = i

    # Every slot must be filled
    if any(slot == None for slot in L[1:]):
        return False
    else:
        return True


def generate_options(n):
    # Options take the form [i, j, k]
    #   i = number
    #   j, k = positions in L

    # Generate every option
    # Options = {
    #     (i, j, j + i + 1)
    #     for i in range(1, n + 1)
    #     for j in range(1, 2 * n + 1)
    #     if i + j + 1 <= 2 * n
    # }

    # Method One to omit reversals
    #   Omits n // 2 options
    #   Knuth claims this is faster than Method Two for Algorithm X
    # Options = {
    #     (i, j, j + i + 1)
    #     for i in range(1, n + 1)
    #     for j in range(1, 2 * n + 1)
    #     if (i + j + 1 <= 2 * n and not (i == n - int(n % 2 == 0) and j > n / 2))
    # }

    # Method Two to omit reversals
    #   Omits n - 1 options
    Options = {
        (i, j, j + i + 1)
        for i in range(1, n + 1)
        for j in range(1, 2 * n + 1)
        if (i + j + 1 <= 2 * n and not (i == 1 and j >= n))
    }

    print(f"{len(Options) = }")
    return Options


def __find_pairings(n, Options, Cover, i):
    # if Cover is a cover
    if is_cover(n, Cover):
        langford_print(n, Cover)
        return  # and print

    # if no option in Options contains i
    if any(x == i for x, y, z in Options) is False:
        return  # without printing

    I = {(x, y, z) for x, y, z in Options if x == i}
    Options_ = Options - I
    for O in I:
        # For now, cover sequentially since we know what problem we are solving
        j = i + 1
        __find_pairings(n, Options_, Cover | {O}, j)


def find_pairings(n):
    Options = generate_options(n)
    __find_pairings(n, Options, set(), 1)

def count_pairings(n):
    # See The Art of Computer Programming, Volume 4A: Combinatorial Algorithms Part 1, Exercise 6 Solution
    # or https://dialectrix.com/langford/godfrey/method.html for an explaination,
    # or the written solutions on the SIGma website

    def f(x): #[x_1, x_2, ..., x_2n] as a list or tuple or whatever, *1 indexed*
        n = (len(x) - 1) // 2
        res = 1
        for k in range(1, n + 1):
            s = sum(x[j] * x[j + k + 1] for j in range(1, 2*n - k))
            res *= x[k] * x[n + k] * s
        return res

    res = 0
    for x in product({-1, 1}, repeat=2*n):
        x_vals = list(x)
        x_vals = [None] + x_vals
        res += f(x_vals)

    print(res // (2**(2*n + 1)))

def generate_single_pairing(n):
    if n == 0:
        print("[]")
        return

    m, r = divmod(n, 4)
    if r == 1 or r == 2:
        print("No Pairing Possible")
    else:
        L = [None]
        if r == 0:
            for i in reversed(range(2*m, 4*m - 4 + 1, 2)):
                L.append(i)
            L.append(4*m - 2)
            for i in reversed(range(1, 2*m - 3 + 1, 2)):
                L.append(i)
            L.append(4*m - 1)
            for i in range(1, 2*m - 3 + 1, 2):
                L.append(i)
            for i in range(2*m, 4*m - 4 + 1, 2):
                L.append(i)
            L.append(4*m)
            for i in reversed(range(2*m + 1, 4*m - 3 + 1, 2)):
                L.append(i)
            L.append(4*m - 2)
            for i in reversed(range(2, 2*m - 2 + 1, 2)):
                L.append(i)
            L.append(2*m - 1)
            L.append(4*m - 1)
            for i in range(2, 2*m - 2 + 1, 2):
                L.append(i)
            for i in range(2*m  + 1, 4*m - 3 + 1, 2):
                L.append(i)
            L.append(2*m - 1)
            L.append(4*m)
        if r == 3:
            # really we want r == -1
            m += 1

            for i in reversed(range(2*m, 4*m - 4 + 1, 2)):
                L.append(i)
            L.append(4*m - 2)
            for i in reversed(range(1, 2*m - 3 + 1, 2)):
                L.append(i)
            L.append(4*m - 1)
            for i in range(1, 2*m - 3 + 1, 2):
                L.append(i)
            for i in range(2*m, 4*m - 4 + 1, 2):
                L.append(i)
            L.append(2*m - 1)
            for i in reversed(range(2*m + 1, 4*m - 3 + 1, 2)):
                L.append(i)
            L.append(4*m - 2)
            for i in reversed(range(2, 2*m - 2 + 1, 2)):
                L.append(i)
            L.append(2*m - 1)
            L.append(4*m - 1)
            for i in range(2, 2*m - 2 + 1, 2):
                L.append(i)
            for i in range(2*m  + 1, 4*m - 3 + 1, 2):
                L.append(i)

        assert is_langford(n, L)
        print(L[1:])

def main():
    count_pairings(7)

    # for i in range(21):
    #     print(f"{i}: ",end=" ")
    #     generate_single_pairing(i)
    #     print()

    # print("Finding Pairings...")
    # find_pairings(4)

    # global total
    # print(f"Total Number of Pairings = {total}")


if __name__ == "__main__":
    main()
