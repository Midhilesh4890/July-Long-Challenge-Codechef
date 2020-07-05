def sumofdigits(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum

for i in range(int(input())):
    N = int(input())
    chef_count = 0
    morty_count = 0
    for i in range(N):
        chef,morty = list(map(int,input().split()))
        if sumofdigits(chef) == sumofdigits(morty):
            chef_count += 1
            morty_count += 1
        elif sumofdigits(chef) > sumofdigits(morty):
            chef_count += 1
        else:
            morty_count += 1
            
    if chef_count == morty_count:
        print(2,chef_count)

    elif chef_count > morty_count:
        print(0,chef_count)

    else:
        print(1,morty_count)
