import string
import random

# Initialize Fibonacci Values
MAXIMUM = 0x10FFFF  # maximum unicode value
FIB = [0, 1]
while FIB[-1] <= MAXIMUM:
    FIB.append(FIB[-2] + FIB[-1])


def random_strings(length, count):
    # Generate random printable strings of some max length
    for _ in range(count):
        yield "".join(random.choices(string.whitespace, k=random.randint(0, length)))


def zeckendorf(x):
    # Generate the Zeckendorf decomposition of n as a binary string
    i = max(i for i in range(len(FIB)) if FIB[i] <= x)
    rep = ""
    rem = x

    while i >= 2:
        if FIB[i] <= rem:
            rep += "1"
            rem -= FIB[i]
            if rem > 0:
                rep += "0"
                i -= 1
        else:
            rep += "0"
        i -= 1

    return rep[::-1]


def frodnekcez(rep):
    # Recover the Zeckendorf decomposition
    x = 0
    for i, c in enumerate(rep, 2):
        if c == "1":
            x += FIB[i]

    return x


def zeck_rep(x):
    # Print the summation of Fibonacci Numbers that sum up to n
    nums = []
    for i, c in enumerate(zeckendorf(x)):
        if c == "1":
            # We don't use F[0] or F[1]
            nums.append(i + 2)
    nums.reverse()

    rows = [[f"{x}", " = "], ["", " = "]]
    for num in nums[:-1]:
        rows[0].append(f"F[{num}]")
        rows[0].append(" + ")
        rows[1].append(f"{FIB[num]}")
        rows[1].append(" + ")
    rows[0].append(f"F[{nums[-1]}]")
    rows[1].append(f"{FIB[nums[-1]]}")

    # Build up a max length of each column
    lengths = {}
    for row in rows:
        for i in range(len(row)):
            lengths[i] = max(lengths.get(i, 0), len(row[i]))

    for row in rows:
        # For each cell, pad it by the max length
        output = ""
        for i in range(len(row)):
            if len(output) > 0:
                # Add a space between columns
                output += ""
            cell = row[i] + " " * lengths[i]
            cell = cell[: lengths[i]]
            output += cell
        print(output)


def enc(x):
    # Just add the 'comma'
    rep = zeckendorf(x)
    return rep + "1"


def dec(rep):
    # Remove 'comma'
    no_comma = rep[:-1]
    # and undo
    return frodnekcez(no_comma)


def encode(m):
    # Turn a string into a coded message
    code = []

    for c in m:
        x = ord(c)
        code.append(enc(x))

    return "".join(code)


def decode(code):
    m = []
    i = 0
    while i < len(code):
        j = i
        # Find the comma
        while not code[j] == code[j + 1] == "1":
            j += 1
        # Decode code word for single character
        rep = code[i : j + 2]
        x = dec(rep)
        m.append(chr(x))

        i = j + 2

    return "".join(m)


def main():
    # # Testing
    # for i in range(1, 100000):
    #     assert frodnekcez(zeckendorf(i)) == i == dec(enc(i))
    # for m in random_strings(100, 1000):
    #     assert decode(encode(m)) == m

    # View decomposition
    n = 123
    zeck_rep(n)

    # # Encode a message
    # for c in "SIGma":
    #     print(c)
    #     print(ord(c))
    #     print(enc(ord(c)))
    #     print()

if __name__ == "__main__":
    main()
