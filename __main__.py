# price of new equipment
P = 17
# amount of years that we are living
N = 8


# calculate income based on equipment age t
def f(t):
    return 30 - t / 2


# calculate equipments consumption based on equipment age t
def r(t):
    return 13 + t / 2


# calculate income of selling the equipment of age t
def fi(t):
    if (t <= 5) and (t >= 0):
        return 7
    else:
        return 3


# function of total income based on current year and declared age of equipment t
def s(t, current_year):
    if current_year == 7:
        keep_decision = (f(t + 1) - r(t + 1) + fi(t + 2), '0')
        sell_decision = (fi(t + 1) + f(0) - r(0) - P + fi(1), '1')
    else:
        keep_decision = (f(t + 1) - r(t + 1) + s(t + 1, current_year + 1)[0], '0' + s(t + 1, current_year + 1)[1])
        sell_decision = (fi(t + 1) + f(0) - r(0) - P + s(0, current_year + 1)[0], '1' + s(0, current_year + 1)[1])
    if keep_decision[0] >= sell_decision[0]:
        return keep_decision
    else:
        return sell_decision


def main():
    print "last iteration"
    for state in range(0, 3 + N):
        print s(state, 7)
    print "first iteration"
    for state in range(0, 3):
        print s(state, 0)
    return 0


if __name__ == "__main__":
    main()
