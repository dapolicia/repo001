import random

firstInput = input("Enter a String to be randomized : ")
listOfFirstInput = list(firstInput)

print("List of First Input  "  + str(listOfFirstInput))

yuj = 0
howManyTimes = len(listOfFirstInput)
print("This program should run " + str(howManyTimes) + " times")
while yuj < howManyTimes:
    print("Run number")
    print(yuj + 1)
    print("Current Letter")
    fromPosition = listOfFirstInput[yuj]
    print(listOfFirstInput[yuj])
    print("Current position")
    print(yuj)
    print("New position")
    tempHolder = listOfFirstInput[yuj]
    juy = random.randint(1, howManyTimes - 1 )
    print(juy)
    print("Whats currently at New position")
    destPostion = listOfFirstInput[juy]
    print(destPostion)
    print("Now lets swap them")
    listOfFirstInput[yuj] = destPostion
    listOfFirstInput[juy] = fromPosition
    print(listOfFirstInput)
    yuj = yuj + 1
    print("\n")

finalPrint = str(listOfFirstInput)
print(finalPrint)



