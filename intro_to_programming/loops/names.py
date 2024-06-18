# Code below creates a new list containing names in uppercase only 

names = ['Jared', 'Daniel', 'Eugene', 'Beatrice'] # created variable to store names
upper_names = []
index = 0 # list indexes are zero-based so initialise variable with 0

while index < len(names): # loop executes as long as index less than length of names list
  upper_name = names[index].upper() # accesses name stored at names[index] and calls .upper then returns the name in uppercase which is assigned to upper.names
  upper_names.append(upper_name) # appends the latest uppercase name to upper_names list
  index += 1 # increments index by 1 to ensure index < len(names) becomes falsy after the last element

print(upper_names) # ['JARED', 'DANIEL', 'EUGENE', 'BEATRICE']

# The variables names, upper_names, and index are initialised before the loop. If we created them inside the loop, they be reset after each iteration doing nothing.