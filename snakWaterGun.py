'''
1 for snake
-1 for water 
0 for gun
'''
import random
computer =random.choice([-1,0,1])
youstr = (input("Enter your choice -> " ))
youDic = {"s":1,"w":-1 ,"g":0}
reverseDict = {1:"Snake",0:"Gun",-1:"Water"}
you = youDic[youstr]

print(f"you chose {reverseDict[you]} and \n computer chose {reverseDict[computer]}\nresult-> ") 

# if(computer==-1 and you ==1 ): -1-1 = 2
#     print("you win")
# elif(computer ==-1 and you == 0): -1-0 = 1
#     print("computer win and you lose!!")


# elif(computer== 1 and you == -1 ): 1--1=-2
#     print("computer win and you lose!!")
# elif(computer == 1 and you == 0): 1-0=-1
#     print("you win !!")
     

# elif(computer== 0 and you ==1 ):0-1=1
#     print("computer win and you lose!!")
# elif(computer == 0 and you == -1):0--1= -1
#     print("you win")
# elif(computer == you):
#     print("it draw buddy")  
# else:
#     print("something went wrong")

    #or you can use 
if((computer - you)== -1 or (computer - you)== 2):
        print("\tyou lose ")
elif(computer == you):
        print("\tit draw buddy") 
else:
        print("\tyou win ")        
        