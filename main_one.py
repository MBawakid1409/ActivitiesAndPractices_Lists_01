# Activities & Practices

# 01 "Append Size"
# For the first code challenge, we are going to calculate the length of a list and then append the value to the end of the list. Here is what we need to do:

# 1. Define the function to accept one parameter for our list
# 2. Get the length of the list
# 3. Append the length of the list to the end of the list
# 4. Return the modified list

# Create a function called [append_size] that has one parameter named [lst].
# The function should append the size of [lst] (inclusive) to the end of [lst]. The function should then return this new list.
# For example, if [lst] was [[23, 42, 108]], the function should return [[23, 42, 108, 3]] because the size of [lst] was originally [3].
print("'Append Size' challenge")
def append_size(lst):
  lst.append(len(lst))
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))  
print("--------------------------------")

# 02 "Append Sum"
# Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end. After doing so, it will repeat this process two more times and return the resulting list. You can choose to use a loop or manually use three lines. Here are the steps we need:

# 1. Define the function to accept one parameter for our list of numbers
# 2. Add the last and second to last elements from our list together
# 3. Append the calculated value to the end of our list.
# 4. Repeat steps 2 and 3 two more times
# 5. Return the modified list

# Write a function named [append_sum] that has one parameter — a list named named [lst].
# The function should add the last two elements of [lst] together and append the result to [lst]. It should do this process three times and then return [lst]
# For example, if [lst] started as [[1, 1, 2]], the final result should be [[1, 1, 2, 3, 5, 8]].
print("'Append Sum' challenge")
def append_sum(lst):
  addTwoElements = lst[-2] + lst[-1]
  lst.append(addTwoElements)
  addTwoElements2 = lst[-2] + lst[-1]
  lst.append(addTwoElements2)
  addTwoElements3 = lst[-2] + lst[-1]
  lst.append(addTwoElements3)
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
# Output: [1, 1, 2, 3, 5, 8]
print("--------------------------------")

# 03 "Larger List"
# Let’s say we are working with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt. In the case where they have the same number of items, return the last item from the first conveyor belt. In our code, we can represent the belts using lists. Here are the steps:

# 1. Define the function to accept two parameters for our two lists of numbers
# 2. Check if the length of the first list is greater than or equal to the length of the second list
# 3. If true, then return the last element from the first list. Otherwise, return the last element from the second list

# Write a function named [larger_list] that has two parameters named [lst1] and [lst2].
#The function should return the last element of the list that contains more elements.If both lists are the same size, then return the last element of [lst1]
print("'Larger List' challenge")
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))    
# 5
print("--------------------------------")

# 04 "More Than N"
# Our factory produces a variety of different flavored snacks and we want to check the number of instances of a certain type. We have a conveyor belt full of different types of snacks represented by different numbers. Our function will accept a list of numbers (representing the type of snack), a number for the second parameter (the type of snack we are looking for), and another number as the third parameter (the maximum number of that type of snack on the conveyor belt). The function will return True if the snack we are searching for appears more times than we provided as our third parameter. These are the steps we need:

# 1. Define the function to accept three parameters, a list of numbers, a number to look for, and a number for the number of instances
# 2. Count the number of occurrences of [item] (the second parameter) in [lst] (the first parameter)
# 3. If the number of occurrences is greater than [n] (the third parameter), return [True]. Otherwise, return [False]

# Create a function named [more_than_n] that has three parameters named [lst], [item], and [n].
# The function should return [True] if [item] appears in the list more than [n] times. The function should return [False] otherwise.
print("'More Than N' challenge")
def more_than_n(lst1, item, n):
  if lst1.count(item) > n:
    return True 
  else:
    return False 

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
# True
print(more_than_n([2, 3, 4], 2, 1))
# False   
print("--------------------------------")

# 05 "Combine Sort"
# Finally, let’s create a function that combines two different lists together and then sorts them. To do this we can combine the lists with an operation and then sort using a function call. Here are the steps we need to use:

# 1. Define the function to accept two parameters, one for each list.
# 2. Combine the two lists together
# 3. Sort the result
# 4. Return the sorted and combined list

# Write a function named [combine_sort] that has two parameters named [lst1] and [lst2].
# The function should combine these two lists into one new list and sort the result. Return the new sorted list.
print("'Combine Sort' challenge")
def combine_sort(lst1, lst2):
  result = lst1[0:] + lst2[0:]
  #sorted_list = result.sort()  # 1st solution
  sorted_list = sorted(result)  # or another
  #return result  # required 2 times return one with return result
  return sorted_list  # and second with sorted_list
  # This is if solve problem with 1st solution
  # 2nd solution is better wich just use sorted() ans assigned it with variable and return the variable

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))  
# Output: [-10, 2, 2, 4, 5, 5, 10, 10]