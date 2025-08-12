# test_visualization.py
import pandas as pd
from scripts import visualization

def test_plot_cltv_distribution(tmp_path):
    df = pd.DataFrame({'cltv': [1, 2, 3, 4, 5], 'exp_average_value': [1, 2, 3, 4, 5]})
    visualization.plot_cltv_distribution(df)

def test_mean_selling(tmp_path):
    df = pd.DataFrame({'exp_average_value': [1, 2, 3, 4, 5], 'cltv': [1, 2, 3, 4, 5]})
    visualization.mean_selling(df)
