# test_segmentation.py
import pandas as pd
from scripts import segmentation

def test_segment_customers():
    df = pd.DataFrame({
        'cltv': [10, 20, 30, 40, 50, 60, 70, 80]
    })
    segmentation.segment_customers(df)
    assert 'cltv_segment' in df.columns
    assert df['cltv_segment'].notnull().all()
