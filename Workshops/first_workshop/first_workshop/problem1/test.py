def is_leap_year(year):
    """
    Return True if leap year and False otherwise
    """
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year%100 == 0:
            return False
        return True
    return False


print( is_leap_year(1997))