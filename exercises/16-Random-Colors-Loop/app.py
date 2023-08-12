import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():
    example_color = get_color(1)
    students_array = []
    #your loop here


print(get_allStudentColors())

import random

def get_color(number):
    colors = ["red", "yellow", "blue", "green"]
    if number >= 0 and number < 4:
        return colors[number]
    else:
        return "black"

def get_allStudentColors():
    student_colors = []
    for _ in range(10):
        random_number = random.randint(0, 3)
        color = get_color(random_number)
        student_colors.append(color)
    return student_colors

# Llamamos a la función y mostramos el resultado
colors_assigned = get_allStudentColors()
print(colors_assigned)
