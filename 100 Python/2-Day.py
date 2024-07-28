# Data Type

# string
# String_name ='name'
# print(String_name)



# Array of string 
# array_naem='hello'
# x=array_naem[0]
# print(x)


# Error Handler

# num_char =len(input("enter your name "))
# error / to fix it 
# print("you name have"+num_char+ "of character")
#  str function 

# print("you name have "+ str(num_char)+ "  characters")

a="123"
print(type(a))
# error TypeError: can only concatenate str (not "int") to str
# print(a+2)

ai=int(a)

print(type(ai))
# no error print out 125
print(ai+2)

b=123
print(type(b))
bs=str(b)
print(type(bs))

# 23. Mathematical Operations in Python
print(type(6/3))

print(2**3)


# 25. Number Manipulation and F Strings in Python


print(round(2.5444,2))
result =8/2
print(result)
result += 2
print(result)


# f-string

print(f"your score is {result}")


age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
remaining_year=65-int(age)
remaining_weeks=remaining_year*52
print(f"You have {remaining_weeks} weeks left.")
# You have 1924 weeks left.


#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")