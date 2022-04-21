# Peter's Problem 2022 No.19

from itertools import permutations

digits = [2, 3, 4, 5, 6, 7, 8, 9]

def check_if_correct(a, b, c, d, e, f, g):
    condition1 = False
    condition2 = False
    condition3 = False
    condition4 = False

    if (a * b) / c == 15:
        condition1 = True
    if (d - 1) * e == 24:
        condition2 = True
    if (a + d) - f == 2:
        condition3 = True
    if (b / 1) + g == 15:
        condition4 = True
    
    if condition1 and condition2 and condition3 and condition4:
        return True

for perm in list(permutations(digits)):
    a = perm[0]
    b = perm[1]
    c = perm[2]
    d = perm[3]
    e = perm[4]
    f = perm[5]
    g = perm[6]
    h = perm[7]

    if check_if_correct(a, b, c, d, e, f, g):
        k = (f - g) + h
        l = (c * e) / h
        if l.is_integer():
            print(f"K: {k}\nL: {int(l)}")
