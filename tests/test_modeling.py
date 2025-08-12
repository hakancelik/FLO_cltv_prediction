# test_modeling.py
import pytest
import pandas as pd
from scripts import modeling

def test_fit_bgf_model():
    df = pd.DataFrame({
        'frequency': [1, 2, 3],
        'recency_cltv_weekly': [1, 2, 3],
        'T_weekly': [2, 3, 4],
        'monetary_cltv_avg': [10, 20, 30]
    })
    bgf = modeling.fit_bgf_model(df)
    assert hasattr(bgf, 'fit')

def test_fit_ggf_model():
    df = pd.DataFrame({
        'frequency': [1, 2, 3],
        'monetary_cltv_avg': [10, 20, 30]
    })
    ggf = modeling.fit_ggf_model(df)
    assert hasattr(ggf, 'fit')
