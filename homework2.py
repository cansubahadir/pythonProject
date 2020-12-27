list1=[]
first_name=input("Please enter your first name:")
last_name=input("Please enter your last name:")
age=int(input("Please enter your age:"))
date_of_birth=input("Please enter your birthday:")


list1.append(first_name)
list1.append(last_name)
list1.append(age)
list1.append(date_of_birth)
print(list1)
for i in list1:
    print(i)

if age < 18:
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street.")
