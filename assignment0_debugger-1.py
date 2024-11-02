# Name: Derek Greene
# OSU Email: greenede@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 0: Debugger Submission
# Due Date: 10/7/2024
# Description: Program counts number of items in list and prints value.

# Please enter your name, favorite color, favorite hobby, and hometown in the list
my_list = ['Derek', 'Grey', 'Hiking', 'Salt Lake City']

def my_info(my_list):
    """ A function that passes a list of my information """
    count = 0
    for value in my_list:
        count += 1
    return count


if __name__ == '__main__':
    print(my_info(my_list))

