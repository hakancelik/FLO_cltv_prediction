
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from config import SCREEN_PATH
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def plot_cltv_distribution(cltv_df) -> None:
    """
    CLTV dağılımını çizer ve kaydeder.
    Args:
        cltv_df (pd.DataFrame): CLTV veri çerçevesi.
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.histplot(cltv_df['cltv'], bins=50, kde=True)
        plt.title('CLTV Distribution')
        plt.xlabel('CLTV')
        plt.ylabel('Frequency')
        out_path = os.path.join(SCREEN_PATH, "cltv_distribution.png")
        plt.savefig(out_path)
        plt.close()
        logging.info(f"CLTV dağılım grafiği kaydedildi: {out_path}")
    except Exception as e:
        logging.error(f"CLTV dağılım grafiği çizilemedi: {e}")


def plot_cltv_segments(cltv_df) -> None:
    """
    Segmentlere göre CLTV dağılımını çizer ve kaydeder.
    Args:
        cltv_df (pd.DataFrame): CLTV veri çerçevesi.
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='cltv_segment', y='cltv', data=cltv_df)
        plt.title('CLTV Distribution by Segment')
        plt.xlabel('Segment')
        plt.ylabel('CLTV')
        out_path = os.path.join(SCREEN_PATH, "cltv_distribution_by_segment.png")
        plt.savefig(out_path)
        plt.close()
        logging.info(f"Segmentlere göre CLTV dağılım grafiği kaydedildi: {out_path}")
    except Exception as e:
        logging.error(f"Segmentlere göre CLTV dağılım grafiği çizilemedi: {e}")


def plot_cltv_over_time(cltv_df) -> None:
    """
    Zamanla CLTV değişimini çizer ve kaydeder.
    Args:
        cltv_df (pd.DataFrame): CLTV veri çerçevesi.
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='date', y='cltv', data=cltv_df)
        plt.title('CLTV Over Time')
        plt.xlabel('Date')
        plt.ylabel('CLTV')
        out_path = os.path.join(SCREEN_PATH, "cltv_over_time.png")
        plt.savefig(out_path)
        plt.close()
        logging.info(f"Zamanla CLTV değişim grafiği kaydedildi: {out_path}")
    except Exception as e:
        logging.error(f"Zamanla CLTV değişim grafiği çizilemedi: {e}")


def mean_selling(cltv_df) -> None:
    """
    Beklenen ortalama harcama değerinin dağılımını çizer ve kaydeder.
    Args:
        cltv_df (pd.DataFrame): CLTV veri çerçevesi.
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.histplot(cltv_df['exp_average_value'], bins=50, kde=True)
        plt.title('Expected Average Value Distribution')
        plt.xlabel('Expected Average Value')
        plt.ylabel('Frequency')
        out_path = os.path.join(SCREEN_PATH, "expected_average_value_distribution.png")
        plt.savefig(out_path)
        plt.close()
        logging.info(f"Beklenen ortalama harcama değeri grafiği kaydedildi: {out_path}")
    except Exception as e:
        logging.error(f"Beklenen ortalama harcama değeri grafiği çizilemedi: {e}")



