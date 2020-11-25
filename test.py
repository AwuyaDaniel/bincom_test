import re
# importing pandas as pd
import numpy
import psycopg2
import random
import statistics

file_name = 'python_class_test.html'

color_1 = []
color_num = []
colors = {}


# Connecting to posgress database
connection = psycopg2.connect(
    host='localhost',
    database='todolist',
    user='postgres',
    password='root',
)
print("Connection was successful")

with open(file_name, 'r') as chosen_colors:
    # read file
    file = chosen_colors.readlines()
    # looping through each line in the test html file
    for color in file:
        color.rstrip()
        color_names = re.findall("<td>\D\D*.</td>", color)
        # print(color_names)
        """looping through each line and removing the tread
            tags displaying only the name by searching
          for names with capital letter and putting out the days or the week"""
        for i in color_names:
            color_name = re.findall("[A-Z][A-Z]*", i)
            for color_single in color_name:
                if color_single != "MONDAY" and color_single != "TUESDAY" and color_single != "WEDNESDAY"\
                        and color_single != 'THURSDAY' and color_single != 'FRIDAY':

                    color_1.append(color_single)
    # Looping through the list color and add the color and count in a dictionary
    for i in color_1:
        colors[i] = color_1.count(i)

    for i, k in colors.items():
        color_num.append(k)

    """Question 1"""
    # Getting the mean
    def mean_numbers():
        mean = numpy.mean(color_num)
        for i, k in colors.items():
            if k > mean:
                if k % 2 == 0:
                    if k % 3 == 0:
                        print('The mean color is ', i)


    """Question 2"""
    # Getting color most worn
    def most_worn():
        for i, k in colors.items():
            most = max(color_num)
            if k == most:
                print("the color most worn is ", i)

    """Question 3"""
    # Getting the median with numpy
    def meidian_num():
        median = numpy.median(color_num)
        median2 = round(median)
        # matching the median and printing it out
        for i, k in colors.items():
            if k == median2:
                print("The median color is ", i)

    """Question 4"""
    def vari():
        # getting the variance with python statistics
        p = statistics.variance(color_num)
        print(p)

    """Question 5"""
    def probability():
        pro = sum(color_num)
        # calculating the probability for only red
        for i, k in colors.items():
            percent = k / pro
            if i == 'RED':
                print(i, percent)
        # calculating the probability for all colors
        # for i, k in colors.items():
        #     percent = k / pro
        #     prcent = k / pro
        #     print(i, percent)

    """Question 6"""
    def save_colors():
        # Create cursor
        cur = connection.cursor()
        # looping through the dictionary and adding to the database one by one
        for i, k in colors:
            cur.execute("INSERT INTO public.crud (frequency, color) VALUES (%s, %s,)",
                        (k, i))
        print("Information has been added\n")
        connection.commit()


"""Question 7"""
def recursive():
    try:
        numbers = [1, 5, 6, 9, 8, 7, 0]
        number = input("Please enter a number: ")
        number = int(number)
        if number in numbers:
            print(str(number) + " is in list of numbers")
        else:
            print(str(number) + " is not in list of numbers")
    except ValueError:
        print("Not an Integer")


"""Question 8"""
def random_numbers():
    numbers = []
    # printing a list of 4 random numbers
    num = list(map(random.randrange, [2]*4))
    # converting dem to a string and adding dem to a new list
    p = str(num)
    for i in num:
        numbers.append(str(i))

    # joining the str in the new list together and printing it in decimal(base 10)
    s = ''.join(numbers)
    r = '0b' + s
    dec = int(r, 0)
    print(dec)


"""Question 9"""
def fib(n):
    a = 0
    b = 1

    # checking if range is 1 or not
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

    # if range is more than two
    for i in range(2, n):
        # adding the first two values and then swapping it
        # and adding the new one to the previous(formal) new one
        c = a + b
        a = b
        b = c
        print(a + b)


vari()
mean_numbers()
most_worn()
