import streamlit as st
import pandas as pd
from scripts.pipeline import cltv_pipeline

st.set_page_config(page_title="FLO CLTV Dashboard", layout="wide")
st.title("FLO CLTV Prediction Dashboard")

uploaded_file = st.file_uploader("Bir müşteri CSV dosyası yükleyin", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    result_df = cltv_pipeline(df)
    st.success("CLTV ve segmentasyon başarıyla hesaplandı!")
    st.dataframe(result_df[["cltv", "cltv_segment"]].head(20))

    st.subheader("Segment Dağılımı")
    st.bar_chart(result_df["cltv_segment"].value_counts())

    st.subheader("CLTV Dağılımı")
    st.histogram(result_df["cltv"], bins=30)

    st.download_button(
        label="Sonuçları CSV olarak indir",
        data=result_df.to_csv(index=False).encode("utf-8"),
        file_name="cltv_results.csv",
        mime="text/csv"
    )
else:
    st.info("Başlamak için bir CSV dosyası yükleyin.")
