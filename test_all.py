# test_all.py - Tüm kalite kontrol adımlarını çalıştıran script

import subprocess
import sys
import os

def run_command(command, description):
    """Komut çalıştırır ve sonucu gösterir."""
    print(f"\n{'='*50}")
    print(f"🔄 {description}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - BAŞARILI")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ {description} - HATA")
            if result.stderr:
                print(result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ {description} - HATA: {e}")
        return False

def main():
    """Ana test süreci."""
    print("🚀 FLO CLTV Prediction - Tam Kalite Kontrol Başlıyor...")
    
    # Önce bağımlılık kontrolü
    try:
        import pandas
        import matplotlib
        import seaborn
        print("✅ Temel bağımlılıklar mevcut")
    except ImportError as e:
        print(f"❌ Eksik bağımlılık: {e}")
        print("🔧 Lütfen önce 'pip install -r requirements.txt' çalıştırın")
        return
    
    tests = [
        ("python -m pytest --tb=short", "Otomatik Testler"),
        ("python -m flake8 scripts/ main.py dashboard.py main_api.py --max-line-length=100 --exclude=venv --ignore=W391,W291,W504", "Kod Kalitesi Kontrolü"),
        ("python -c \"from scripts.pipeline import cltv_pipeline; print('Pipeline import OK')\"", "Pipeline Import Testi"),
    ]
    
    passed = 0
    failed = 0
    
    for command, description in tests:
        if run_command(command, description):
            passed += 1
        else:
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"📊 SONUÇ RAPORU")
    print(f"{'='*50}")
    print(f"✅ Başarılı: {passed}")
    print(f"❌ Başarısız: {failed}")
    print(f"📈 Toplam: {passed + failed}")
    
    if failed == 0:
        print("🎉 TÜM TESTLER BAŞARILI! Push etmeye hazır.")
        sys.exit(0)
    else:
        print("⚠️  Bazı testler başarısız. Lütfen hataları düzeltin.")
        sys.exit(1)

if __name__ == "__main__":
    main()
