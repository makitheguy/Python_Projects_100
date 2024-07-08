def FizzBuzz(number):
    for i in range(1,number):
        
        if i%15==0:
            print("FizzBuzz")
            continue
        elif i%3==0:
            print("FIzz")
            continue
        elif i%5==0:
            print("Buzz")
            continue
        print(i)
        i=i+1

print(FizzBuzz(31))
