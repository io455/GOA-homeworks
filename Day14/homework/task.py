# control flow არის პროგრამირების პროცესის მიმართულება, რომელიც განსაზღვრავს, თუ როგორ უნდა შესრულდეს პროგრამაში მითითებული ინსტრუქციები. 
# control flow:

# sequencing - კოდის თანმიმდევრობითი (ზემოდან ქვემოთ) გაშვება
# Iteration - კოდის განმეორებითი გამოტანა/ციკლი
# Selection - არჩევანის გაკეთება/ რამოდენიმე მოცემული არჩევნიდან გადაწყვეტილების მიღება პროგრამაში

for i in range(21):
    print(i)

for i in range(31):
    print(i)

for i in range(15, 81):
    print(i)

for i in range(65):
    print(i)

for i in range(0, 51, 3):
    print(i)

total = 0
for i in range(51):
    total += i
print(total)

for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(20, -1, -1):
    print(i)
