from show_gk import draw_graph


p = 31
n = 3
q = 31


def e(a, b):
    cnt = 1
    while (b ** cnt) % a != 1:
        cnt += 1
    return cnt


def nu(m):
    if m % 4 == 0:
        return m
    if m % 4 == 2:
        return m // 2
    return 2 * m


primes = [2, 3, 5, 7, 19, 31]
# problems with 31 and 2

# proposition 2.2 for ^2 A_2(31) over field of characteristic 31
edges = []
for r in primes:
    for s in primes:
        if r == p or s == p:
            continue
        if r % 2 == 0 or s % 2 == 0:
            continue
        k = e(r, q)
        l = e(s, q)
        if 2 <= nu(k) <= nu(l):
            non_adjacent = (nu(k) + nu(l) > n and nu(l) % nu(k) != 0)
            if not non_adjacent:
                edges.append(r * s)


draw_graph("cands/ON/U3(31)", primes, edges)
