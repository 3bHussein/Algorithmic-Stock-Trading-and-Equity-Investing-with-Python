

d=['a',4,'3']

for x in d :
    print(x)
    print(d)

list= ['ali','ahmed','noha','asad','mona','olivia','nour',]

for x in list:
    print(x)






# create password generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

Password=""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for char in range(0,nr_letters):
# for char in range(1,nr_letters,1):
    
#   ranChar= random.choice(letters)  
  Password += random.choice(letters) 


for char in range(0,nr_symbols):
  Password += random.choice(symbols) 

for char in range(0,nr_numbers):

  Password += random.choice(numbers) 
  
  
print(Password)


  
 

 

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
