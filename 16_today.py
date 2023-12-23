#Christmis Tree with python
# n=10

# for i in range(0,n):
#     for j in range(1,n-i):
#         print(" ", end="")
#     print("*", end="")
#     for k in range(0,i):
#         print("|", end="")
#     for j in range(1,i):
#         print("|",end="")
#     if i>0:
#         print("*", end="")
#     print()            

#Shutdown PC 
# import os
# shutdown=input("Shutdown your PC? yes/no")
# if shutdown=="no":
#     exit()
# else:
#     os.system("shutdown /s /t 1")    

#Email Slicer
email_id=input("Enter your email id: ")#.strip()
username=email_id[:email_id.index('@')]
domain=email_id[email_id.index('@')+1:]
print(f"Your user name is {username} and your domain name is {domain}")

# animals=["Python","Viper","Cobra"]
# def add_snake(snake_type):
#      animals.append(snake_type)
#      print(animals)
# add_snake("Boa")
# add_snake("Anaconda")

# Guessing number

#Rolling Dice
# import random
# result=random.randint(1,6)
# print("Dice result: ", result)        
    

