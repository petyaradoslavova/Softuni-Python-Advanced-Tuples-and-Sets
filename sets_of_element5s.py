n,m = [int(x) for x in input().split()]

set_for_n = {input() for _ in range(n)}
set_for_m = {input() for _ in range(m)}

print(*set_for_n.intersection(set_for_m),sep="\n")