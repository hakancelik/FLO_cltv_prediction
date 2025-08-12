# Universal Data Science Project Template

Bu template, herhangi bir veri bilimi projesinde hızlı başlangıç için kullanılabilir.

## 📋 Kurulum Rehberi

### 1. Template'i Kopyala
```bash
cp -r /path/to/project_template your_new_project
cd your_new_project
```

### 2. Proje Özelleştirmesi
- README.md'de {{PROJECT_NAME}} kısımlarını değiştir
- config/config.yaml'da proje ayarlarını güncelle
- requirements.txt'e projeye özel paketleri ekle

### 3. Sanal Ortam Kur
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 4. Test Et
```bash
python test_all.py
```

## 🛠️ Template Özellikleri

✅ **Modüler Yapı**: src/ klasöründe organized kod  
✅ **API Servisi**: FastAPI ile hazır REST API  
✅ **Dashboard**: Streamlit ile görsel arayüz  
✅ **Otomatik Test**: pytest ile comprehensive testing  
✅ **CI/CD**: GitHub Actions workflow  
✅ **Docker**: Container deployment ready  
✅ **Reporting**: Otomatik rapor sistemi  
✅ **Config**: YAML-based configuration  

## 📁 Klasör Yapısı

```
your_project/
├── src/                     # Ana kaynak kodlar
│   ├── data/
│   │   ├── loader.py        # Veri yükleme fonksiyonları
│   │   ├── processor.py     # Veri işleme pipeline
│   │   └── validator.py     # Veri doğrulama
│   ├── models/
│   │   ├── base.py          # Temel model sınıfı
│   │   ├── trainer.py       # Model eğitimi
│   │   └── predictor.py     # Tahmin fonksiyonları
│   ├── utils/
│   │   ├── logger.py        # Logging sistemi
│   │   ├── config.py        # Config yöneticisi
│   │   ├── metrics.py       # Performans metrikleri
│   │   └── visualization.py # Plot ve grafik fonksiyonları
│   ├── pipeline/
│   │   ├── training.py      # Eğitim pipeline
│   │   └── inference.py     # Tahmin pipeline
│   └── reporting/
│       ├── generator.py     # Rapor üretici
│       └── templates/       # Rapor şablonları
├── api/
│   ├── main.py             # FastAPI ana dosya
│   └── endpoints/          # API endpoint'leri
├── dashboard/
│   ├── app.py              # Streamlit ana dosya
│   └── components/         # Dashboard bileşenleri
├── config/
│   ├── config.yaml         # Ana konfigürasyon
│   └── model_config.yaml   # Model parametreleri
├── tests/                   # Test dosyaları
├── data/                    # Veri klasörleri
├── reports/                 # Otomatik raporlar
├── outputs/                 # Model ve sonuçlar
├── docker/                  # Docker dosyaları
├── .github/workflows/       # CI/CD
├── main.py                  # Ana çalıştırma scripti
├── test_all.py              # Kapsamlı test scripti
├── tasks.py                 # Invoke otomasyon
├── requirements.txt         # Python bağımlılıkları
└── setup.py                 # Paket kurulum
```

## 🚀 Kullanım Alanları

Bu template şu projeler için idealdir:
- 🤖 Machine Learning modelleri
- 📊 Data Analytics dashboardları
- 🔍 Computer Vision uygulamaları
- 💬 NLP projeleri
- 📈 Time Series forecasting
- 🌐 REST API servisleri
- 📋 Interactive dashboardları

## 🔧 Hızlı Özelleştirme

1. **Project Name**: Tüm dosyalarda {{PROJECT_NAME}} değiştir
2. **Dependencies**: requirements.txt güncelle
3. **Config**: config/config.yaml parametrelerini ayarla
4. **Data Pipeline**: src/data/ modüllerini customize et
5. **Models**: src/models/ klasörüne model kodlarını ekle
6. **API**: api/endpoints/ klasörüne endpoint'leri ekle
7. **Dashboard**: dashboard/components/ klasörüne bileşenleri ekle

## 📝 Template Dosyaları

Template'de hazır gelen dosyalar:
- ✅ Comprehensive README.md
- ✅ Modular source code structure
- ✅ FastAPI boilerplate
- ✅ Streamlit dashboard template
- ✅ pytest test framework
- ✅ GitHub Actions CI/CD
- ✅ Docker configuration
- ✅ Pre-commit hooks
- ✅ Logging configuration
- ✅ Error handling patterns
