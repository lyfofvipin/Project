import random
sticks = 21

print("There are 21 sticks, you can take 1-4 sticks at a time.")
print("Whoever will pick the last stick will loose")
flag = 1
while True:

    if flag != 0:
        x = random.randrange(1,5) if sticks > 5 else sticks-1
        if sticks - x < 1 :
            continue
        print('Computer took: ', x)
        print('Sticks left : ', sticks-x)
        sticks -= x
        if sticks == 1:
            print("You loose")
            break
        flag = 1
    n = int(input("Take a stick : "))
    if n > 4 or n < 1:
        print("Wrong choice")
        print('Sticks left : ', sticks)
        flag = 0
        continue
    flag = 1
    sticks -= n
    if sticks == 1:
        print("You won")
        break
    print('Sticks left : ', sticks)
