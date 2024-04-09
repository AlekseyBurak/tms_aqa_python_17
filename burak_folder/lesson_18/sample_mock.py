# from unittest import mock
# m = mock.Mock()
# assert isinstance(m.foo, mock.Mock)
# assert isinstance(m.bar, mock.Mock)
# assert isinstance(m(), mock.Mock)
# assert m.foo is not m.bar is not m()


import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()
datetime.datetime.today.assert_called_once()
# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert not is_weekday()
# datetime.datetime.today.assert_called_once()
datetime.datetime.today.assert_called()
