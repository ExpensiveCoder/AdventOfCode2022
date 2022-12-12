# Joshua McDaniel
# Advent of Code 2022
# Day 1 - Part 2
# Counting Calories
# Answer: 206152

max = 0
count = 1
curr = 0
cal = []

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

    # update array with Calories held by Elf
    cal.append(curr)
    # reset curr to 0 for each new Elf
    curr = 0
  else:
    # adds each line to curr
    curr += int(line) 
    if curr > max:
      max = curr
cal.append(curr)

# sort the array (largest to smallest)
cal.sort(reverse=True)
# add up first 3 elements
total = cal[0] + cal[1] + cal[2]

f.close()
print("The total calories of the most 3 elves are", total)
print("This file contains", count, "elves")
print("The max calories is", max)
