class Cache:
    def __init__(self, capacity=1024, block_size=64, associativity=1, replacement_policy='LRU'):
        self.capacity = capacity
        self.block_size = block_size
        self.associativity = associativity
        self.replacement_policy = replacement_policy
        
        self.num_blocks = capacity // block_size
        self.num_sets = self.num_blocks // associativity
        
        self.hits = 0
        self.misses = 0
        
        self.sets = [[{'valid': False, 'tag': None, 'lru': 0} for _ in range(associativity)] for _ in range(self.num_sets)]
        self.time_counter = 0

    def _decode_address(self, address):
        offset_bits = int(self.block_size.bit_length() - 1)
        set_bits = int(self.num_sets.bit_length() - 1) if self.num_sets > 1 else 0
        
        offset = address & ((1 << offset_bits) - 1)
        temp = address >> offset_bits
        
        set_index = temp & ((1 << set_bits) - 1) if set_bits > 0 else 0
        tag = temp >> set_bits
        
        return tag, set_index, offset

    def access(self, address):
        self.time_counter += 1
        tag, set_index, _ = self._decode_address(address)
        target_set = self.sets[set_index]
        
        for block in target_set:
            if block['valid'] and block['tag'] == tag:
                self.hits += 1
                block['lru'] = self.time_counter
                return True
                
        self.misses += 1
        
        for block in target_set:
            if not block['valid']:
                block['valid'] = True
                block['tag'] = tag
                block['lru'] = self.time_counter
                return False
                
        lru_block = min(target_set, key=lambda x: x['lru'])
        lru_block['tag'] = tag
        lru_block['lru'] = self.time_counter
        return False

    def get_metrics(self):
        total = self.hits + self.misses
        hit_rate = (self.hits / total) * 100 if total > 0 else 0.0
        miss_rate = (self.misses / total) * 100 if total > 0 else 0.0
        
        return {
            "hits": self.hits,
            "misses": self.misses,
            "total_accesses": total,
            "hit_rate": hit_rate,
            "miss_rate": miss_rate
        }

    def reset(self):
        self.hits = 0
        self.misses = 0
        self.time_counter = 0
        self.sets = [[{'valid': False, 'tag': None, 'lru': 0} for _ in range(self.associativity)] for _ in range(self.num_sets)]