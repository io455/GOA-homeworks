for i in range(0, 20):
    if i % 2 == 0:
        print("even", i)
    else:
        print("odd", i)


i = 0
while i < 20:
    if i % 2 == 0:
        print("even", i)
    else:
        print("odd", i)
    i += 1


name = input("Enter your name: ")
if name == "ioane":  
    print("coincidence")

score = int(input("Enter your exam score: "))
if score > 70:
    print("passed")
else:
    print("failed")



score = int(input("Enter your score: "))

if score > 80:
    print("Grade: A")
elif score > 60:
    print("Grade: B")
elif score > 40:
    print("Grade: C")
elif score > 20:
    print("Grade: D")
else:
    print("Grade: F")