class Memory:
    def __init__(self, size_bytes: int = 65536, latency_cycles: int = 100):
        self.size_bytes = size_bytes
        self.latency_cycles = latency_cycles
        self.ram = bytearray(size_bytes)
        self.total_access_cycles = 0

    def read_block(self, address: int, block_size: int) -> bytes:
        self.total_access_cycles += self.latency_cycles
        start_addr = (address // block_size) * block_size
        return bytes(self.ram[start_addr : start_addr + block_size])

    def write_block(self, address: int, data: bytes, block_size: int):
        self.total_access_cycles += self.latency_cycles
        start_addr = (address // block_size) * block_size
        self.ram[start_addr : start_addr + len(data)] = data

    def read_byte(self, address: int) -> int:
        return self.ram[address % self.size_bytes]

    def write_byte(self, address: int, value: int):
        self.ram[address % self.size_bytes] = value & 0xFF