# Module to calculate the hypotenuse of a
# right angled triangle

# Function to check input is float/integer
# Throw error if not

# Function to add to numbers together
# input: floats or int or list/arrays of ints/floats
def add_nums(a, b):
    """_summary_

    Args:
        a (float, int, array): _description_
        b (float, int, array): _description_

    Returns:
        float, int, array: The sum of a and b
    """
    sum_of_numbers = a + b
    return sum_of_numbers

# Function to calculate the square of a number
# input: floats or int or list/arrays of ints/floats
def square_number(a):
    square_number = a **2
    return square_number
# Function to calculate the square root of a number
# input: floats or int or list/arrays of ints/floats
def square_root(a):
    """_summary_

    Args:
        a (_type_): _description_

    Returns:
        _type_: _description_
    """
    sq_rt_num = a ** 0.5
    return sq_rt_num


# Function to calculate the hypotenuse using all the above
# a^2 + b^2 = c^2
# c = sqrt(a^2 + b^2)
# input: floats or int or list/arrays of ints/floats
def calc_hypot(opposite, adjacent):
    """Calculate the longest side of the hypotenuse of a R.A.T.
    
    Calculate the longest side of a right angled triangle using Pythagoras'

    Args:
        opposite (_type_): _description_
        adjacent (_type_): _description_

    Returns:
        _type_: _description_
    """
    opp_sqrd = square_number(opposite)
    opp_sqrd = square_number(adjacent)
    summed_nums = add_nums(opp_sqrd)
    hypotenuse = square_root
    return calc_hypot