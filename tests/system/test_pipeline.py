from pathlib import Path

import pandas as pd

from gold_analysis import (
    add_year_column,
    calculate_average_gold_price,
    get_high_gold_days,
)


def test_complete_analysis_workflow():
    data_path = Path(__file__).parents[2] / "gold_data_2015_25.csv"
    data = pd.read_csv(data_path)

    data = add_year_column(data)
    average = calculate_average_gold_price(data)
    high_gold_days = get_high_gold_days(data)

    assert "Year" in data.columns
    assert round(average, 2) == 158.60
    assert len(high_gold_days) == 1299
