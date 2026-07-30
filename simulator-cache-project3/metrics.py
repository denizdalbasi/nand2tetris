import matplotlib.pyplot as plt


class CacheMetrics:

  def __init__(self, hits, misses):
    self.hits = hits
    self.misses = misses
    self.total_accesses = hits + misses

  def get_hit_rate(self):
    """İsabet (hit) oranını yüzde olarak döner."""
    if self.total_accesses == 0:
      return 0.0
    return (self.hits / self.total_accesses) * 100

  def get_miss_rate(self):
    """Iskalama (miss) oranını yüzde olarak döner."""
    if self.total_accesses == 0:
      return 0.0
    return (self.misses / self.total_accesses) * 100

  def print_summary(self):
    """Konsola düzenli bir özet rapor yazdırır."""
    print("--- Cache Performance Metrics ---")
    print(f"Total Accesses : {self.total_accesses}")
    print(f"Hits           : {self.hits}")
    print(f"Misses         : {self.misses}")
    print(f"Hit Rate       : {self.get_hit_rate():.2f}%")
    print(f"Miss Rate      : {self.get_miss_rate():.2f}%")
    print("-" * 32)

  @staticmethod
  def compare_configurations(results_dict):
    """Farklı cache konfigürasyonlarını (örn. Direct-mapped vs 2-way)

    grafiksel olarak karşılaştırır.
    results_dict formatı: {'Direct-Mapped': hit_rate_1, '2-Way': hit_rate_2}
    """
    configs = list(results_dict.keys())
    hit_rates = list(results_dict.values())

    plt.figure(figsize=(8, 5))
    bars = plt.bar(
        configs, hit_rates, color=["#3498db", "#2ecc71", "#e74c3c", "#f39c12"]
    )

    plt.xlabel("Cache Configurations", fontweight="bold")
    plt.ylabel("Hit Rate (%)", fontweight="bold")
    plt.title("Cache Performance Comparison", fontweight="bold")
    plt.ylim(0, 100)

    # Çubukların üzerine yüzde değerlerini yazdır
    for bar in bars:
      height = bar.get_height()
      plt.text(
          bar.get_x() + bar.get_width() / 2.0,
          height + 1,
          f"{height:.2f}%",
          ha="center",
          va="bottom",
      )

    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()