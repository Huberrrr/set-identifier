from data import data1, data2
from constants import *

# arrays to keep track of attributes
red = []
green = []
purple = []
squiggle = []
circle = []
diamond = []
solid = []
striped = []
blank = []
num1 = []
num2 = []
num3 = []

# which sample data to use
data = data2

# function to find sets
def find_sets():
  set_count = 0
  for i in range(0, 12):
    for j in range(i+1, 12):
      for k in range(j+1, 12):
        print("checking", i, j, k)

        # count how many of the 3 are in the red array
        red_count = 0
        if i in red:
          red_count += 1
        if j in red:
          red_count += 1
        if k in red:
          red_count += 1

        # count how many of the 3 are in the green array
        green_count = 0
        if i in green:
          green_count += 1
        if j in green:
          green_count += 1
        if k in green:
          green_count += 1

        # count how many of the 3 are in the purple array
        purple_count = 0
        if i in purple:
          purple_count += 1
        if j in purple:
          purple_count += 1
        if k in purple:
          purple_count += 1

        # check if any of the counters are 2
        if red_count == 2 or green_count == 2 or purple_count == 2:
          continue

        # count how many of the 3 are in the squiggle array
        squiggle_count = 0
        if i in squiggle:
          squiggle_count += 1
        if j in squiggle:
          squiggle_count += 1
        if k in squiggle:
          squiggle_count += 1

        # count how many of the 3 are in the circle array
        circle_count = 0
        if i in circle:
          circle_count += 1
        if j in circle:
          circle_count += 1
        if k in circle:
          circle_count += 1

        # count how many of the 3 are in the diamond array
        diamond_count = 0
        if i in diamond:
          diamond_count += 1
        if j in diamond:
          diamond_count += 1
        if k in diamond:
          diamond_count += 1

        # check if any of the counters are 2
        if squiggle_count == 2 or circle_count == 2 or diamond_count == 2:
          continue

        # count how many of the 3 are in the solid array
        solid_count = 0
        if i in solid:
          solid_count += 1
        if j in solid:
          solid_count += 1
        if k in solid:
          solid_count += 1

        # count how many of the 3 are in the striped array
        striped_count = 0
        if i in striped:
          striped_count += 1
        if j in striped:
          striped_count += 1
        if k in striped:
          striped_count += 1

        # count how many of the 3 are in the blank array
        blank_count = 0
        if i in blank:
          blank_count += 1
        if j in blank:
          blank_count += 1
        if k in blank:
          blank_count += 1

        # check if any of the counters are 2
        if solid_count == 2 or striped_count == 2 or blank_count == 2:
          continue

        # count how many of the 3 are in the num1 array
        num1_count = 0
        if i in num1:
          num1_count += 1
        if j in num1:
          num1_count += 1
        if k in num1:
          num1_count += 1

        # count how many of the 3 are in the num2 array
        num2_count = 0
        if i in num2:
          num2_count += 1
        if j in num2:
          num2_count += 1
        if k in num2:
          num2_count += 1

        # count how many of the 3 are in the num3 array
        num3_count = 0
        if i in num3:
          num3_count += 1
        if j in num3:
          num3_count += 1
        if k in num3:
          num3_count += 1

        # check if any of the counters are 2
        if num1_count == 2 or num2_count == 2 or num3_count == 2:
          continue

        print("FOUND SET")
        set_count += 1
  return set_count

# adding cards to attribute tracking arrays
for i in range(0, 12):
  # check for color
  if data[i][COLOR] == RED:
    red.append(i)
  elif data[i][COLOR] == GREEN:
    green.append(i)
  elif data[i][COLOR] == PURPLE:
    purple.append(i)

  # check for shape
  if data[i][SHAPE] == SQUIGGLE:
    squiggle.append(i)
  elif data[i][SHAPE] == CIRCLE:
    circle.append(i)
  elif data[i][SHAPE] == DIAMOND:
    diamond.append(i)

  # check for fill
  if data[i][FILL] == SOLID:
    solid.append(i)
  elif data[i][FILL] == STRIPED:
    striped.append(i)
  elif data[i][FILL] == BLANK:
    blank.append(i)

  # check for number
  if data[i][NUMBER] == 1:
    num1.append(i)
  elif data[i][NUMBER] == 2:
    num2.append(i)
  elif data[i][NUMBER] == 3:
    num3.append(i)

print("red array", red)
print("green array", green)
print("purple array", purple)

# check for sets
set_count = find_sets()
print("set count", set_count)
