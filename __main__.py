# price of new equipment
P = 17
# amount of years that we are living
N = 8
# x0 or enum of zero states
zero_state = (0, 1, 2)


def f(t):
    return 30 - t / 2


def r(t):
    return 13 + t / 2


def fi(t):
    if (t <= 5) and (t >= 0):
        return 7
    else:
        return 3


def s(t):
    keep = f(t + 1) - r(t + 1) + fi(t + 2)
    sell = fi(t + 1) + f(0) - r(0) - P + fi(1)
    if keep < sell:
        result = (keep, 0)
    elif sell > keep:
        result = (sell, 1)
    else:
        result = (sell, (0, 1))
    return result


def main():
    return 0

if __name__ == "__main__":
    main()
