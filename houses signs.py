"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00
# Charge for this sign.
charge = 35
# Number of characters.
numChars = 18
# Color of characters.
color = "Black"
# Type of wood.
woodType = "Oak"
# Write assignment and if statements here as appropriate.
if numChars > 5:
    charge += 4 * (numChars - 5)

if woodType == "Oak":
    charge += 20.00

if color == "Gold":
    charge += 15.00
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))