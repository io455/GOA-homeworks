#from turtle import *

name = "ioane"
surname = "meladze"
city = "თბილისი"
age = 14
height = 182.5
weight = 88.5
grade = 9

learn_programming = True
will_be_lazy = False

def get_boolean_text(val):
    if val == True:
        return "დიახ"
    else:
        return "არა"
    
print("ჩემი სახელი არის " + name + ", ხოლო გვარი " + surname 
      + "\n" + ", სიმაღლე - " + str(height) + ", წონა - " + str(weight)
      + "\n" + ", ასაკი - " + str(age) + ", კლასი - " + str(grade) 
      + "\n" + ", საცხოვრებელი ადგილი: " + city
      + "\n" + ", მსურს ვისწავლო პროგრამირება: " + get_boolean_text(learn_programming)  
      + "\n" + ", ვიზარმაცებ პროგრამირების სწავლისას: " + get_boolean_text(will_be_lazy))