def task15():
    """
    Function that accepts a comma separated sequence of words as input and prints the words in a comma-separated
    sequence after sorting them alphabetically.

    Input: string
    Output: string
    """
    pass


def task16():
    """
    Function that compute the frequency of the words from the input. The output should output after sorting the key
    alphanumerically.
    Input: none
    Output: word -> count for every word in separated lines
    """
    pass


def task17():
    """
    Function that take sentence with words and numbers and calculate the number of letters and digits
    Input: sentence
    Output: dictionary (e.g. {"DIGITS": 3, "LETTERS":65})
    """
    pass


def task18():
    """
    Function that take sentence with words and numbers and calculate the number upper case letters and lower case letters
    
    Input: sentence
    Output: dictionary (e.g. {"UPPER": 3, "LOWER":65})
    """
    pass


def task19():
    """
    Function that take sentence with words and numbers and calculate the number upper case and lower case letters

    Input: sentence
    Output: dictionary (e.g. {"UPPER": 3, "LOWER":65})
    """
    pass


def task20():
    """
    Function that square each odd number in a list
    Use filer, labmda and map.

    Input: sentence with numbers that are comma separated (e.g. 5,6,7,8)
    Output: sentence with numbers (e.g. 25,49)
    """
    pass


def task21():
    """
    Function that computes the net amount of a bank account based a transaction log. The transaction log format is shown as following:
    M 100
    W 200
    for M-more and L-less

    Input: Log
    e.g.
    M 400
    M 300
    L 100

    Output: number (e.g. 600)
    """
    pass


def print_result(function, *args):
    print(function.__name__)
    print("Arguments:")
    for arg in args:
        print(arg)
    result = function(*args)
    if type(result) == tuple:
        result1, result2 = function(*args)
        print(f"Result 1: {result1}")
        print(f"Type of result: {type(result1)}")
        print(f"Result 2: {result2}")
        print(f"Type of result: {type(result2)}")
        print("\n")
    else:
        print(f"Result: {result}")
        print(f"Type of result: {type(result)}")
        print("\n")


if __name__ == '__main__':
    #task1
    slowa = "ala,ma,kota"
    print_result(task15, slowa)
