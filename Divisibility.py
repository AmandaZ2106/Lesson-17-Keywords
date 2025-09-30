for num in range(15):
    if num%20==0:
        print("Twist")
    elif num%15==0:
        pass
    elif num%10==0:
        print("Bubble")
    elif num%5==0:
        print("Fizz")
    elif num%3==0:
        print("Pop")    
    else:
        print(num)