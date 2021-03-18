"""
Fantastic functions for fun frivolity with Python
"""
ANIMAL = 'wombat'

def spam():
    """
    Canned fatty meat.

    :return: None
    """
    x = 5
    print("Hello from spam()")


def _ham():  #  "private"
    """
    Helper function for toast

    :return:
    """
    print("   and _ham()")


def toast():
    """
    Delicious roasted slices of bread.

    :return: None
    """
    print("Hello from toast()")
    _ham()

# this
# is
# a
# comment

def wombat(a, b, c):
    """
    A furry marsupial that lives in Oz

    :param a: widget count (int)
    :param b: fear factor
    :param c: repeat count
    :return: percentage of stuff
    """
    print("I am a wombat")