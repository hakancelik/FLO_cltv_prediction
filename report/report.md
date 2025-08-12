# 📊 FLO CLTV Prediction Raporu

**Oluşturulma Tarihi:** 2025-08-12 21:07

**Toplam Müşteri Sayısı:** 19,945

## 📈 Executive Summary

- **Toplam CLTV:** 3,172,465.00 TL
- **Ortalama CLTV:** 159.06 TL
- **Medyan CLTV:** 127.84 TL

## 🎯 Segment Analizi

### Segment Bazında Detaylı İstatistikler

| Segment | Müşteri Sayısı | Ortalama CLTV | Toplam CLTV | Ortalama Harcama | Ortalama Frequency |
|---------|----------------|---------------|-------------|------------------|--------------------|
| A | 4,987 | 57.87 TL | 288,597.82 TL | 96.29 TL | 2.51 |
| B | 9,972 | 130.69 TL | 1,303,198.59 TL | 146.30 TL | 3.55 |
| C | 4,986 | 317.02 TL | 1,580,668.59 TL | 220.72 TL | 6.48 |

## 📊 Görsel Analizler

### 1. 📈 CLTV Dağılımı
Bu grafik müşterilerin CLTV değerlerinin genel dağılımını gösterir. Çoğu müşterinin düşük-orta CLTV değerlerine sahip olduğu, az sayıda müşterinin ise çok yüksek CLTV değerlerine sahip olduğu görülmektedir.

