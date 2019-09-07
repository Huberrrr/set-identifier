from data import data1, data2
from constants import *
import timeit
start = timeit.default_timer()

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
data = data1

# function to find sets
def find_sets():
  set_count = 0
  for i in range(0, 12):
    for j in range(i+1, 12):
      for k in range(j+1, 12):

        # check if red has any combo of 2
        if (i in red and j in red and k not in red) or (i in red and j not in red and k in red) or (i not in red and j in red and k in red):
          continue

        # check if green has any combo of 2
        if (i in green and j in green and k not in green) or (i in green and j not in green and k in green) or (i not in green and j in green and k in green):
          continue

        # check if purple has any combo of 2
        if (i in purple and j in purple and k not in purple) or (i in purple and j not in purple and k in purple) or (i not in purple and j in purple and k in purple):
          continue

        # check if squiggle has any combo of 2
        if (i in squiggle and j in squiggle and k not in squiggle) or (i in squiggle and j not in squiggle and k in squiggle) or (i not in squiggle and j in squiggle and k in squiggle):
          continue

        # check if circle has any combo of 2
        if (i in circle and j in circle and k not in circle) or (i in circle and j not in circle and k in circle) or (i not in circle and j in circle and k in circle):
          continue

        # check if diamond has any combo of 2
        if (i in diamond and j in diamond and k not in diamond) or (i in diamond and j not in diamond and k in diamond) or (i not in diamond and j in diamond and k in diamond):
          continue

        # check if solid has any combo of 2
        if (i in solid and j in solid and k not in solid) or (i in solid and j not in solid and k in solid) or (i not in solid and j in solid and k in solid):
          continue

        # check if striped has any combo of 2
        if (i in striped and j in striped and k not in striped) or (i in striped and j not in striped and k in striped) or (i not in striped and j in striped and k in striped):
          continue

        # check if blank has any combo of 2
        if (i in blank and j in blank and k not in blank) or (i in blank and j not in blank and k in blank) or (i not in blank and j in blank and k in blank):
          continue

        # check if num1 has any combo of 2
        if (i in num1 and j in num1 and k not in num1) or (i in num1 and j not in num1 and k in num1) or (i not in num1 and j in num1 and k in num1):
          continue

        # check if num2 has any combo of 2
        if (i in num2 and j in num2 and k not in num2) or (i in num2 and j not in num2 and k in num2) or (i not in num2 and j in num2 and k in num2):
          continue

        # check if num3 has any combo of 2
        if (i in num3 and j in num3 and k not in num3) or (i in num3 and j not in num3 and k in num3) or (i not in num3 and j in num3 and k in num3):
          continue

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

# check for sets
set_count = find_sets()
stop = timeit.default_timer()
print("found", set_count, "sets in", ((stop - start)*1000), "ms")
