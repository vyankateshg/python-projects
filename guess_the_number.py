import random 
n = random.randint(1,100)
a =-1
guesses = 0
if(n<50):
    print("the number is under 50")
else:
    print("the number between 50 to 100")    
while(a != n):
    guesses += 1
    a = int(input("Guess the number : -> "))
    if(a>n):
        print("lower numner please ")
    elif(a<n):
        print("Higher number please ") 

print(f"You gussed in {guesses} attemepts the number was {n}")       
