import os


class TraceReader:

  def __init__(self, file_path=None):
    self.file_path = file_path

  def read_addresses(self):
    """Dosyadan veya varsayılan listeden bellek adreslerini okur.

    Dosya satır satır hex (örn: 0x1A4) veya decimal (örn: 420) adresler
    içermelidir.
    """
    addresses = []

    if self.file_path and os.path.exists(self.file_path):
      try:
        with open(self.file_path, "r") as f:
          for line in f:
            line = line.strip()
            # Boş satırları veya yorum satırlarını (# ile başlayan) atla
            if not line or line.startswith("#"):
              continue

            # Hex veya decimal dönüşümü yap
            if line.startswith("0x") or line.startswith("0X"):
              addr = int(line, 16)
            else:
              addr = int(line, 10)
            addresses.append(addr)
        print(f"'{self.file_path}' dosyasından {len(addresses)} adres okundu.")
      except Exception as e:
        print(f"Dosya okunurken hata oluştu: {e}")
    else:
      if self.file_path:
        print(
            f"Uyarı: '{self.file_path}' bulunamadı. Varsayılan test verisi"
            " kullanılıyor."
        )
      # Dosya yoksa veya belirtilmemişse varsayılan örnek trace verisi dön
      addresses = [
          0x00,
          0x04,
          0x40,
          0x44,
          0x00,
          0x80,
          0x04,
          0x40,
          0x100,
          0x104,
          0x00,
      ]

    return addresses