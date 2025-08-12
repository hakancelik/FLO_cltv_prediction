
from lifetimes import BetaGeoFitter, GammaGammaFitter
import logging
from config import BGF_PARAMS, GGF_PARAMS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fit_bgf_model(cltv_df, params: dict = BGF_PARAMS) -> BetaGeoFitter:
    """
    BG/NBD modelini fit eder.
    Args:
        cltv_df (pd.DataFrame): CLTV veri çerçevesi.
        params (dict): Model parametreleri.
    Returns:
        BetaGeoFitter: Eğitilmiş model.
    """
    try:
        bgf = BetaGeoFitter(**params)
        bgf.fit(cltv_df['frequency'], cltv_df['recency_cltv_weekly'], cltv_df['T_weekly'])
        logging.info("BGF modeli başarıyla fit edildi.")
        return bgf
    except Exception as e:
        logging.error(f"BGF modeli fit edilirken hata oluştu: {e}")
        raise


def fit_ggf_model(cltv_df, params: dict = GGF_PARAMS) -> GammaGammaFitter:
    """
    Gamma-Gamma modelini fit eder.
    Args:
        cltv_df (pd.DataFrame): CLTV veri çerçevesi.
        params (dict): Model parametreleri.
    Returns:
        GammaGammaFitter: Eğitilmiş model.
    """
    try:
        ggf = GammaGammaFitter(**params)
        ggf.fit(cltv_df['frequency'], cltv_df['monetary_cltv_avg'])
        logging.info("GGF modeli başarıyla fit edildi.")
        return ggf
    except Exception as e:
        logging.error(f"GGF modeli fit edilirken hata oluştu: {e}")
        raise


def calculate_cltv(
    bgf: BetaGeoFitter,
    ggf: GammaGammaFitter,
    cltv_df,
    time: int = 6,
    freq: str = "W",
    discount_rate: float = 0.01
) -> None:
    """
    CLTV hesaplar ve veri çerçevesine ekler.
    Args:
        bgf (BetaGeoFitter): BG/NBD modeli.
        ggf (GammaGammaFitter): Gamma-Gamma modeli.
        cltv_df (pd.DataFrame): CLTV veri çerçevesi.
        time (int): Tahmin süresi.
        freq (str): Frekans.
        discount_rate (float): İskonto oranı.
    """
    try:
        cltv = ggf.customer_lifetime_value(
            bgf,
            cltv_df['frequency'],
            cltv_df['recency_cltv_weekly'],
            cltv_df['T_weekly'],
            cltv_df['monetary_cltv_avg'],
            time=time,
            freq=freq,
            discount_rate=discount_rate
        )
        cltv_df["cltv"] = cltv
        logging.info("CLTV başarıyla hesaplandı ve eklendi.")
    except Exception as e:
        logging.error(f"CLTV hesaplanırken hata oluştu: {e}")
        raise



