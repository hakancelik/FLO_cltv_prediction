import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

REPORT_DIR = "report"
SCREEN_DIR = "screen"
REPORT_PATH = os.path.join(REPORT_DIR, "report.md")

os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(SCREEN_DIR, exist_ok=True)


def create_visualizations(df: pd.DataFrame):
    """
    Tüm CLTV görsellerini oluşturur ve screen/ klasörüne kaydeder.
    """
    # Set style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # 1. CLTV Dağılımı
    plt.figure(figsize=(10, 6))
    sns.histplot(df['cltv'], bins=50, kde=True, alpha=0.7)
    plt.title('CLTV Dağılımı', fontsize=16, fontweight='bold')
    plt.xlabel('CLTV Değeri', fontsize=12)
    plt.ylabel('Müşteri Sayısı', fontsize=12)
    plt.tight_layout()
    plt.savefig(f'{SCREEN_DIR}/cltv_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Segment bazında CLTV dağılımı
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='cltv_segment', y='cltv')
    plt.title('Segment Bazında CLTV Dağılımı', fontsize=16, fontweight='bold')
    plt.xlabel('CLTV Segmenti', fontsize=12)
    plt.ylabel('CLTV Değeri', fontsize=12)
    plt.tight_layout()
    plt.savefig(f'{SCREEN_DIR}/cltv_distribution_by_segment.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Müşteri sayısı ve toplam CLTV segment bazında
    plt.figure(figsize=(14, 6))
    segment_stats = df.groupby('cltv_segment').agg({
        'cltv': ['count', 'sum']
    }).round(2)
    segment_stats.columns = ['Müşteri Sayısı', 'Toplam CLTV']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Müşteri sayısı
    segment_stats['Müşteri Sayısı'].plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_title('Segment Bazında Müşteri Sayısı', fontweight='bold')
    ax1.set_xlabel('CLTV Segmenti')
    ax1.set_ylabel('Müşteri Sayısı')
    ax1.tick_params(axis='x', rotation=0)
    
    # Toplam CLTV
    segment_stats['Toplam CLTV'].plot(kind='bar', ax=ax2, color='lightcoral')
    ax2.set_title('Segment Bazında Toplam CLTV', fontweight='bold')
    ax2.set_xlabel('CLTV Segmenti')
    ax2.set_ylabel('Toplam CLTV')
    ax2.tick_params(axis='x', rotation=0)
    
    plt.tight_layout()
    plt.savefig(f'{SCREEN_DIR}/number_of_customers_and_total_cltv_by_segment.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Ortalama harcama segment bazında
    plt.figure(figsize=(10, 6))
    avg_spending = df.groupby('cltv_segment')['monetary_cltv_avg'].mean()
    sns.barplot(x=avg_spending.index, y=avg_spending.values, palette='viridis')
    plt.title('Segment Bazında Ortalama Harcama', fontsize=16, fontweight='bold')
    plt.xlabel('CLTV Segmenti', fontsize=12)
    plt.ylabel('Ortalama Harcama', fontsize=12)
    plt.tight_layout()
    plt.savefig(f'{SCREEN_DIR}/average_spending_by_cltv_segment.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 5. Müşteri dağılımı segment bazında (pasta grafik)
    plt.figure(figsize=(8, 8))
    segment_counts = df['cltv_segment'].value_counts()
    plt.pie(segment_counts.values, labels=segment_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('CLTV Segmentlerine Göre Müşteri Dağılımı', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f'{SCREEN_DIR}/customer_distribution_by_cltv_segment.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 6. Expected Sales ve Expected Average Value dağılımları
    if 'expected_average_value' in df.columns:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Expected Average Value
        sns.histplot(df['expected_average_value'], bins=30, kde=True, ax=ax1, alpha=0.7)
        ax1.set_title('Expected Average Value Dağılımı', fontweight='bold')
        ax1.set_xlabel('Expected Average Value')
        ax1.set_ylabel('Müşteri Sayısı')
        
        # Expected Sales
        if 'expected_sales' in df.columns:
            sns.histplot(df['expected_sales'], bins=30, kde=True, ax=ax2, alpha=0.7)
            ax2.set_title('Expected Sales Dağılımı', fontweight='bold')
            ax2.set_xlabel('Expected Sales')
            ax2.set_ylabel('Müşteri Sayısı')
        
        plt.tight_layout()
        plt.savefig(f'{SCREEN_DIR}/expected_average_value_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # Expected Sales by segment
        if 'expected_sales' in df.columns:
            plt.figure(figsize=(10, 6))
            expected_sales_by_segment = df.groupby('cltv_segment')['expected_sales'].mean()
            sns.barplot(x=expected_sales_by_segment.index, y=expected_sales_by_segment.values, palette='plasma')
            plt.title('Segment Bazında Ortalama Expected Sales', fontsize=16, fontweight='bold')
            plt.xlabel('CLTV Segmenti', fontsize=12)
            plt.ylabel('Ortalama Expected Sales', fontsize=12)
            plt.tight_layout()
            plt.savefig(f'{SCREEN_DIR}/expected_sales_by_cltv_segment.png', dpi=300, bbox_inches='tight')
            plt.close()
    
    # 7. Recency vs Frequency scatter plot
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(df['recency_cltv_weekly'], df['frequency'], 
                         c=df['cltv'], s=60, alpha=0.6, cmap='viridis')
    plt.colorbar(scatter, label='CLTV Değeri')
    plt.title('Recency vs Frequency (CLTV Segmentleri)', fontsize=16, fontweight='bold')
    plt.xlabel('Recency (hafta)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    
    # Segment renklerini ekle
    segments = df['cltv_segment'].unique()
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    for i, segment in enumerate(segments):
        segment_data = df[df['cltv_segment'] == segment]
        plt.scatter(segment_data['recency_cltv_weekly'], segment_data['frequency'], 
                   alpha=0.3, s=100, label=f'Segment {segment}', 
                   color=colors[i % len(colors)])
    
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'{SCREEN_DIR}/recency_vs_frequency_by_cltv_segment.png', dpi=300, bbox_inches='tight')
    plt.close()


def generate_report(df: pd.DataFrame, model_info: dict = None):
    """
    CLTV pipeline sonrası kapsamlı markdown raporu üretir.
    Args:
        df (pd.DataFrame): CLTV ve segment sütunları eklenmiş veri
        model_info (dict): Model parametreleri ve özetleri (opsiyonel)
    """
    # Önce tüm görselleri oluştur
    create_visualizations(df)
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("# 📊 FLO CLTV Prediction Raporu\n\n")
        f.write(f"**Oluşturulma Tarihi:** {now}\n\n")
        f.write(f"**Toplam Müşteri Sayısı:** {len(df):,}\n\n")
        
        # Executive Summary
        f.write("## 📈 Executive Summary\n\n")
        total_cltv = df['cltv'].sum()
        avg_cltv = df['cltv'].mean()
        median_cltv = df['cltv'].median()
        
        f.write(f"- **Toplam CLTV:** {total_cltv:,.2f} TL\n")
        f.write(f"- **Ortalama CLTV:** {avg_cltv:,.2f} TL\n")
        f.write(f"- **Medyan CLTV:** {median_cltv:,.2f} TL\n\n")
        
        # Segment Analysis
        f.write("## 🎯 Segment Analizi\n\n")
        segment_stats = df.groupby('cltv_segment').agg({
            'cltv': ['count', 'mean', 'sum'],
            'monetary_cltv_avg': 'mean',
            'frequency': 'mean'
        }).round(2)
        
        f.write("### Segment Bazında Detaylı İstatistikler\n\n")
        f.write("| Segment | Müşteri Sayısı | Ortalama CLTV | Toplam CLTV | Ortalama Harcama | Ortalama Frequency |\n")
        f.write("|---------|----------------|---------------|-------------|------------------|--------------------|\n")
        
        for segment in segment_stats.index:
            customer_count = int(segment_stats.loc[segment, ('cltv', 'count')])
            avg_cltv = segment_stats.loc[segment, ('cltv', 'mean')]
            total_cltv = segment_stats.loc[segment, ('cltv', 'sum')]
            avg_monetary = segment_stats.loc[segment, ('monetary_cltv_avg', 'mean')]
            avg_freq = segment_stats.loc[segment, ('frequency', 'mean')]
            
            f.write(f"| {segment} | {customer_count:,} | {avg_cltv:,.2f} TL | {total_cltv:,.2f} TL | {avg_monetary:,.2f} TL | {avg_freq:.2f} |\n")
        
        f.write("\n")
        
        # Visualizations
        f.write("## 📊 Görsel Analizler\n\n")
        
        f.write("### 1. 📈 CLTV Dağılımı\n")
        f.write("Bu grafik müşterilerin CLTV değerlerinin genel dağılımını gösterir. ")
        f.write("Çoğu müşterinin düşük-orta CLTV değerlerine sahip olduğu, ")
        f.write("az sayıda müşterinin ise çok yüksek CLTV değerlerine sahip olduğu görülmektedir.\n\n")
        f.write("![CLTV Dağılımı](screen/cltv_distribution.png)\n\n")
        
        f.write("### 2. 📊 Segment Bazında CLTV Dağılımı\n")
        f.write("Bu kutu grafiği, her segment içindeki CLTV değerlerinin dağılımını gösterir. ")
        f.write("C segmenti en yüksek CLTV değerlerine sahipken, A segmenti en düşük değerlere sahiptir. ")
        f.write("B segmenti ise orta seviyede yer almaktadır.\n\n")
        f.write("![Segment Bazında CLTV Dağılımı](screen/cltv_distribution_by_segment.png)\n\n")
        
        f.write("### 3. 👥 Müşteri Sayısı ve Toplam CLTV (Segment Bazında)\n")
        f.write("Sol grafik her segmentteki müşteri sayısını, sağ grafik ise ")
        f.write("her segmentin toplam CLTV katkısını gösterir. ")
        f.write("B segmentinin müşteri sayısı en fazla iken, C segmentinin toplam CLTV değeri en yüksektir.\n\n")
        f.write("![Müşteri Sayısı ve Toplam CLTV](screen/number_of_customers_and_total_cltv_by_segment.png)\n\n")
        
        f.write("### 4. 💰 Ortalama Harcama (Segment Bazında)\n")
        f.write("Bu grafik her segmentin ortalama harcama tutarını gösterir. ")
        f.write("C segmenti müşterileri en yüksek ortalama harcamaya sahipken, ")
        f.write("A segmenti en düşük ortalama harcamaya sahiptir.\n\n")
        f.write("![Ortalama Harcama](screen/average_spending_by_cltv_segment.png)\n\n")
        
        f.write("### 5. 🥧 Müşteri Dağılımı (Segment Bazında)\n")
        f.write("Bu pasta grafiği müşterilerin segmentlere göre yüzdelik dağılımını gösterir. ")
        f.write("Müşteri portföyünün segment bazında oransal dağılımını görsel olarak sunar.\n\n")
        f.write("![Müşteri Dağılımı](screen/customer_distribution_by_cltv_segment.png)\n\n")
        
        f.write("### 6. 📊 Expected Average Value Dağılımı\n")
        f.write("Bu grafik müşterilerin gelecekteki ortalama harcama değerlerinin dağılımını gösterir. ")
        f.write("Model tarafından tahmin edilen bu değerler, müşterilerin gelecekteki ")
        f.write("alışveriş davranışları hakkında öngörü sağlar.\n\n")
        f.write("![Expected Value Dağılımları](screen/expected_average_value_distribution.png)\n\n")
        
        f.write("### 7. 🎯 Expected Sales (Segment Bazında)\n")
        f.write("Bu grafik her segmentin gelecek dönemdeki ortalama satış beklentisini gösterir. ")
        f.write("C segmenti müşterilerinden en yüksek satış beklentisi vardır.\n\n")
        f.write("![Expected Sales](screen/expected_sales_by_cltv_segment.png)\n\n")
        
        f.write("### 8. 🔍 Recency vs Frequency Analizi\n")
        f.write("Bu scatter plot müşterilerin recency (son alışverişten geçen süre) ve ")
        f.write("frequency (alışveriş sıklığı) değerlerini CLTV ile ilişkilendirir. ")
        f.write("Renkli noktalar CLTV değerini, farklı şekiller ise segmentleri temsil eder. ")
        f.write("Yüksek frequency ve düşük recency değerleri genellikle yüksek CLTV ile ilişkilidir.\n\n")
        f.write("![Recency vs Frequency](screen/recency_vs_frequency_by_cltv_segment.png)\n\n")
        
        # Detailed Statistics
        f.write("## 📋 Detaylı İstatistikler\n\n")
        f.write("### Genel Veri İstatistikleri\n")
        f.write(df.describe().to_markdown() + "\n\n")
        
        # Model Information
        if model_info:
            f.write("## 🤖 Model Bilgileri\n\n")
            for k, v in model_info.items():
                f.write(f"- **{k}**: {v}\n")
            f.write("\n")
        
        # Recommendations
        f.write("## 💡 Öneriler\n\n")
        
        high_value_segment = df.groupby('cltv_segment')['cltv'].mean().idxmax()
        low_value_segment = df.groupby('cltv_segment')['cltv'].mean().idxmin()
        
        f.write(f"1. **En Yüksek Değerli Segment ({high_value_segment}):** Bu segment müşterilerine özel sadakat programları uygulanmalı.\n")
        f.write(f"2. **En Düşük Değerli Segment ({low_value_segment}):** Bu segment için aktivasyon kampanyaları düzenlenebilir.\n")
        f.write("3. **Orta Segment Müşteriler:** Upselling ve cross-selling fırsatları değerlendirilebilir.\n")
        f.write("4. **Yüksek Frequency Müşteriler:** Daha sık alışveriş yapan müşterilere özel indirimler sunulabilir.\n\n")
        
        f.write("---\n")
        f.write("*Bu rapor FLO CLTV Prediction sistemi tarafından otomatik oluşturulmuştur.*\n")




