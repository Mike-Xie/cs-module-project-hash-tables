def some_function(a):
  if a <= 5:
   return a + 5
  elif 5 < a < 30:
   return a + 7
  else:
   return a * 100 

x = some_function(10)

print(x)