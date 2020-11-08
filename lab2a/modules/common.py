import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def parne_neparne(T):
    if T == True:
        i = 0
        while i <= 100:
            print(i)
            i += 2
    else:
        i = 1
        while i <= 100:
            print(i)
            i += 2
