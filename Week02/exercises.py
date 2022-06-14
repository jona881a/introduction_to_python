#Slicing

list = ['Hello', 'World', 'Huston', 'we', 'are', 'here']

#Slicing info: the first parameter is from and the last is to, but not with!

print(f'First: {list[1:-1]}')
print(f'Second: {list[0:2]}')
print(f'Third: {list[4:]}')
print(f'Fourth: {list[::2]}')
print(f'Fifth: {list[::-1]}')

#Sort a text

def string_to_list(s):
    list = []
    for i in range(len(s)):
        list.append(s[i])

    return list

def findVowels(s):
    
    s = s.lower()
    s = s.replace(' ','')

    for x in 'aeijouy':
        if(x in s):
            s = s.replace(x,'')
            
    return s

str = findVowels("Hello World")
sortedList = string_to_list(str)
sortedList.sort()
print(sortedList)
#print(string_to_list("Hello World"))