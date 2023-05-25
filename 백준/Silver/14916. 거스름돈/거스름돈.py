money = int(input())
count = 0
while money >= 2:
    if money % 5 == 0:
        count += money//5
        money = money % 5
        break
    else:
        money -= 2
        count += 1

if not money:
    print(count)
else:
    print(-1)