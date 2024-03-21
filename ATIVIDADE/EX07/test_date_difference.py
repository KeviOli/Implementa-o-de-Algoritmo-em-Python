# test_date_difference.py
import pytest
from date_difference import calculate_date_difference

def test_calculate_date_difference():
    start_date = "2023-01-01 00:00:00"
    end_date = "2023-01-02 12:30:00"
    result = calculate_date_difference(start_date, end_date)
    assert result["days"] == 1
    assert result["months"] == 0
    assert result["years"] == 0
    assert result["hours"] == 12
    assert result["minutes"] == 30

    start_date = "2023-01-01 00:00:00"
    end_date = "2023-02-01 12:00:00"
    result = calculate_date_difference(start_date, end_date)
    assert result["days"] == 31
    assert result["months"] == 1
    assert result["years"] == 0
    assert result["hours"] == 12
    assert result["minutes"] == 0

    start_date = "2023-01-01 00:00:00"
    end_date = "2024-01-01 00:00:00"
    result = calculate_date_difference(start_date, end_date)
    assert result["days"] == 365
    assert result["months"] == 0
    assert result["years"] == 1
    assert result["hours"] == 0
    assert result["minutes"] == 0
