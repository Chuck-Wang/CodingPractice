# The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully
# wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still
# affecting them - nobody can even agree on how to cut the fabric.
#
# The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.
#
# Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and
# consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as
# follows:
#
# The number of inches between the left edge of the fabric and the left edge of the rectangle.
# The number of inches between the top edge of the fabric and the top edge of the rectangle.
# The width of the rectangle in inches.
# The height of the rectangle in inches.
# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from
# the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and
# ignores the square inches of fabric represented by .) in the diagram below:
#
# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........
# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For
# example, consider the following claims:
#
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# Visually, these claim the following areas:
#
# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........
# The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not
# overlap either of them.)
#
# If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric
# are within two or more claims?

from collections import defaultdict


def func1():
    with open("input_3") as file:
        input_list = file.read().split("\n")
    dict = {}
    count = 0
    for i in range(1, 1001):
        dict[i] = defaultdict(int)
    for x in input_list:
        list = x.split()
        dim = list[2].split(",")
        dim[1] = dim[1].split(":")[0]
        name = list[0]
        a = int(dim[0])
        b = int(dim[1])
        size = list[3].split("x")
        x = int(size[0])
        y = int(size[1])
        flag = False
        for i in range(0, x):
            for j in range(0, y):
                if dict[i+a+1][j+b+1] == 1:
                    dict[i + a + 1][j + b + 1] = 2
                    flag = True
                if dict[i+a+1][j+b+1] == 2:
                    flag = True
                else:
                    dict[i + a + 1][j + b + 1] = 1
        if flag == False:
            print name
    for x in range(0, 1000):
        for y in range(0, 1000):
            if dict[x+1][y+1] == 2:
                count += 1
    print count

# func1()


# Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any
# other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!
#
# For example, in the claims above, only claim 3 is intact after all claims are made.
#
# What is the ID of the only claim that doesn't overlap?
def func2():
    with open("input_3") as file:
        input_list = file.read().split("\n")
    dict = {}
    count = 0
    for i in range(1, 1001):
        dict[i] = defaultdict(int)
    for x in input_list:
        list = x.split()
        dim = list[2].split(",")
        dim[1] = dim[1].split(":")[0]
        name = list[0]
        a = int(dim[0])
        b = int(dim[1])
        size = list[3].split("x")
        x = int(size[0])
        y = int(size[1])
        flag = False
        for i in range(0, x):
            for j in range(0, y):
                if dict[i+a+1][j+b+1] == 1:
                    dict[i + a + 1][j + b + 1] = 2
                    flag = True
                if dict[i+a+1][j+b+1] == 2:
                    flag = True
                else:
                    dict[i + a + 1][j + b + 1] = 1
    for x in input_list:
        list = x.split()
        dim = list[2].split(",")
        dim[1] = dim[1].split(":")[0]
        name = list[0]
        a = int(dim[0])
        b = int(dim[1])
        size = list[3].split("x")
        x = int(size[0])
        y = int(size[1])
        flag = False
        for i in range(0, x):
            for j in range(0, y):
                if dict[i + a + 1][j + b + 1] == 1:
                    pass
                if dict[i + a + 1][j + b + 1] == 2:
                    flag = True
                else:
                    pass
        if not flag:
            print name


print func2()
