from constants import *
import random
import pandas as pd

invalid_set = [
  {
    COLOR: RED,
    SHAPE: CIRCLE,
    FILL: BLANK,
    NUMBER: 2
  },
  {
    COLOR: PURPLE,
    SHAPE: SQUIGGLE,
    FILL: SOLID,
    NUMBER: 1
  },
  {
    COLOR: RED,
    SHAPE: DIAMOND,
    FILL: SOLID,
    NUMBER: 3
  }
]

valid_set = [
  {
    COLOR: RED,
    SHAPE: CIRCLE,
    FILL: BLANK,
    NUMBER: 2
  },
  {
    COLOR: RED,
    SHAPE: SQUIGGLE,
    FILL: SOLID,
    NUMBER: 1
  },
  {
    COLOR: RED,
    SHAPE: DIAMOND,
    FILL: STRIPED,
    NUMBER: 3
  }
]

colors = [RED, GREEN, PURPLE]
shapes = [SQUIGGLE, CIRCLE, DIAMOND]
fills = [SOLID, STRIPED, BLANK]
numbers = [1, 2, 3]

def check_if_set(data):
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

  for i in range(0, 3):
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
  for i in range(0, 3):
    for j in range(i+1, 3):
      for k in range(j+1, 3):
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

        return True

  return False

def get_random_row():
  # generate set
  generated_set = []
  for _ in range(0, 3):
    generated_set.append({
      COLOR: colors[random.randint(0, 2)],
      SHAPE: shapes[random.randint(0, 2)],
      FILL: fills[random.randint(0, 2)],
      NUMBER: numbers[random.randint(0, 2)]
    })

  # create row to add to csv
  row = {
    "color1": [generated_set[0][COLOR]],
    "shape1": [generated_set[0][SHAPE]],
    "fill1": [generated_set[0][FILL]],
    "number1": [generated_set[0][NUMBER]],
    "color2": [generated_set[1][COLOR]],
    "shape2": [generated_set[1][SHAPE]],
    "fill2": [generated_set[1][FILL]],
    "number2": [generated_set[1][NUMBER]],
    "color3": [generated_set[2][COLOR]],
    "shape3": [generated_set[2][SHAPE]],
    "fill3": [generated_set[2][FILL]],
    "number3": [generated_set[2][NUMBER]],
    "set": [check_if_set(generated_set)]
  }

  return row

# create dataframe
csv_df = pd.DataFrame(get_random_row())

#track trues and falses
num_trues = 0
num_falses = 0

# add data to dataframe
while True:
  print(num_trues, num_falses)

  # get a random row
  row = get_random_row()

  # check if loop is done with one or both
  if num_trues > 1000 and num_falses > 1000:
    break
  elif row["set"] == [False] and num_falses > 1000:
    continue
  elif row["set"] == [True] and num_trues > 1000:
    continue

  # increment counters
  if row["set"] == [False]:
    num_falses += 1
  elif row["set"] == [True]:
    num_trues += 1

  # create dataframe for new row
  row_df = pd.DataFrame(row)

  # add row to dataframe
  csv_df = csv_df.append(row_df, ignore_index=True)

# export the csv
csv_df.to_csv("generated_data.csv")
