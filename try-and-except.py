#try and except - tests if the user inputs the right data type or value.  triggers an except statement - message to user about what is wrong.
zip_code = input("What is your zipcode?: ")

try:
  int(zip_code)

except:
  print("Your input was not a number. ")