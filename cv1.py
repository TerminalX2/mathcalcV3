import math
import statistics
from collections import Counter
from math import sqrt

print("------------------------------------------")
print("                Calculator")
print("------------------------------------------")

print("This a list of the categories of mathematics in the calculator.")
print()

branchList = [
  "Operations", "Standard Deviation", "Prime Number Checker", "Slope"
]
for count, ele in enumerate(branchList, 1):
  print(count, ele)
print()
branchChoice = input("Which of these categories would you like to perform? ")
print()

# arithmetic
if branchChoice == "1":
  arithmeticList = [
    "Addition", "Subtraction", "Multiplication", "Division", "Square Root", "Factorial", 
    "Decimals", "Concatenation", "Exponents", "Recurring Decimals"
  ]
  for count, ele in enumerate(arithmeticList, 1):
    print(count, ele)
  print()
  arithmeticChoice = input("Which of these categories would you like to perform? ")
  print()
  arithmeticString = input("What are your numbers (separated by commas)? ")
  numString = arithmeticString.split(",")
  for i in range(2, len(numString)):
    numString[i] = str(int(numString[i]))
  print()
  # addition
  if arithmeticChoice == "1":
    sum = str(sum(int(num) for num in numString))
    print("The sum is " + sum + ".")
  # subtraction
  elif arithmeticChoice == "2":
    difference = float(numString[0]) - float(numString[1])
    for i in range(2, len(numString)):
        difference = difference - float(numString[i])
    print("The difference is " + str(difference) + ".")
  # multiplication
  elif arithmeticChoice == "3":
    product = str(math.prod([float(num) for num in numString]))
    print("The product is " + product + ".")
  # division
  elif arithmeticChoice == "4":
    quotient = float(numString[0]) / float(numString[1])
    for i in range(2, len(numString)):
      quotient = quotient / float(numString[i])
    print("The quotient is " + str(quotient) + ".")
  # square root
  elif arithmeticChoice == "5":
    squareRoot = str(math.sqrt(float(numString[0])))
    for i in range(2, len(numString)):
      squareRoot = squareRoot + ", " + str(math.sqrt(float(numString[i])))
    print("The square root is " + squareRoot + ".")
  elif arithmeticChoice == "6":

    print("The factorials are " + factorial + ".")
  else:
    print("Please enter a valid number." + "\n" + "Restart the program.")
# standard deviation
elif branchChoice == "2":
  standardDeviationList = [
    "Mean", "Median", "Mode", "Range", "Mean Absolute Deviation"
  ]
  for count, ele in enumerate(standardDeviationList, 1):
    print(count, ele)
  print()
  standardDeviationChoice = input(
    "Which of these categories would you like to perform? "
  )
  print()
  standardDeviationString = input("What are your numbers (separated by commas)? ")
  numString = standardDeviationString.split(",")
  for i in range(2, len(numString)):
    numString[i] = str(int(numString[i]))
  print()
  numString = sorted(numString)
  # mean
  if standardDeviationChoice == "1":
    mean = str(statistics.median([int(num) for num in numString]))
    print("The mean is " + mean + ".")
  # median
  elif standardDeviationChoice == "2":
    median = str(statistics.median([int(num) for num in numString]))
    print("The median is " + median + ".")
  # mode
  elif standardDeviationChoice == "3":
    mode = str(statistics.mode([int(num) for num in numString]))
    print("The mode is " + mode + ".")
  # range
  elif standardDeviationChoice == "4":
    range = str(int(numString[-1]) - int(numString[0]))
    print("The range is " + range + ".")
  # mean absolute deviation
  elif standardDeviationChoice == "5":
    meanAbsoluteDeviation = str(statistics.mean([
      abs(int(num) - statistics.mean([
        int(num) for num in numString
      ])) for num in numString
    ]))
    print("The mean absolute deviation is " + meanAbsoluteDeviation + ".")
  else:
    print("Please enter a valid number." + "\n" + "Restart the program.")
# prime number checker
elif branchChoice == "3":
  p = input("Input an integer to be tested: ")
  print()

  try:
    p = int(p)
    if p <= 1:
        flag = False
    elif p <= 3:
        flag = True
    elif p % 2 == 0 or p % 3 == 0:
        flag = False
    else:
        i = 5
        while i * i <= p:
            if p % i == 0 or p % (i + 2) == 0:
                flag = False
                break
            i += 6
        else:
            flag = True
    if flag:
        print(f"{p} is prime.")
    else:
        print(f"{p} is not prime.")
  except ValueError:
    print(f"{p} is not an integer. Input an integer.")
elif branchChoice == "4":
  y2 = int(input("What is your second y-coordinate? "))
  y1 = int(input("What is your first y-coordinate? "))
  x2 = int(input("What is your second x-coordinate? "))
  x1 = int(input("What is first x-coordinate? "))
  m = (y2 - y1) / x2 - x1
  print()
  print("Slope =", str(m), ".")
