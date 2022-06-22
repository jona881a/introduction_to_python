from datastructure_tools import create_datastructure_from_csv

print("\nName set with unique names in csv file ")
print(create_datastructure_from_csv("names.csv", "set","first_name"))

print("\nUnique car brands in csv file")
print(create_datastructure_from_csv("../testdata/cardata.csv", "set","car_make"))