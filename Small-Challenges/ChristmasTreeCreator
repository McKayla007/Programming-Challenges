# Solution Code: Christmas Tree Creator
# This program will print a Christmas tree pattern using asterisks

# ----------------
# Subprograms
# ----------------

def draw_christmas_tree(height):
  row = 1
  while row <= height:
    spaces = height - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)
    row += 1
  draw_stump(height)
    
def draw_stump(height):
  stump_width = int(height/3)
  stump_height = int(height/3)
  spaces = int((2 * height - stump_width) / 2)
  row = 0
  while row <= stump_height:
    print(" " * spaces + "|" * stump_width)
    row += 1

# ----------------
# Main program
# ----------------

height = int(input("Enter the height of the Christmas tree: "))
draw_christmas_tree(height)
