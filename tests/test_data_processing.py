# test_data_processing.py
import pytest
import pandas as pd
from scripts import data_processing

def test_load_data():
    df = data_processing.load_data()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_create_total_columns():
    df = pd.DataFrame({
        'order_num_total_ever_online': [1, 2],
        'order_num_total_ever_offline': [3, 4],
        'customer_value_total_ever_offline': [10, 20],
        'customer_value_total_ever_online': [30, 40]
    })
    data_processing.create_total_columns(df)
    assert 'order_num_total' in df.columns
    assert 'customer_value_total' in df.columns
    assert df['order_num_total'].iloc[0] == 4
    assert df['customer_value_total'].iloc[1] == 60
