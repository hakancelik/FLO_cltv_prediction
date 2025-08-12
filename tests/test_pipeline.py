# test_pipeline.py
import pandas as pd
from scripts.pipeline import cltv_pipeline

def test_cltv_pipeline():
    df = pd.DataFrame({
        'order_num_total_ever_online': [1, 2],
        'order_num_total_ever_offline': [3, 4],
        'customer_value_total_ever_offline': [10, 20],
        'customer_value_total_ever_online': [30, 40],
        'recency_cltv_weekly': [1, 2],
        'T_weekly': [2, 3],
        'frequency': [1, 2],
        'monetary_cltv_avg': [10, 20],
        'first_order_date': ['2021-01-01', '2021-02-01'],
        'last_order_date': ['2021-06-01', '2021-07-01']
    })
    result = cltv_pipeline(df)
    assert 'cltv' in result.columns
    assert 'cltv_segment' in result.columns
