import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

REPORT_DIR = "report"
REPORT_PATH = os.path.join(REPORT_DIR, "report.md")

os.makedirs(REPORT_DIR, exist_ok=True)


def generate_report(df: pd.DataFrame, model_info: dict = None):
    """
    CLTV pipeline sonrası otomatik markdown raporu üretir.
    Args:
        df (pd.DataFrame): CLTV ve segment sütunları eklenmiş veri
        model_info (dict): Model parametreleri ve özetleri (opsiyonel)
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("# FLO CLTV Prediction Raporu\n\n")
        f.write(f"Oluşturulma: {now}\n\n")
        f.write("## Genel İstatistikler\n")
        f.write(df.describe().to_markdown() + "\n\n")
        f.write("## Segment Dağılımı\n")
        seg_counts = df['cltv_segment'].value_counts().sort_index()
        f.write(seg_counts.to_markdown() + "\n\n")
        f.write("## CLTV Dağılımı\n")
        plt.figure(figsize=(8, 4))
        sns.histplot(df['cltv'], bins=30, kde=True)
        img_path = os.path.join(REPORT_DIR, "cltv_dist.png")
        plt.savefig(img_path)
        plt.close()
        f.write(f"![CLTV Dağılımı]({img_path})\n\n")
        if model_info:
            f.write("## Model Bilgileri\n")
            for k, v in model_info.items():
                f.write(f"- **{k}**: {v}\n")
        f.write("\n---\nOtomatik oluşturulmuştur.")




