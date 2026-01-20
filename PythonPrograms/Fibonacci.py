
def fibonacci_series(n):
    num1,num2 = 0,1
    print("Fibonacci Series:", num1, num2, end=" ")
    for a in range(2,n):
        next_num = num1+num2
        print(next_num, end=" ")
        num1,num2 = num2,next_num

fibonacci_series(10)