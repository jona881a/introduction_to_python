directoryBoard = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte","Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

#Assignment 1
print("-----------------Assignment 1-----------------")
print()
#Part 1 and 2
notAnEmployee = directoryBoard.intersection(employees)

print(f'1. and 2. {notAnEmployee} is the only one who is an employee, the rest on the board of directory is not employees')

#Part 3
boardMemberFromManagement = management.intersection(directoryBoard)

print(f'3. {boardMemberFromManagement} is the ones who are from management, which is also members of the directory board')

#Part 4
employeesAlsoInManagement = management.intersection(employees)

print(f'4. {employeesAlsoInManagement} are the employees which is also on the management team')

#Part 5
managementAlsoOnBoard = management.intersection(directoryBoard)

print(f'5. {managementAlsoOnBoard} is the only one which is from management and are also on the board of directory')

#Part 6
memberOfAllSets = employees.intersection(management).intersection(directoryBoard)

print(f'6. {memberOfAllSets} is the only one, which is present in all sets')

#Part 7
employeesNotInManagementOrBoardDirectory = employees.difference(management).difference(directoryBoard)

print(f'7. {employeesNotInManagementOrBoardDirectory} which is not in management or board directory')

#Verify
print(f'Verification of 7: {employeesNotInManagementOrBoardDirectory.intersection(directoryBoard).intersection(management)} which means that assignment 7 is correct')

#Assignment 2
print()
print("-----------------Assignment 2-----------------")
print()

dict = {"a": "Alpha",
        "b" : "Beta", 
        "g": "Gamma"}
#we make a tuple from the key and the value
listOfTuples = [(k, v) for k, v in dict.items()]
#Another option, which is implicit
print([x for x in dict.items()])
print(listOfTuples)

#Assignment 3
print()
print("-----------------Assignment 3-----------------")
print()

set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

print(f'The following 2 sets {set1} and {set2}')

print(f'Union of set1 and 2 {set1.union(set2)}')
print(f'Symmetric difference in set1 and set2 {set1.symmetric_difference(set2)}')
print(f'Difference in set1 and set2 {set1.difference(set2)} which means that there are no difference from set1 to set2')
print(f'If there are a disjoining between set1 and set2 {set1.isdisjoint(set2)}, which means that the set is not disjoint')

print()
print("-----------------Assignment 4-----------------")
print()

#Part 1
monthDict = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEPT": 9,
    "OKT": 10,
    "NOV": 11,
    "DEC": 12
}
print(monthDict)

#Part 2

def datesplitter(str):
    dateList = str.split("-")[::-1]

    for item in monthDict.items():
        if dateList[1] in item:
            dateList[1] = item[-1]

    if int(dateList[0]) <= 99 and int(dateList[0]) > 22:
        dateList[0] = f'19{dateList[0]}'
    else:
        dateList[0] = f'20{dateList[0]}'

    return tuple(dateList)

#Part 3
print(datesplitter("8-MAR-85"))
print(datesplitter("10-JAN-21"))