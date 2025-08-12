
from fastapi import FastAPI, UploadFile, File
import pandas as pd
from scripts.pipeline import cltv_pipeline

app = FastAPI(title="FLO CLTV Prediction API")


@app.post("/predict_cltv/")
def predict_cltv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    result_df = cltv_pipeline(df)
    return result_df[["cltv", "cltv_segment"]].to_dict(orient="records")
