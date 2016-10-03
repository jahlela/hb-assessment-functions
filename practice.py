"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

def full_title(name, title = "Engineer"):
    """
    Returns string with title and name. Title defaults to "Engineer"
    """

    return title + " " + name


# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


def write_letter(name, title, sender): 
    """
    Takes three strings as arguments to return small greeting letter.
    """
    full_name = full_title(name, title)

    print "Dear %s, I think you are amazing! Sincerely, %s" % (full_name, sender)

################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world(): 
    """ 
    Prints 'Hello World' 
    """

    print 'Hello World'


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name): 
    """ 
    Prints "Hi" and the input string
    """
    print "Hi", name

# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.

def print_product(int_1, int_2): 
    """ 
    Takes two integers and returns their product
    """

    print int_1 * int_2


# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times

def repeat_string(input_string, n): 
    """ 
    Repeats a string n times
    """

    print input_string * n

# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".

def print_sign(integer): 
    """ 
    Prints whether the input integer is lower, equal to, or higher than zero
    """

    if integer < 0:
        print "Lower than 0"
    elif integer == 0:
        print "Zero"
    else:
        print "Higher than 0"

# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def is_divisible_by_three(integer): 
    """ 
    Returns a boolean for whether an integer is divisible by 3
    """

    return integer % 3 == 0

# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.

def num_spaces(sentence): 
    """ 
    Returns the number of spaces in a string
    """

    space_count = 0
    
    for character in sentence:
        if character == " ": 
            space_count += 1

    return space_count

# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_meal_price(price, tip = .15): 
    """ 
    Returns the total for a meal after tip. Tip parameter is optional and defaults
    to 15%.
    """

    return price * (tip + 1)
    
# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.

def sign_and_parity(integer): 
    """ 
    Returns the parity and sign of an integer as strings in a list:
    [parity, sign]
    """

    sign = "Positive"
    parity = "Even"

    if integer < 0:
        sign = "Negative"

    if integer % 2 == 1:
        parity = "Odd"

    return [parity, sign]

#Testing sign_and_parity function
test_integer = -5
result = sign_and_parity(test_integer)

print "Test integer", test_integer
print "Parity:", result[0]
print "Sign:", result[1]

################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
