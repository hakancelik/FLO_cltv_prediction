# config.py

# Genel ayarlar ve sabitler burada tutulur.

DATA_PATH = "data/flo_data_20k.csv"
REPORT_PATH = "report/report.md"
SCREEN_PATH = "screen/"
RANDOM_STATE = 42

# Model parametreleri
BGF_PARAMS = {
    "penalizer_coef": 0.01
}

GGF_PARAMS = {
    "penalizer_coef": 0.01
}

# Segmentasyon sınırları
SEGMENT_LABELS = ["A", "B", "C"]
SEGMENT_BINS = [0, 0.25, 0.75, 1.0]
