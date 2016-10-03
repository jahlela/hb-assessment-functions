# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 


def tax_calculator(state, price, tax = .05):
    """
    Takes three inputs: A string state abbreviation, the cost of the item, 
    and a default tax of .05. The tax can be changed by the user. 
    Output: Total cost of item, including tax, in currency string format.

    Note: if the state is CA, tax is increased to .07.

    Ex. 
    >>> tax_calculator("NY", 1450.2) 
    $1,522.71
    >>> tax_calculator("CA", 33)
    $35.31
    >>> tax_calculator("ME", 229.50, .06)
    $243.27

    """

    #If state is CA, tax is .07
    if state == "CA":
        tax = .07

    #Calculate price as multiplication by 1 plus tax. 
    total_price = price * (tax + 1)

    #Format total for currency
    formatted_total = '${:,.2f}'.format(total_price)

    return formatted_total

#Example calls
print tax_calculator("NY", 1450.2)
print tax_calculator("CA", 33)
print tax_calculator("ME", 229.50, .06)


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def is_berry(fruit_name):
    """
    Returns a boolean, based on whether the input string is "strawberry", 
    "cherry", or "blackberry"
    """

    # check if input string is a berry. Return True if yes, False if no.
    if fruit_name == "strawberry":
        return True
    elif fruit_name == "cherry": 
        return True
    elif fruit_name == "blackberry":
        return True
    else:
        return False

print is_berry('cherry')
print is_berry('plum')

def shipping_cost(fruit_name):
    """
    Returns either 0 or 5, based on whether the input string is a berry.
    Uses the is_berry function to determine the boolean.
    """

    #calls is_berry function using the input string 
    fruit_bool = is_berry(fruit_name)

    if fruit_bool:
        return 0
    else:
        return 5

print shipping_cost('cherry')
print shipping_cost('plum')


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.


def is_hometown(town):
    """
    Takes a town name as a string and evaluates to `True` if it is Chico, 
    and `False` otherwise.
    """

    # Check if town is "Chico"
    if town == "Chico":
        return True
    else:
        return False

print is_hometown("Chico")
print is_hometown("Massillon")


def full_name(first_name, last_name):
    """
    Takes a first and last name as arguments as strings and returns the 
    concatenation of the two names in one string.
    """

    #make string with full name using first and last name
    return first_name + " " + last_name

print full_name("Jahlela", "Hasle")


def hometown_greeting(first_name, last_name, town):
    """
    Returns a string that greets the user with their first and last name 
    by calling full_name with both names. It also gives variable reponses 
    based on whether the user is from the same hometown. This is determined
    by calling the is_hometown function.
    """

    #Calls full_name with first and last name, and assigns it to user_full_name
    user_full_name = full_name(first_name, last_name)


    if is_hometown(town):
        print "Hi %s, we're from the same place!" % (user_full_name)
    else:
        print "Hi %s, where are you from?" % (user_full_name)

print hometown_greeting("Ella", "Fitzgerald", "Newport News") 
print hometown_greeting("Jahlela", "Hasle", "Chico")

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.


#I am very confused about the second part of these instructions. 

def increment(x = 1):
    """ 
    I'm not sure what this is supposed to return. It has a nested function that 
    adds the x input with a y input given within this function.
    """

    def add(y):
        """ 
        Returns the sum of x and y.
        """

        return x + y

    # Where am I supposed to be calling this? What should I do with the output?
    return add(5)
    return add(20)

#call incrememnt with 5 and assign it to addfive
addfive = increment(5)



# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def list_adder(list, number):
    """
    Appends a number to a list of numbers, and returns the list. 
    """

    #return the list with the number appended
    return list + [number]


#####################################################################




