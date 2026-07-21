import sys
from src.cache import Cache
from src.policy import DirectMappedPolicy, SetAssociativePolicy


def parse_trace_line(line: str) -> tuple[str, int] | None:
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    parts = line.split()
    if len(parts) < 2:
        return None
    op = parts[0].upper()
    addr = int(parts[1], 16) if parts[1].startswith("0x") else int(parts[1])
    return op, addr


def run_simulation(policy, trace_data: list[tuple[str, int]]) -> Cache:
    cache = Cache(num_sets=policy.num_sets, associativity=policy.associativity)
    for op, addr in trace_data:
        tag, index, _ = policy.parse_address(addr)
        is_write = op in ("W", "WRITE", "STORE")
        cache.access(tag, index, is_write=is_write)
    return cache


def generate_sample_trace() -> list[tuple[str, int]]:
    return [
        ("R", 0x0000),
        ("R", 0x0004),
        ("W", 0x0008),
        ("R", 0x0000),
        ("R", 0x1000),
        ("R", 0x2000),
        ("R", 0x0000),
        ("R", 0x1000),
        ("R", 0x0004),
        ("W", 0x000C),
    ]


def print_report(name: str, cache: Cache):
    total = cache.hits + cache.misses
    print(f"=== {name} ===")
    print(f"Total Accesses : {total}")
    print(f"Hits           : {cache.hits}")
    print(f"Misses         : {cache.misses}")
    print(f"Hit Rate       : {cache.hit_rate:.2f}%\n")


def main():
    trace_file = sys.argv[1] if len(sys.argv) > 1 else None

    if trace_file:
        trace_data = []
        with open(trace_file, "r") as f:
            for line in f:
                parsed = parse_trace_line(line)
                if parsed:
                    trace_data.append(parsed)
    else:
        trace_data = generate_sample_trace()

    cache_size = 1024
    block_size = 32

    direct_policy = DirectMappedPolicy(cache_size, block_size)
    two_way_policy = SetAssociativePolicy(cache_size, block_size, associativity=2)

    direct_cache = run_simulation(direct_policy, trace_data)
    two_way_cache = run_simulation(two_way_policy, trace_data)

    print_report("Direct-Mapped Cache (1-Way)", direct_cache)
    print_report("2-Way Set Associative Cache", two_way_cache)


if __name__ == "__main__":
    main()