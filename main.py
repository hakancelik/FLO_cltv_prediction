#!/usr/bin/env python
"""
FLO CLTV Prediction - Main Script
Runs the complete CLTV pipeline including data processing, modeling, segmentation, and reporting.
"""

from scripts.data_processing import load_data
from scripts.pipeline import cltv_pipeline
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    """Main function to run the complete CLTV analysis pipeline."""
    try:
        print("🚀 FLO CLTV Prediction Pipeline Başlıyor...")

        # Load data
        df = load_data()
        print(f"📊 Veri yüklendi: {len(df)} müşteri")

        # Run complete pipeline
        result_df = cltv_pipeline(df)

        print("✅ Pipeline başarıyla tamamlandı!")
        print(f"📈 CLTV hesaplanan müşteri sayısı: {len(result_df)}")
        print("📂 Raporlar 'report/' klasöründe oluşturuldu")
        print("📊 Grafikler 'screen/' klasöründe kaydedildi")

        # Show segment summary
        if 'cltv_segment' in result_df.columns:
            segment_counts = result_df['cltv_segment'].value_counts().sort_index()
            print("\n📋 Segment Dağılımı:")
            for segment, count in segment_counts.items():
                print(f"   {segment}: {count} müşteri")

    except Exception as e:
        logging.error(f"Pipeline sırasında hata oluştu: {e}")
        print(f"❌ Hata: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())

