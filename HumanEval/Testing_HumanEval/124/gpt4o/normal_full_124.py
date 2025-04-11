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
    assert valid_date("02-29-2019") == True
    assert valid_date("not-a-date") == False
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
    assert valid_date("02-29-2019") == True
    assert valid_date("not-a-date") == False
    assert valid_date("02-0-2020") == False  # New test case to check for day 0 in February
    assert valid_date("06/04/2020") == False  # New test case to check incorrect format

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
    assert valid_date("02-29-2019") == True
    assert valid_date("not-a-date") == False
    assert valid_date("06/04/2020") == False  # Added test case for invalid date format

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
    assert valid_date("02-29-2019") == False  # Incorrect expected result fixed from True to False
    assert valid_date("not-a-date") == False
    assert valid_date("06-04-2020") == True  # Additional test case to detect the fault
    assert valid_date("06/04/2020") == False  # Additional test case to detect the fault

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
    assert valid_date("06/04/2020") == False
    assert valid_date("15-01-2012") == False
    assert valid_date("04-0-2040") == False

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
    assert valid_date("02-29-2019") == True
    assert valid_date("not-a-date") == False
    assert valid_date("15-01-2012") == False
    assert valid_date("06/04/2020") == False
    assert valid_date("04-0-2040") == False

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
    assert valid_date("06-04/2020") == False

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
    assert valid_date("02-29-2019") == True
    assert valid_date("not-a-date") == False
    assert valid_date("06/04/2020") == False  # Added test case to catch fault

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
    assert valid_date("02-29-2019") == True
    assert valid_date("not-a-date") == False
    assert valid_date("03-00-2000") == False  # New test case to catch the fault

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
    assert valid_date("06/04/2020") == False  # New test case to catch the fault

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
    assert valid_date("02-29-2019") == True
    assert valid_date("not-a-date") == False
    assert valid_date("06/04/2020") == False

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
    assert valid_date("02-29-2019") == False  # Corrected based on leap year rule
    assert valid_date("not-a-date") == False
    assert valid_date("15-01-2012") == False  # New test case for invalid month format
    assert valid_date("04-0-2040") == False   # New test case for invalid day format
    assert valid_date("06-04-2020") == True   # New test case for valid date format
    assert valid_date("06/04/2020") == False  # New test case for invalid date separator

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
    assert valid_date("02-29-2019") == True
    assert valid_date("not-a-date") == False
    assert valid_date("03-11-2000") == True
    assert valid_date("15-01-2012") == False
    assert valid_date("04-0-2040") == False
    assert valid_date("06-04-2020") == True
    assert valid_date("06/04/2020") == False

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
    assert valid_date("04-0-2020") == False

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
    assert valid_date("04-0-2040") == False  # new test case to detect the fault

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
    assert valid_date("06/04/2020") == False  # New test case to detect invalid format

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
    assert valid_date("02-29-2019") == False  # Corrected the expected result
    assert valid_date("not-a-date") == False
    assert valid_date("06/04/2020") == False  # New test case to check for wrong format
    assert valid_date("04-0-2040") == False  # New test case for invalid day

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
    assert valid_date("02-29-2019") == False  # Corrected this test case
    assert valid_date("not-a-date") == False
    assert valid_date("06/04/2020") == False  # New test case
    assert valid_date("04-0-2040") == False  # New test case

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
    assert valid_date("06/04/2020") == False

    assert valid_date("15-01-2012") == False  # Invalid month
    assert valid_date("04-0-2040") == False   # Invalid day
    assert valid_date("06-04-2020") == True   # Valid date
    assert valid_date("06/04/2020") == False  # Invalid format
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
    assert valid_date("02-29-2019") == False  # Should be False for non-leap year
    assert valid_date("not-a-date") == False

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
    assert valid_date("06/04/2020") == False # New test case to test invalid format
    assert valid_date("06-0-2040") == False # New test case to test day 0

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
    assert valid_date("06/04/2020") == False

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
    assert valid_date("02-29-2019") == False # Updated from True to False
    assert valid_date("not-a-date") == False
    assert valid_date("06/04/2020") == False # New test case to check the format

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
    assert valid_date("02-29-2019") == True
    assert valid_date("not-a-date") == False
    assert valid_date("02-31-2020") == False  # New test case to catch the fault

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
    assert valid_date("02-29-2019") == True
    assert valid_date("not-a-date") == False
    assert valid_date("06-04-2020") == True  # Added this test to cover the format issue
    assert valid_date("06/04/2020") == False # Added this test to cover the format issue

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
    assert valid_date("04-0-2040") == False

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
    assert valid_date("15-01-2012") == False  # test case to detect the fault
    assert valid_date("04-0-2040") == False  # test case to detect the fault
    assert valid_date("06/04/2020") == False  # test case to detect the fault

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
    assert valid_date("02-29-2019") == True
    assert valid_date("not-a-date") == False
    assert valid_date("02-00-2020") == False  # February 0 should be invalid

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
    assert valid_date("15-01-2012") == False  # New test case to check format
    assert valid_date("06/04/2020") == False  # New test case to check format

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
    assert valid_date("") == False  # Test for an empty string

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
    assert valid_date("02-29-2021") == False  # Adding a test case for a non-leap year date

