
import pandas as pd
from scripts import data_processing, modeling, segmentation
from scripts.reporting import generate_report


def cltv_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tüm CLTV sürecini tek fonksiyonda birleştirir.
    Args:
        df (pd.DataFrame): Ham müşteri verisi
    Returns:
        pd.DataFrame: CLTV ve segment sütunları eklenmiş veri
    """
    # Temel ön işlemler
    data_processing.create_total_columns(df)
    data_processing.convert_date_columns(df)
    
    # CLTV dataframe oluştur
    cltv_df = data_processing.create_cltv_dataframe(df)
    
    # Model fit ve tahmin
    bgf = modeling.fit_bgf_model(cltv_df)
    ggf = modeling.fit_ggf_model(cltv_df)
    modeling.calculate_cltv(bgf, ggf, cltv_df)
    
    # Segmentasyon
    segmentation.segment_customers(cltv_df)
    
    # Otomatik rapor
    generate_report(cltv_df, model_info={"BGF": str(bgf), "GGF": str(ggf)})
    
    return cltv_df




