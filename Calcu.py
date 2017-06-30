# Function to add numbers in the given list
def add(numbers_List):
    result = 0
    for numbers in numbers_List:
        result = result + int(numbers)
    return result

#Function to find the average of numbers in the given list
def average(number_list):
    result = 0
    listsum = 0
    listLength = len(number_list)
    listSum = add(number_list)
    result = listsum/listLength
    return result

# Our main program starts here
answer = 0

option = input("Do you want to add or find an average? add/ averag")
if option != "add" and option != "average":
    print ("Invalid option")
    exit()

numbersIn = input("Enter a comma separated by comma:")

numbersList = numbersIn.split(",")

if option =="add":
    answer = add(numbersList)
elif option == "average":
    answer = add(numbersList)

print ("the answer is:", answer)
