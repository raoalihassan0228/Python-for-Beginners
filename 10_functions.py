# defining a function
#1
# def print_codanics():
#     print("we are learning with ammar")
#     print("we are learning with ammar")
#     print("we are learning with ammar")

# print_codanics()

#2
# def print_codanics():
#     text = "We are learning with ammar in codanics you tube channel"
#     print(text)
#     print(text)
#     print(text)
# print_codanics()

#3
# def print_codanics(text):
#     print(text)
#     print(text)
#     print(text)
# print_codanics("We are learning with aammar in codanics you tube channel")

#defining a function with if, else and elif statements

# def school_calculator(age):
#     if age==5:
#         print("Hammad can join the school")
#     elif age>5:
#         print("Hammad should join higher secondary school")
#     else:
#         print("Hammad is still a baby")

# school_calculator(10)

#defining a function of future

# def future_age(age):
#     new_age=age+20
#     return new_age
#     print(new_age)

# future_predicted_age=future_age(22)
# print(future_predicted_age)

#i understand function really well

# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# repeat_lyrics()

# def print_twice(bruce):
#     print(bruce)
#     print(bruce)
# print_twice('Spam '*4)    

# def addTwo(a,b):
#     ab= a + b
#     return ab
# result=addTwo(5,15)
# print(result)

score = input("Enter score: ")
def computegrade(score):
    if (score>="0.9"):
        print("Grade A")
    elif (score>="0.8"):
        print("Grade B")
    elif (score>="0.7"):
        print("Grade C")     
    elif (score>="0.6"):
        print("Grade D")
    elif (score<="0.6" and score>="0.5"):
        print("Grade F")
    else:
        print("Bad Score")

computegrade(score)