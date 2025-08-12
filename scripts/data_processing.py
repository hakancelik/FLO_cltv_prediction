
import pandas as pd
import logging
from typing import List
from config import DATA_PATH

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_data(file_path: str = DATA_PATH) -> pd.DataFrame:
    """
    Verilen dosya yolundan veriyi yükler.
    Args:
        file_path (str): CSV dosya yolu.
    Returns:
        pd.DataFrame: Yüklenen veri.
    """
    try:
        df_ = pd.read_csv(file_path)
        df = df_.copy()
        logging.info(f"Veri başarıyla yüklendi: {file_path}")
        return df
    except Exception as e:
        logging.error(f"Veri yüklenirken hata oluştu: {e}")
        raise


def process_outliers(dataframe: pd.DataFrame, columns: List[str]) -> None:
    """
    Belirtilen sütunlardaki aykırı değerleri eşiklerle sınırlar.
    Args:
        dataframe (pd.DataFrame): Veri çerçevesi.
        columns (List[str]): Aykırı değer kontrolü yapılacak sütunlar.
    """
    def outlier_thresholds(dataframe: pd.DataFrame, variable: str):
        quartile1 = dataframe[variable].quantile(0.01)
        quartile3 = dataframe[variable].quantile(0.99)
        interquantile_range = quartile3 - quartile1
        up_limit = quartile3 + 1.5 * interquantile_range
        low_limit = quartile1 - 1.5 * interquantile_range
        return low_limit, up_limit

    def replace_with_thresholds(dataframe: pd.DataFrame, variable: str):
        # Remove outliers based on quantiles
        low_limit, up_limit = outlier_thresholds(dataframe, variable)
        dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
        dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

    for col in columns:
        replace_with_thresholds(dataframe, col)
    logging.info(f"Aykırı değerler işlendi: {columns}")


def create_total_columns(dataframe: pd.DataFrame) -> None:
    """
    Toplam sipariş ve toplam müşteri değeri sütunlarını oluşturur.
    Args:
        dataframe (pd.DataFrame): Veri çerçevesi.
    """
    dataframe["order_num_total"] = (
        dataframe["order_num_total_ever_online"] + 
        dataframe["order_num_total_ever_offline"]
    )
    dataframe["customer_value_total"] = (
        dataframe["customer_value_total_ever_offline"] + 
        dataframe["customer_value_total_ever_online"]
    )
    logging.info("Toplam sütunlar oluşturuldu.")


def convert_date_columns(dataframe: pd.DataFrame) -> None:
    """
    Tarih içeren sütunları datetime tipine çevirir.
    Args:
        dataframe (pd.DataFrame): Veri çerçevesi.
    """
    date_columns = dataframe.columns[dataframe.columns.str.contains("date")]
    dataframe[date_columns] = dataframe[date_columns].apply(pd.to_datetime)
    logging.info(f"Tarih sütunları dönüştürüldü: {list(date_columns)}")



