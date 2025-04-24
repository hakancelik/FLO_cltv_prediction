from lifetimes import BetaGeoFitter, GammaGammaFitter

def fit_bgf_model(cltv_df):
    bgf = BetaGeoFitter(penalizer_coef=0.001)
    bgf.fit(cltv_df['frequency'], cltv_df['recency_cltv_weekly'], cltv_df['T_weekly'])
    return bgf

def fit_ggf_model(cltv_df):
    ggf = GammaGammaFitter(penalizer_coef=0.01)
    ggf.fit(cltv_df['frequency'], cltv_df['monetary_cltv_avg'])
    return ggf

def calculate_cltv(bgf, ggf, cltv_df, time=6, freq="W", discount_rate=0.01):
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