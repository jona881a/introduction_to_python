file = open('text.txt','r')

text = file.read()

#Vil ikke køre, da filen allerede er læst, så her skal vi open igen
text2 = file.readline()

print(text)