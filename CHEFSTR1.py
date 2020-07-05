for i in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    
    count = 0
    for i in range(1,len(arr)):
        count = count + abs(arr[i-1] - arr[i])
        
    print(count - len(arr) + 1)
    