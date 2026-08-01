# Cache Simulator Works

This project models how a CPU cache memory works to make computer programs run faster.

- **Reading Memory Addresses (`trace_reader.py`)**: The system starts by reading a list of memory addresses from a file or a default list. These addresses represent the data that the CPU wants to access.
- **Decoding the Address (`cache.py`)**: When the cache receives a memory address, it splits the address into parts: the **offset**, the **index**, and the **tag**. This helps the system know exactly where to look inside the cache memory.
- **Checking for Hits and Misses (`cache.py`)**:
  - **Hit**: If the requested data is already stored inside the cache, it is a "hit". The CPU gets the data very quickly.
  - **Miss**: If the data is not in the cache, it is a "miss". The system must find space for it, using a replacement policy like **LRU** (Least Recently Used) to remove old data.
- **Comparing Architectures (`main.py`)**: The simulator runs the same memory addresses through two different cache designs: **Direct-Mapped** and **2-Way Set Associative**.
- **Measuring Performance (`metrics.py`)**: Finally, the system calculates the hit and miss rates, prints the results in the console, and creates a visual bar chart to show which cache design performed better.
