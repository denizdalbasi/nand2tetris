import math


class PlacementPolicy:
    def __init__(self, cache_size_bytes: int, block_size_bytes: int, associativity: int):
        self.cache_size_bytes = cache_size_bytes
        self.block_size_bytes = block_size_bytes
        self.associativity = associativity
        
        self.num_blocks = cache_size_bytes // block_size_bytes
        self.num_sets = self.num_blocks // associativity
        
        self.offset_bits = int(math.log2(block_size_bytes))
        self.index_bits = int(math.log2(self.num_sets))
        self.tag_bits = 32 - (self.offset_bits + self.index_bits)

    def parse_address(self, address: int) -> tuple[int, int, int]:
        offset_mask = (1 << self.offset_bits) - 1
        index_mask = (1 << self.index_bits) - 1
        
        offset = address & offset_mask
        index = (address >> self.offset_bits) & index_mask
        tag = address >> (self.offset_bits + self.index_bits)
        
        return tag, index, offset


class DirectMappedPolicy(PlacementPolicy):
    def __init__(self, cache_size_bytes: int, block_size_bytes: int):
        super().__init__(cache_size_bytes, block_size_bytes, associativity=1)


class SetAssociativePolicy(PlacementPolicy):
    def __init__(self, cache_size_bytes: int, block_size_bytes: int, associativity: int = 2):
        super().__init__(cache_size_bytes, block_size_bytes, associativity=associativity)