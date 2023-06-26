# 1. Fill in the blanks to print the numbers from 15 to 5, counting down by fives.
number = 15 # Initialize the variable
while number > 0 : # Complete the while loop condition
    print(number, end=" ")
    number -= 5 # Increment the variable

# Should print 15 10 5 

# 2. Find and correct the error in the for loop below.  The loop should print every even number from 2 to 12.
for number in range(2,13,2):
    print(number)

# Should print:
# 2
# 4
# 6
# 8
# 10
# 12

# 3. Fill in the blanks to complete the function “even_numbers(n)”. This function should count how many even numbers exist in 
# a sequence from 0 to the given “n”number, where 0 counts as an even number.  For example, even_numbers(25) should return 13,
# and even_numbers(6) should return 4.
def even_numbers(n):
    count = 0
    current_number = 0
    while n >= current_number :# Complete the while loop condition
        if current_number % 2 == 0:
            count += 1 # Increment the appropriate variable
        current_number +=1 # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1

# 4. Fill in the blanks to complete the “multiplication_table” function. This function should print a multiplication table, where
# each number is the result of multiplying the first number of its row by the number at the top of its column. Complete the 
# range sequences in the nested loops so that “multiplication_table(1, 3)” will print:
# 123
# 246
# 369

def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start,stop + 1): 
         # Complete the inner loop range
        for y in range(start, stop + 1):
            # Prints the value of "x" multiplied by "y" 
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above

# 5. Fill in the blanks to complete the “counter” function. This function should count down from the “start” to “stop” variables when
# “start” is bigger than “stop”. Otherwise, it should count up from “start” to “stop”. Complete the code so that a function call like
# “counter(3, 1)” will return “Counting down: 3, 2, 1” and “counter(2, 5)” will return “Counting up: 2, 3, 4, 5”.
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop: # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start > stop:
                return_string += ","
            start -= 1 # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while start <= stop: # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            start += 1 # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

# 6. Fill in the blanks to complete the “even_numbers” function. This function should return a space-separated string of all positive
# even numbers, excluding 0, up to and including the “maximum” variable that's passed into the function. Complete the for loop so
# that a function call like “even_numbers(6)” will return the numbers “2 4 6”.  

def even_numbers(maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all even numbers
    # up to and including the "maximum" value, but excluding 0.
    for x in range (maximum + 1):  
        # Complete the body of the loop by appending the even number
        # followed by a space to the "return_string" variable.
        if (x % 2) == 0 and x != 0:
            return_string += str (x) + " "          
    # This .strip command will remove the final " " space at the end of
    # the "return_string".
    return return_string.strip() 

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)

# 7. Fill in the blanks to complete the “confirm_length” function. This function should return how many characters a string contains as long 
# as it has one or more characters, otherwise it will return 0. Complete the string operations needed in this function so that input like 
# "Monday" will produce the output "6".
def confirm_length(word):

    # Complete the condition statement using a string operation. 
    if len(word) > 0 :        
        return len(word) 
    else:
        return 0

print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0

# 8. Fill in the blank to complete the “string_words” function. This function should split up the words in the given “string” and return
# the number of words in the “string”.  Complete the string operation and method needed in this function so that a function call like 
# "string_words("Hello, World")" will return the output "2".

def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split())

print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4

# 9. Consider the following scenario about using Python lists:
 
# A professor gave his two assistants, Jaime and Drew, the task of keeping an attendance list of students in the order they arrive
# in the classroom. Drew was the first one to note which students arrived, and then Jaime took over. After the class, they each 
# entered their lists into the computer and emailed them to the professor. The professor wants to combine the two lists into one, 
# in the order of each student's arrival. Jaime emailed a follow-up, saying that her list is in reverse order.

    # 1. Accept two lists through the function’s parameters;
    # 2. Reverse the order of “list1”; 
    # 3. Combine the two lists so that “list2” comes first, followed by “list1”;
    # 4. return the new list. 

def combine_lists(list1, list2):
  combined_list = []# Initialize an empty list variable
  list1 = list1[::-1]# Reverse the order of "list1"
  list2 = list2 + list1 # Combine the two lists 
  combined_list = list2
  return combined_list  
  
Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]

print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']

# 10. Fill in the blank to complete the “even_numbers” function. This function should use a list comprehension to create 
# a list of even numbers using a conditional if statement with the modulo operator to test for numbers evenly divisible by 2. 
# The function receives two variables and should return the list of even numbers that occur between the “first” and “last” variables
# exclusively (meaning don’t modify the default behavior of the range to exclude the “end” value in the range). For example, 
# even_numbers(2, 7) should return [2, 4, 6].  

def even_numbers(first, last):
  return [x for x in range(first,last) if x % 2 == 0]

print(even_numbers(4, 14)) # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]

# 11. Consider the following scenario about using Python dictionaries: 

# Tessa and Rick are hosting a party. Together, they sent out invitations, and collected the responses in a dictionary, with names 
# of their friends and the number of guests each friend will be bringing. 

# Complete the function so that the “check_guests” function retrieves the number of guests (value)  the specified friend “guest” 
# (key) is bringing. This function should:
        
        # 1. Accept a dictionary “guest_list” and a key “guest” variable passed through the function parameters;
        # 2. Print the values associated with the key variable.

def check_guests(guest_list, guest):
  return guest_list[guest] # Return the value for the given key

guest_list = { "Adam":3, "Camila":3, "David":5, "Jamal":3, "Charley":2, "Titus":1, "Raj":6, "Noemi":1, "Sakira":3, "Chidi":5}

print(check_guests(guest_list, "Adam")) # Should print 3
print(check_guests(guest_list, "Sakira")) # Should print 3
print(check_guests(guest_list, "Charley")) # Should print 2

# 12. Consider the following scenario about using Python dictionaries:

# A teacher is using a dictionary to store student grades. The grades are stored as a point value out of 100.  Currently, the teacher has a 
# dictionary setup for Term 1 grades and wants to duplicate it for Term 2. The student name keys in the dictionary should stay the same,
# but the grade values should be reset to 0.

# Complete the “setup_gradebook” function so that input like “{"James": 93, "Felicity": 98, "Barakaa": 80}” will produce a resulting dictionary 
# that contains  “{"James": 0, "Felicity": 0, "Barakaa": 0}”. This function should: 

    # 1. Accept a dictionary “old_gradebook” variable through the function’s parameters;
    # 2. Make a copy of the “old_gradebook” dictionary;
    # 3. Iterate over each key and value pair in the new dictionary;
    # 4. Replace the value for each key with the number 0;
    # 5. Return the new dictionary.

def setup_gradebook(old_gradebook):
  # Use a dictionary method to create a new copy of the "old_gradebook".
  new_gradebook = old_gradebook 
    # Complete the for loop to iterate over the new gradebook. 
  for name, points in new_gradebook.items():
      # Use a dictionary operation to reset the grade values to 0.      
      new_gradebook[name] = 0
  return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}
