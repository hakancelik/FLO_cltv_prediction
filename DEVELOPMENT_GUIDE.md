# FLO CLTV Prediction Projesi - Adım Adım Geliştirme Rehberi

🇺🇸 **[English Version](DEVELOPMENT_GUIDE_EN.md)** | 🇹🇷 **Türkçe Versiyon**

## 1. Proje Başlangıcı ve Yapılandırma

### 1.1 Proje Klasör Yapısını Oluşturma
```
FLO_cltv_prediction/
├── data/                    # Ham veri dosyaları
├── scripts/                 # Ana kodlar (modüler yapı)
│   ├── __init__.py
│   ├── data_processing.py   # Veri işleme fonksiyonları
│   ├── modeling.py          # Model fit ve tahmin
│   ├── segmentation.py      # Müşteri segmentasyonu
│   ├── visualization.py     # Grafik ve görselleştirme
│   ├── pipeline.py          # Tüm süreçleri birleştiren ana pipeline
│   └── reporting.py         # Otomatik rapor üretimi
├── tests/                   # Otomatik test dosyaları
├── report/                  # Otomatik rapor çıktıları
├── screen/                  # Grafik çıktıları
├── config.py               # Parametreler ve ayarlar
├── main.py                 # Komut satırı ana script
├── main_api.py             # FastAPI REST servisi
├── dashboard.py            # Streamlit görsel arayüz
├── tasks.py                # Otomasyon komutları (invoke)
├── requirements.txt        # Python bağımlılıkları
├── Dockerfile              # Container yapılandırması
├── .gitignore              # Git ignore dosyası
├── LICENSE                 # Lisans
└── README.md               # Proje dokümantasyonu
```

### 1.2 Temel Dosyaları Oluşturma
- `requirements.txt`: Gerekli Python paketleri
- `config.py`: Tüm parametreleri merkezi olarak yönetmek için
- `.gitignore`: Gereksiz dosyaları git'e eklememek için

## 2. Kod Modüllerini Geliştirme

### 2.1 Veri İşleme Modülü (`scripts/data_processing.py`)
- Veri yükleme fonksiyonu
- Aykırı değer işleme
- Sütun oluşturma (toplam değerler)
- Tarih dönüşümleri

### 2.2 Modelleme Modülü (`scripts/modeling.py`)
- BG/NBD model fit fonksiyonu
- Gamma-Gamma model fit fonksiyonu
- CLTV hesaplama fonksiyonu

### 2.3 Segmentasyon Modülü (`scripts/segmentation.py`)
- CLTV değerine göre müşteri segmentleri oluşturma

### 2.4 Görselleştirme Modülü (`scripts/visualization.py`)
- CLTV dağılım grafikleri
- Segment bazlı analizler
- Grafikleri dosyaya kaydetme

### 2.5 Pipeline Modülü (`scripts/pipeline.py`)
- Tüm süreçleri birleştiren ana fonksiyon
- Tek komutla tüm analizi çalıştırma

### 2.6 Raporlama Modülü (`scripts/reporting.py`)
- Otomatik markdown raporu üretimi
- İstatistiksel özetler
- Grafikleri raporda gösterme

## 3. Profesyonelleştirme Adımları

### 3.1 Kod Kalitesi
- Her fonksiyona docstring eklemek
- Tip ipuçları (type hints) kullanmak
- Logging ile süreç takibi
- Hata yönetimi (try-catch blokları)

### 3.2 Test Altyapısı
- Her modül için test dosyaları (`tests/`)
- pytest ile otomatik test çalıştırma
- Kod kapsamı (coverage) ölçümü

### 3.3 Kod Standardizasyonu
- flake8 ile PEP8 uyumluluğu
- Tutarlı naming convention
- İmport sıralaması

## 4. API ve Görsel Arayüz Geliştirme

### 4.1 FastAPI REST Servisi (`main_api.py`)
- CSV dosyası yükleme endpoint'i
- CLTV tahmin servisi
- Swagger dokümantasyonu

### 4.2 Streamlit Dashboard (`dashboard.py`)
- Dosya yükleme arayüzü
- Sonuçları tablo ve grafiklerle gösterme
- Çıktı indirme özelliği

## 5. DevOps ve Dağıtım

### 5.1 Docker Entegrasyonu
- Dockerfile oluşturma
- Container olarak çalıştırma

### 5.2 CI/CD Pipeline
- GitHub Actions workflow dosyası
- Otomatik test çalıştırma
- Kod kalitesi kontrolü

### 5.3 Otomasyon
- invoke ile komut otomasyonu (`tasks.py`)
- Tek komutla test, lint, çalıştırma

## 6. Dokümantasyon

### 6.1 README.md Güncelleme
- Kurulum talimatları
- Kullanım örnekleri
- API dokümantasyonu
- Dosya yapısı açıklaması

### 6.2 Kod İçi Dokümantasyon
- Fonksiyon açıklamaları
- Kullanım örnekleri
- Parametre açıklamaları

## 7. Son Kontroller ve Yayınlama

### 7.1 Test Süreci
```bash
invoke test        # Otomatik testler
invoke lint        # Kod kalitesi
invoke run         # Ana script
invoke api         # API testi
invoke dashboard   # Dashboard testi
```

### 7.2 Git ve GitHub
- .gitignore kontrolü
- Commit mesajları
- README son kontrol
- License ekleme

## Kullanım Komutları

```bash
# Kurulum
pip install invoke
invoke install

# Geliştirme
invoke test
invoke lint
invoke run

# Servisler
invoke api        # http://127.0.0.1:8000/docs
invoke dashboard  # Streamlit arayüzü

# Kalite kontrol
invoke all-tests  # Tüm kontroller
```

## Önemli Notlar

1. **Modüler Yapı**: Her işlev ayrı modülde, tekrar kullanılabilir
2. **Konfigürasyon**: Tüm parametreler `config.py`'de merkezi
3. **Testler**: Her modül için test yazılmalı
4. **Dokümantasyon**: Kod ve kullanım dokümante edilmeli
5. **Versiyon Kontrolü**: Git ile düzenli commit'ler
6. **Hata Yönetimi**: Try-catch blokları ve logging
7. **Performans**: Büyük veri setleri için optimizasyon
