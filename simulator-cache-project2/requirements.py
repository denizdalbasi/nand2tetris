import importlib
import subprocess
import sys

# Proje için gerekli paketler ve minimum versiyonları
REQUIRED_PACKAGES = {
    "pytest": "7.0.0",  # ALU ve Cache test suite için
}


def check_and_install_requirements():
    """Gerekli paketlerin yüklü olup olmadığını kontrol eder, eksikleri yükler."""
    print("🔍 Bağımlılıklar kontrol ediliyor...\n")
    missing_packages = []

    for package, min_version in REQUIRED_PACKAGES.items():
        try:
            mod = importlib.import_module(package)
            version = getattr(mod, "__version__", "Bilinmiyor")
            print(f"  [✓] {package} yüklü (Versiyon: {version})")
        except ImportError:
            print(f"  [✗] {package} eksik! (Gerekli: >= {min_version})")
            missing_packages.append(package)

    if missing_packages:
        print("\n⚙️  Eksik paketler kuruluyor...")
        for pkg in missing_packages:
            try:
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", pkg]
                )
                print(f"  [✓] {pkg} başarıyla kuruldu.")
            except subprocess.CalledProcessError:
                print(f"  [!] {pkg} yüklenirken hata oluştu.")
    else:
        print("\n✨ Tüm bağımlılıklar hazır!")
