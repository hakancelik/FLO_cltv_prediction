from invoke import task

@task
def test(c):
    """Tüm otomatik testleri çalıştırır."""
    print("🧪 Testler çalıştırılıyor...")
    c.run("pytest")

@task
def lint(c):
    """Kodun PEP8 ve stil kurallarına uygunluğunu kontrol eder."""
    print("🔍 Kod kalitesi kontrol ediliyor...")
    c.run("flake8 scripts/", pty=True)

@task
def run(c):
    """Ana scripti çalıştırır."""
    c.run("py main.py", pty=True)

@task
def api(c):
    """FastAPI servisini başlatır."""
    c.run("py -m uvicorn main_api:app --reload", pty=True)

@task
def dashboard(c):
    """Streamlit dashboard'u başlatır."""
    print("📊 Dashboard başlatılıyor...")
    c.run("py -m streamlit run dashboard.py")

@task
def docker_build(c):
    """Docker image'ını oluşturur."""
    print("🐳 Docker image oluşturuluyor...")
    c.run("docker build -t flo-cltv .")

@task
def docker_run(c):
    """Docker container'ını çalıştırır."""
    print("🐳 Docker container çalıştırılıyor...")
    c.run("docker run -p 8000:8000 flo-cltv")

@task
def install(c):
    """Tüm bağımlılıkları yükler."""
    print("📦 Bağımlılıklar yükleniyor...")
    c.run("pip install -r requirements.txt")
    c.run("pip install fastapi uvicorn streamlit pytest flake8 invoke")

@task
def full_test(c):
    """Tüm kalite kontrol adımlarını sırayla çalıştırır."""
    print("🔄 Tam kalite kontrol başlıyor...")
    print("\n1️⃣ Testler çalıştırılıyor...")
    test(c)
    print("\n2️⃣ Kod kalitesi kontrol ediliyor...")
    lint(c)
    print("\n3️⃣ Ana script test ediliyor...")
    try:
        c.run("python main.py")
        print("✅ Ana script başarılı!")
    except:
        print("❌ Ana script hatası!")
    print("\n🎉 Tüm kontroller tamamlandı!")

@task
def clean(c):
    """Geçici dosyaları temizler."""
    print("🧹 Temizlik yapılıyor...")
    c.run("find . -name '*.pyc' -delete", warn=True)
    c.run("find . -name '__pycache__' -type d -exec rm -rf {} +", warn=True)
    print("✅ Temizlik tamamlandı!")
