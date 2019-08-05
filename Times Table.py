"""
Tom Penny
Prints a times table of a size given by the user
"""
import math

def display_heading(size,spaces):
 display_separator(size,spaces)
 title = str(size) + " x " + str(size) + " Times Table"
 print(get_word(title, (size+1)*spaces))
 print(get_row(0, size,spaces))
 display_separator(size,spaces)
 
def get_user_input():
 size_of_table = int(input("What size table (between 1 and 31)? "))
 while size_of_table < 1 or size_of_table > 31:
  print("Table size should be between 1 and 31.")
  size_of_table = int(input("Please try again: "))
 return size_of_table

def display_separator(size, spaces):
 print("=" * ((size + 1) * spaces))
 
def get_word(words, spaces):
 spaces_to_add = spaces - len(words)
 if spaces_to_add % 2 == 0:
  string_word = int((spaces_to_add/2)) * " " + words + int((spaces_to_add/2)) * " "
 else:
  string_word = (math.ceil(spaces_to_add/2) * " ") + words + (math.floor(spaces_to_add/2) * " ")
 return string_word

def get_row(num, size, spaces):
 if num == 0:
  count = 1
  print_string = "    "
  for count in range(1, size + 1):
   print_string = print_string + get_number(count, spaces)
   count = count + 1
  return print_string  
 else:
  print_string = ""
  count = 1
  for count in  range(1, size + 1):
   print_string = print_string + get_number(count*num, spaces)
  num = " " + str(num)
  num = num[-2:]
  print_string = str(num) + " |" + print_string
  return print_string

def get_number(num, spaces):
 string_number = "    " + str(num)
 string_number = string_number[-spaces:]
 return string_number
 
def display_table(size, spaces):
 num = 1
 for num in range(1, size + 1):
  print(get_row(num, size, spaces))

def main():
 size = get_user_input()
 spaces = len(str(size*size))+2
 display_heading(size,spaces)
 display_table(size,spaces)
 display_separator(size,spaces)
 
main()