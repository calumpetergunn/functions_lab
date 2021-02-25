def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

# def number_to_full_month_name(month):
#     import calendar
#     return calendar.month_name[month]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def number_to_full_month_name(number):
    number = number - 1
    return months[number]
# print(number_to_full_month_name(12))

def number_to_short_month_name(month):
    return number_to_full_month_name(month)[0:3]
# print(number_to_short_month_name(10))    

def volume_of_cube(length_of_side):
    return length_of_side ** 3
# print(volume_of_cube (3))

def string_reverse(str):
    string_reversed = ''
    index = len(str)
    while index > 0:
        string_reversed += str [index - 1]
        index = index - 1
    return string_reversed
# print (string_reverse("Scotland"))

# ALSO - much simpler
# def string_reverse(str):
#     return str[::-1]

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * (5.0/9.0)
    print(f"The value before rounding is {celcius}")

    return round(celcius, 2)
