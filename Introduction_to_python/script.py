#Strongly typed language
#Dynamically

def checkDrinkingAge(age):
    if(age > 18 and not age == 0):
        return True
    return False
    

a = "Hello world 33"
age = input("Insert a number: ")
arr = ["Yoda","Darth Vader","Luke"]


if checkDrinkingAge(age):
    print("You are old enough to drink a beer! Cheers!")
else:
    print("Sorry kiddo, your not old enough")


for starwarsCharacters in arr:
    print(starwarsCharacters)