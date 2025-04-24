from data_processing import load_data, process_outliers, create_total_columns, convert_date_columns
from modeling import fit_bgf_model, fit_ggf_model, calculate_cltv
from segmentation import segment_customers
from visualization import plot_cltv_distribution

# Load and process data
df = load_data("data/flo_data_20k.csv")
process_outliers(df, ["order_num_total_ever_online", "order_num_total_ever_offline", 
                      "customer_value_total_ever_offline", "customer_value_total_ever_online"])
create_total_columns(df)
convert_date_columns(df)

# Modeling
cltv_df = df[["master_id", "last_order_date", "first_order_date", "order_num_total", "customer_value_total"]].copy()
cltv_df["recency_cltv_weekly"] = ((df["last_order_date"] - df["first_order_date"]).dt.days / 7)
cltv_df["T_weekly"] = ((pd.Timestamp("2021-06-01") - df["first_order_date"]).dt.days / 7)
cltv_df["frequency"] = df["order_num_total"]
cltv_df["monetary_cltv_avg"] = df["customer_value_total"] / df["order_num_total"]

bgf = fit_bgf_model(cltv_df)
ggf = fit_ggf_model(cltv_df)
calculate_cltv(bgf, ggf, cltv_df)

# Segmentation
segment_customers(cltv_df)

# Visualization
plot_cltv_distribution(cltv_df)