![CLTV Dağılımı](https://raw.githubusercontent.com/hakancelik/FLO_cltv_prediction/main/screen/cltv_distribution.png)

### 2. 📊 Segment Bazında CLTV Dağılımı
Bu kutu grafiği, her segment içindeki CLTV değerlerinin dağılımını gösterir. C segmenti en yüksek CLTV değerlerine sahipken, A segmenti en düşük değerlere sahiptir. B segmenti ise orta seviyede yer almaktadır.

![Segment Bazında CLTV Dağılımı](https://raw.githubusercontent.com/hakancelik/FLO_cltv_prediction/main/screen/cltv_distribution_by_segment.png)

### 3. 👥 Müşteri Sayısı ve Toplam CLTV (Segment Bazında)
Sol grafik her segmentteki müşteri sayısını, sağ grafik ise her segmentin toplam CLTV katkısını gösterir. B segmentinin müşteri sayısı en fazla iken, C segmentinin toplam CLTV değeri en yüksektir.

![Müşteri Sayısı ve Toplam CLTV](https://raw.githubusercontent.com/hakancelik/FLO_cltv_prediction/main/screen/number_of_customers_and_total_cltv_by_segment.png)

### 4. 💰 Ortalama Harcama (Segment Bazında)
Bu grafik her segmentin ortalama harcama tutarını gösterir. C segmenti müşterileri en yüksek ortalama harcamaya sahipken, A segmenti en düşük ortalama harcamaya sahiptir.

![Ortalama Harcama](https://raw.githubusercontent.com/hakancelik/FLO_cltv_prediction/main/screen/average_spending_by_cltv_segment.png)

### 5. 🥧 Müşteri Dağılımı (Segment Bazında)
Bu pasta grafiği müşterilerin segmentlere göre yüzdelik dağılımını gösterir. Müşteri portföyünün segment bazında oransal dağılımını görsel olarak sunar.

![Müşteri Dağılımı](https://raw.githubusercontent.com/hakancelik/FLO_cltv_prediction/main/screen/customer_distribution_by_cltv_segment.png)

### 6. 📊 Expected Average Value Dağılımı
Bu grafik müşterilerin gelecekteki ortalama harcama değerlerinin dağılımını gösterir. Model tarafından tahmin edilen bu değerler, müşterilerin gelecekteki alışveriş davranışları hakkında öngörü sağlar.

![Expected Value Dağılımları](https://raw.githubusercontent.com/hakancelik/FLO_cltv_prediction/main/screen/expected_average_value_distribution.png)

### 7. 🎯 Expected Sales (Segment Bazında)
Bu grafik her segmentin gelecek dönemdeki ortalama satış beklentisini gösterir. C segmenti müşterilerinden en yüksek satış beklentisi vardır.

![Expected Sales](https://raw.githubusercontent.com/hakancelik/FLO_cltv_prediction/main/screen/expected_sales_by_cltv_segment.png)

### 8. 🔍 Recency vs Frequency Analizi
Bu scatter plot müşterilerin recency (son alışverişten geçen süre) ve frequency (alışveriş sıklığı) değerlerini CLTV ile ilişkilendirir. Renkli noktalar CLTV değerini, farklı şekiller ise segmentleri temsil eder. Yüksek frequency ve düşük recency değerleri genellikle yüksek CLTV ile ilişkilidir.

![Recency vs Frequency](https://raw.githubusercontent.com/hakancelik/FLO_cltv_prediction/main/screen/recency_vs_frequency_by_cltv_segment.png)

## 📋 Detaylı İstatistikler

### Genel Veri İstatistikleri
|       |   order_num_total |   customer_value_total | first_order_date              | last_order_date               |   frequency |   recency_cltv_weekly |     T_weekly |   monetary_cltv_avg |   expected_sales |   expected_average_value |          cltv |
|:------|------------------:|-----------------------:|:------------------------------|:------------------------------|------------:|----------------------:|-------------:|--------------------:|-----------------:|-------------------------:|--------------:|
| count |       19945       |              19945     | 19945                         | 19945                         | 19945       |            19945      | 19945        |          19945      |  19945           |               19945      | 19945         |
| mean  |           5.02477 |                751.244 | 2019-03-22 16:43:55.246929152 | 2021-01-17 12:59:57.653547264 |     4.02477 |               95.2635 |   114.472    |            152.399  |      0.22916     |                 164.557  |   159.061     |
| min   |           2       |                 44.98  | 2013-01-14 00:00:00           | 2020-05-30 00:00:00           |     1       |                0      |     0.714286 |             22.49   |      4.01146e-05 |                  26.3602 |     0.0164317 |
| 25%   |           3       |                339.98  | 2019-02-16 00:00:00           | 2020-11-11 00:00:00           |     2       |               50.4286 |    73.8571   |            103.49   |      0.145767    |                 111.391  |    82.7295    |
| 50%   |           4       |                545.27  | 2019-08-20 00:00:00           | 2021-02-10 00:00:00           |     3       |               76.5714 |    93        |            136.735  |      0.198461    |                 146.916  |   127.837     |
| 75%   |           6       |                897.78  | 2020-01-01 00:00:00           | 2021-04-19 00:00:00           |     5       |              109.429  |   119.429    |            182.445  |      0.274677    |                 195.941  |   193.04      |
| max   |         202       |              45905.1   | 2021-05-27 00:00:00           | 2021-05-30 00:00:00           |   201       |              433.429  |   437.143    |           5176.59   |      3.60681     |                5406.74   | 13540.6       |
| std   |           4.74271 |                895.402 | nan                           | nan                           |     4.74271 |               74.5894 |    74.771    |             83.5039 |      0.137485    |                  90.1132 |   180.657     |

## 🤖 Model Bilgileri

- **BGF**: <lifetimes.BetaGeoFitter: fitted with 19945 subjects, a: 0.00, alpha: 50.73, b: 0.08, r: 1.94>
- **GGF**: <lifetimes.GammaGammaFitter: fitted with 19945 subjects, p: 4.18, q: 0.47, v: 4.06>

## 💡 Öneriler

1. **En Yüksek Değerli Segment (C):** Bu segment müşterilerine özel sadakat programları uygulanmalı.
2. **En Düşük Değerli Segment (A):** Bu segment için aktivasyon kampanyaları düzenlenebilir.
3. **Orta Segment Müşteriler:** Upselling ve cross-selling fırsatları değerlendirilebilir.
4. **Yüksek Frequency Müşteriler:** Daha sık alışveriş yapan müşterilere özel indirimler sunulabilir.

---
*Bu rapor FLO CLTV Prediction sistemi tarafından otomatik oluşturulmuştur.*
