class CacheLine:
    def __init__(self):
        self.valid = False
        self.dirty = False
        self.tag = None
        self.last_used = 0


class CacheSet:
    def __init__(self, associativity: int):
        self.lines = [CacheLine() for _ in range(associativity)]


class Cache:
    def __init__(self, num_sets: int, associativity: int):
        self.num_sets = num_sets
        self.associativity = associativity
        self.sets = [CacheSet(associativity) for _ in range(num_sets)]
        self.hits = 0
        self.misses = 0
        self.access_counter = 0

    def access(self, tag: int, index: int, is_write: bool = False) -> bool:
        self.access_counter += 1
        target_set = self.sets[index]

        for line in target_set.lines:
            if line.valid and line.tag == tag:
                self.hits += 1
                line.last_used = self.access_counter
                if is_write:
                    line.dirty = True
                return True

        self.misses += 1
        self._allocate(target_set, tag, is_write)
        return False

    def _allocate(self, target_set: CacheSet, tag: int, is_write: bool):
        for line in target_set.lines:
            if not line.valid:
                line.valid = True
                line.tag = tag
                line.dirty = is_write
                line.last_used = self.access_counter
                return

        lru_line = min(target_set.lines, key=lambda l: l.last_used)
        lru_line.tag = tag
        lru_line.dirty = is_write
        lru_line.last_used = self.access_counter

    @property
    def hit_rate(self) -> float:
        total = self.hits + self.misses
        return (self.hits / total * 100) if total > 0 else 0.0

    def reset_stats(self):
        self.hits = 0
        self.misses = 0
        self.access_counter = 0