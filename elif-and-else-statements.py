#Elif will test another condition when the if statement is false. You can have more than one elif statement, but only one if statement in a block of code.
#Else statements appear at the end of the block of code and will perform an action if all the preceding conditions were false.  There can only be one else statement in a block of code.
tacos = 2

if tacos == 0:
  print("We need more tacos, pronto!")
elif tacos == 1:
  print("Only one taco left!")
elif tacos <= 3:
  print("Time to order more tacos!")
else:
  print("We have enough tacos.")