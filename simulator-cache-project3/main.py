from cache import Cache
from metrics import CacheMetrics
from trace_reader import TraceReader


def main():
    reader = TraceReader("traces/sample.txt")
    addresses = reader.read_addresses()

    direct_mapped_cache = Cache(capacity=1024, block_size=64, associativity=1)
    for addr in addresses:
        direct_mapped_cache.access(addr)
    
    metrics_dm = direct_mapped_cache.get_metrics()
    dm_metrics_obj = CacheMetrics(metrics_dm["hits"], metrics_dm["misses"])
    print("--- Direct-Mapped Cache Metrics ---")
    dm_metrics_obj.print_summary()

    print("\n" + "="*40 + "\n")

    set_associative_cache = Cache(capacity=1024, block_size=64, associativity=2)
    for addr in addresses:
        set_associative_cache.access(addr)
    
    metrics_sa = set_associative_cache.get_metrics()
    sa_metrics_obj = CacheMetrics(metrics_sa["hits"], metrics_sa["misses"])
    print("--- 2-Way Set Associative Cache Metrics ---")
    sa_metrics_obj.print_summary()

    CacheMetrics.compare_configurations({
        "Direct-Mapped": dm_metrics_obj.get_hit_rate(),
        "2-Way": sa_metrics_obj.get_hit_rate()
    })


if __name__ == "__main__":
    main()