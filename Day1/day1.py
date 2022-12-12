# Joshua McDaniel
# Advent of Code 2022
# Day 1 - Part 1
# Counting Calories
# Answer: 69528


max = 0
count = 1
curr = 0

# Opens file and reads input
try:
  f = open("day1/day1.txt","r")
except:
  print("File not found, please check spelling")

# Loops through file input
for line in f: 
  # if the line is empty move to next elf and update max
  if line == '\n':
    count = count + 1
    # max update
    if curr > max:
      max = curr
    # reset curr to 0 for each new Elf
    curr = 0
  else:
    # adds each line to curr
    curr += int(line) 
    if curr > max:
      max = curr

f.close()
print("This file contains", count, "elves")
print("The max calories is", max)
