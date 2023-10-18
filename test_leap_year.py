from LeapYear import LeapYear


def leap_year():
    return LeapYear()


def test_is_year_divisible_by_4_and_not_100():
    assert leap_year().is_leap_year(2004) == True
    assert leap_year().is_leap_year(2020) == True
    assert leap_year().is_leap_year(2048) == True


def test_is_year_divisible_by_400():
    assert leap_year().is_leap_year(2400) == True
    assert leap_year().is_leap_year(2000) == True
    assert leap_year().is_leap_year(2800) == True


def test_is_year_not_divisible_by_4():
    assert leap_year().is_leap_year(2037) == False
    assert leap_year().is_leap_year(2047) == False
    assert leap_year().is_leap_year(2025) == False
    assert leap_year().is_leap_year(2049) == False


def test_is_year_divisible_by_100_and_not_400():
    assert leap_year().is_leap_year(1700) == False
    assert leap_year().is_leap_year(2900) == False
    assert leap_year().is_leap_year(2200) == False
    assert leap_year().is_leap_year(1900) == False



