
import pandas as pd
import logging
from config import SEGMENT_LABELS, SEGMENT_BINS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def segment_customers(cltv_df: pd.DataFrame, labels=SEGMENT_LABELS, bins=SEGMENT_BINS) -> None:
    """
    CLTV değerine göre müşterileri segmentlere ayırır.
    Args:
        cltv_df (pd.DataFrame): CLTV veri çerçevesi.
        labels (list): Segment etiketleri.
        bins (list): Segment sınırları (0-1 arası quantile değerleri).
    """
    try:
        cltv_df['cltv_segment'] = pd.qcut(
            cltv_df['cltv'].rank(method='first') / len(cltv_df), 
            q=bins, 
            labels=labels
        )
        logging.info(f"Müşteriler segmentlere ayrıldı: {labels}")
    except Exception as e:
        logging.error(f"Segmentasyon sırasında hata oluştu: {e}")
        raise



