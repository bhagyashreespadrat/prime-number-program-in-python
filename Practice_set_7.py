#1
'''num=int(input("enter number"))
for i in range(1,11):
    print(f"{num} X {i}={num*i}")
#OUTPUT:
enter number34
34 X 1=34
34 X 2=68
34 X 3=102
34 X 4=136
34 X 5=170
34 X 6=204
34 X 7=238
34 X 8=272
34 X 9=306
34 X 10=340'''

#2
'''
l1=["Harry","Rohan","Sayali","Shubham","Rahul"]
for name in l1:
    if name.startswith("S"):
        print("hello"+name)
#output:helloSayali
helloShubham'''

#3 factorial number
'''n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(f"the factorial of {n} is {fact}")
#OUTPUT:
enter number:4
the factorial of 4 is 1
the factorial of 4 is 2
the factorial of 4 is 6
the factorial of 4 is 24'''

#4  prime number
'''# taking input from user
number = int(input("Enter any number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")

#OUTPUT:
Enter any number: 2
2 is a prime number'''

# 5 Number is Odd or Even
'''n=int(input("Enter number"))
if n%2==0:
    print("number is even")
else:
    print("number is odd")
#putput:
Enter number25
number is odd'''

#6 Reverse Multiplication table Number
num=int(input("enter number"))
for i in range(10,0,-1):
    print(f"{num} X {i}={num*i}")

#OUTPUT:
enter number34
34 X 1=34
34 X 2=68
34 X 3=102
34 X 4=136
34 X 5=170
34 X 6=204
34 X 7=238
34 X 8=272
34 X 9=306
34 X 10=340'''


