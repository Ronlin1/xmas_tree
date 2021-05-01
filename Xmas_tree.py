# Program to print x-mas tree using for loops

# Error Handling so as the program does not break explicitly
while True: # keep the loop running until we get the correct input unless otherwise; break
    try:
        rows = int(input('Enter the number of rows: '))
        break
    except ValueError:
        print('Please enter an integer!')

# Our triangle as tree lives {function}
def triangle(n):
    """
    This function forms a triangle that  will help act as tree lives
    :param n: n is an integer for rows to be used
    :return: it returns no space ie ""
    """
    for i in range(n):
        # for catering the decreasing space as the triangle is formed
        for j in range(n-i):
            print(' ', end=' ')
        # catering for stars formation as the increase as space decreases
        for k in range(2*i + 1):
            print("*", end=" ")
        print()
    return ""

# Every tree has a trunk where everything get attached to:
def trunk(n):
    """
    This Trunk function takes input as rows in iteger
    :param n: n--> rows input -> integer
    :return: Nothing is returned
    """
    for i in range(n):
        # for loop to cater for the spaces
        for j in range(n-1):
            print(' ', end=' ')
        # print stars inside the first loop counter
        print("****")
    return ""


# the roots of the tree
def base(n):
    """
    This function takes input an integer  to be used in range function of the loops
    :param n: --> an integer of number of rows
    :return: Nothing is returned
    """
    # reduce the base since we want more columns than rows
    for i in range(n-8):
        for j in range(n-4):
            print(' ', end=' ')
        print('********'*2)
    return ""


# Calling our Tree Functions together to form a single tree
print(triangle(rows), end='')
print(triangle(rows), end="")
print(trunk(rows), end="")
print(triangle(rows), end='')
print(triangle(rows), end='')
print(triangle(rows), end='')
print(trunk(rows), end='')
print(trunk(rows), end='')
print(base(rows))


# hook me up if you fail to understand any of this or if this code does not run on your machine!

