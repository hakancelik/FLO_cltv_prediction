
# FLO CLTV Prediction

🇺🇸 **[English Version](README_EN.md)** | 🇹🇷 **Türkçe Versiyon**

## Overview
FLO müşterileri için yaşam boyu değer (CLTV) tahmini, segmentasyon, otomatik raporlama ve API servisi sunan profesyonel analiz projesi.

## Özellikler
- CLTV hesaplama ve segmentasyon
- Otomatik markdown raporu ve görseller
- FastAPI ile canlı REST API servisi
- Test altyapısı ve kod kalite kontrolü
- Docker ile kolay dağıtım

## Kurulum
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/hakancelik/FLO_cltv_prediction.git
   cd FLO_cltv_prediction
   ```
2. Sanal ortam oluşturun ve bağımlılıkları yükleyin:
   ```bash
   py -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   pip install fastapi uvicorn pytest flake8
   ```

## Kullanım
### Komut Satırı
```bash
python main.py
```
Çıktı ve raporlar `report/` ve `screen/` klasörlerinde oluşur.

### API Servisi
```bash
py -m uvicorn main_api:app --reload
```
Swagger arayüzü: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

#### API Endpointleri
- `POST /predict_cltv/` : CSV dosyası yükleyin, CLTV ve segment sonuçlarını alın.

#### Örnek cURL:
```bash
curl -X POST "http://127.0.0.1:8000/predict_cltv/" -F "file=@data/flo_data_20k.csv"
```

## Otomatik Rapor
Her çalıştırmada `report/report.md` dosyası otomatik güncellenir. İçerik:
- Genel istatistikler
- Segment dağılımı
- CLTV dağılımı ve grafik
- Model parametreleri

## Dosya Yapısı
- `main.py` : Komut satırı ana script
- `main_api.py` : FastAPI servis dosyası
- `scripts/` : Modüller (veri işleme, modelleme, pipeline, raporlama)
- `report/` : Otomatik markdown rapor ve görseller
- `screen/` : Grafikler
- `tests/` : Otomatik testler
- `requirements.txt` : Bağımlılıklar
- `Dockerfile` : (isteğe bağlı, aşağıda örnek)

## Test
Tüm testleri çalıştırmak için:
```bash
pytest
```

## Docker ile Çalıştırma (Opsiyonel)
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt && pip install fastapi uvicorn
CMD ["uvicorn", "main_api:app", "--host", "0.0.0.0", "--port", "8000"]
```
```bash
docker build -t flo-cltv .
docker run -p 8000:8000 flo-cltv
```

## CI/CD
GitHub Actions veya benzeri bir sistemle otomatik test ve kalite kontrol entegrasyonu önerilir.

## Katkı
Katkıda bulunmak için lütfen bir issue açın veya pull request gönderin.

## Lisans
MIT

## Test
Tüm testleri çalıştırmak için:
```bash
pytest
```

## Katkı
Katkıda bulunmak için lütfen bir issue açın veya pull request gönderin.

## Lisans
MIT
