import matplotlib.pyplot as plt
import seaborn as sns

def plot_cltv_distribution(cltv_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(cltv_df['cltv'], bins=50, kde=True)
    plt.title('CLTV Distribution')
    plt.xlabel('CLTV')
    plt.ylabel('Frequency')
    plt.show()

def plot_cltv_segments(cltv_df): # Segmentlere göre CLTV dağılımı
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='cltv_segment', y='cltv', data=cltv_df)
    plt.title('CLTV Distribution by Segment')
    plt.xlabel('Segment')
    plt.ylabel('CLTV')
    plt.savefig("reports/cltv_distribution_by_segment.png")
    plt.show()

def plot_cltv_over_time(cltv_df): # Zamanla CLTV değişimi
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='cltv', data=cltv_df)
    plt.title('CLTV Over Time')
    plt.xlabel('Date')
    plt.ylabel('CLTV')
    plt.savefig("reports/cltv_over_time.png")
    plt.show()

def mean_selling(cltv_df):# Ortalama harcama değeri
    plt.figure(figsize=(10, 6))
    sns.histplot(cltv_df['exp_average_value'], bins=50, kde=True)
    plt.title('Expected Average Value Distribution')
    plt.xlabel('Expected Average Value')
    plt.ylabel('Frequency')
    plt.savefig("reports/expected_average_value_distribution.png")
    plt.show()