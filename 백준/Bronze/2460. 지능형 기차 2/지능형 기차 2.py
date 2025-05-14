max_pp = 0
current = 0
for i in range(10):
    out_pp, in_pp = map(int, input().split())
    current -= out_pp
    current += in_pp
    if max_pp < current:
        max_pp = current

print(max_pp)

