def valid_date(date):
    
    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
            return False
        if month in [4,6,9,11] and day < 1 or day > 30:
            return False
        if month == 2 and day < 1 or day > 29:
            return False
    except:
        return False

    return True



def test():
        assert valid_date("01-15-2020") == True
    assert valid_date("02-29-2020") == True
    assert valid_date("02-30-2020") == False
    assert valid_date("04-31-2021") == False
    assert valid_date("13-01-2020") == False
    assert valid_date("00-10-2020") == False
    assert valid_date("11-31-2020") == False
    assert valid_date("11-00-2020") == False
    assert valid_date("12-25-2020") == True
    assert valid_date("07-04-1776") == True
    assert valid_date("02-28-2019") == True
    assert valid_date("02-29-2019") == False
    assert valid_date("not-a-date") == False
    assert valid_date("04-0-2040") == False  # This test case will detect the fault
