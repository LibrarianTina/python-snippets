#if statement - tests a condition and then decides to run a piece of code or not.  If statements start with the 'if' keyword and end with a colon(:) to tell the computer the statement is finished.
#if the number of tacos is less than 3, it will print "We need more tacos" and add a taco.  The statement "We have tacoss" will always print, along with the total number of tacos.
tacos = 4

if tacos < 3:
  print("We need more tacos!")
tacos = tacos + 1
print("We have tacos!", tacos)