import pandas as pd

from gold_analysis import (
    add_year_column,
    calculate_average_gold_price,
    get_high_gold_days,
)


def test_calculate_average_gold_price():
    sample = pd.DataFrame({"GLD": [100, 200, 300]})

    result = calculate_average_gold_price(sample)

    assert result == 200


def test_get_high_gold_days():
    sample = pd.DataFrame({"GLD": [100, 200, 300]})

    result = get_high_gold_days(sample)

    assert result["GLD"].tolist() == [300]


def test_add_year_column():
    sample = pd.DataFrame({"Date": ["2024-01-01", "2025-01-01"]})

    result = add_year_column(sample)

    assert result["Year"].tolist() == [2024, 2025]
