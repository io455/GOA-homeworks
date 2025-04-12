from turtle import*

def user():
    name =  input("enter your name:")
    lastname = input("enter your last name:")
    age = input("enter your age:")
    location = input("enter your location:")
    occupation = input("entar your occupation:")
    hobby = input("enter your hobby:")
    finall_words = name + " " + lastname + " is " + age + " years old lives in " + location + ", works as an " + occupation + ", and loves  " + hobby + "."

    print(finall_words)


user()