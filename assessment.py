#TO DO LIST: Cheat sheet for SublimeText keyboard shortcuts (beginning of line)

#Declare global sales tax of 5%
tax = 0.05
#assume function takes input from prior survey to get properly formatted state abbreviation , cost of item. Assume it's up to me to adjust national tax for local variation.
def calculate_total_cost(cost, state, tax = tax):
    """From the on-shelf cost of an item and local tax rate, return total cost including sales tax.
    """
    #In case of typos
    state.lower()
    if state == 'ca':
        tax = 0.07
    total_cost = cost * (tax+1)
    return total_cost

#####################################################################
def is_berry(fruit):
    """Takes in a string and returns a boolean
    Tests fruit to determine if it is a berry.
    """
    fruit.lower()
#sets are for searching and we may want to add more berries later. Sorting is irrelevant for this use.
    berries = {'strawberry', 'cherry', 'blueberry'}
    if fruit in berries:
        return True
#Asked someone whether I really needed an "else:" here and was told that failing if will return None and None and False are equivalent. Are they really the same or just often treated (by code) the same?

#TO DO LIST: HB Email Filter/Folder

def shipping_cost(fruit):
    """Takes a string, and returns an integer
    Returns the shipping cost for a fruit, on the basis of whether or not it is a berry
    """
    if is_berry(fruit):
        return 0
    else:
        return 5

def is_hometown(town):
    """Takes a string and returns Boolean
    Tests user's hometown to see if it's the same as the programmer's
    """
    town.lower
    if town == 'malibu':
        return True

def full_name(first_name, last_name):
    """Takes two strings and returns one string
    Takes first and last names and concatenates them to make the user's full name
    """
    #Clould also use .format, but seems like overkill here
    full_name = first_name + " " + last_name
    return full_name

def hometown_greeting (town, first_name, last_name):
    """Takes three strings and returns nothing
    Prints a greeting statement incorporating the user's name and hometown
    """
    home_town = home_town(town) #True or False
    name = full_name(first_name, last_name)
    if home_town:
        print "Hi, {}, we're from the same place!".format(name)
    else:
        print "Hi, {}, where are you from?".format(name)
        #Except, that we know where they're from, because they told us.

        ##TO DO LIST: Fluency in %s notation
#####################################################################
def increment(x=1):
    """Takes two numbers and returns one number
    Outer function increment() takes a single number (default is 1. Inner function add() takes a single number which it adds to the parameter from the outer function.
    """
    def add(y):
        return x+y
    return add

addfive = increment(5)(5)
addfive = increment(5)(20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def append_input_to_list(number_list, new_num):
    """Takes a list of numbers and a number, and returns a list
    Appends new_num to number_list
    """
    number_list.append(new_num)
    return number_list


#####################################################################