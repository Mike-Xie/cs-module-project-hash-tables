all_ints = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
names = ["Bob", "Jane", "Bill"]

divisible_by_three = list(filter(lambda x: x % 3 == 0, all_ints))
names_that_are_4_chars = list(filter(lambda x: len(x) == 4, names))

for item in divisible_by_three:
	print(item)

# Print out all of the strings in the following array that represent a number divisible by 3:
# [
#   "five",
#   "twenty six",
#   "nine hundred ninety nine,
#   "twelve",
#   "eighteen",
#   "one hundred one",
#   "fifty two",
#   "forty one",
#   "seventy seven",
#   "six",
#   "twelve",
#   "four",
#   "sixteen"
# ]
# The expected output for the above input is:
# nine hundred ninety nine
# twelve
# eighteen
# six
# twelve
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
# pretty much you are writing a parser
# either start at the front or the back and recurse to other end
# while keeping a running total

# the strings alternate a number and an optional multiplier like
# 9 x 100 + 90 + 9 


# terminals are below:
# one
# two
# three
# four
# five
# six
# seven
# eight
# nine
# ten 
# eleven
# twelve
# thirteen
# fourteen
# fifteen
# sixteen
# seventeen
# eighteen
# nineteen 

