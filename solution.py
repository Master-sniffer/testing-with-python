class task:
    
    def __init__(self):
        print("Submit a number and get an answer!")
    
    def solution(self,n):
        try:
            n=int(n)
            if (n % 3==0 and n % 5==0):
                print("FizzBuzz!")
            elif (n%3 == 0):
                print("Fizz!")
            elif (n%5 == 0):
                print("Buzz!")
            else:
                print("This number is not aliquot on 3 or 5")
        except (RuntimeError, TypeError, NameError, ValueError):
            print("Well, i got no idea what u've entered, but i couldn't solve your number.\nLets start again")

ts = task()
n=(input("Number: "))

while (n!='0'): #i keep here '0' so a user can enter whatever he wants
    ts.solution(n)
    n=input("Number: ")
