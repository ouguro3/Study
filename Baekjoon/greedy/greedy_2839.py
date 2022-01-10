n = int(input())
cal = 0
five = 0
three = 0
while n > 0:
    if n % 5 == 0:
        five = n//5
        n = 0
    else:
        n -= 3
        three += 1
if n < 0:
    print(-1)
else:
    print(five+three)


    

