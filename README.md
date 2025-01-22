# L1 Cache Performance Simulation

This repository contains a Python-based simulation tool designed to evaluate and analyze the performance of an L1 cache under varying configurations. The project provides insights into how cache size and block size influence critical metrics such as hit rate, miss rate, latency, and throughput.

---

## Features

1. **Cache Simulation**:
   - Implements a configurable L1 cache using the Least Recently Used (LRU) replacement policy.
   - Simulates realistic memory accesses with random address generation.

2. **Dynamic Configuration**:
   - Supports cache sizes ranging from 2KB to 64KB.
   - Allows block size variations of 32, 64, and 128 bytes.
   - Configurable number of memory accesses and address space.

3. **Performance Metrics**:
   - Calculates hit rate, miss rate, access latency, throughput, and miss penalty.
   - Provides a comprehensive analysis of cache performance.

4. **Data Visualization**:
   - Generates comparative plots for hit rate, miss rate, latency, and throughput.
   - Visualizes the impact of cache and block size configurations on system performance.

---

## How It Works

1. **L1 Cache Simulation**:
   - Simulates the cache as an `OrderedDict` for efficient LRU operations.
   - Tracks hits and misses during memory access simulation.

2. **Metric Calculation**:
   - Computes performance metrics based on hits, misses, and configurable miss penalties.
   - Measures overall latency and throughput for different cache configurations.

3. **Visualization**:
   - Utilizes Matplotlib to create clear and insightful plots for comparing performance across cache sizes and block sizes.

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/l1-cache-simulation.git
   cd l1-cache-simulation
   ```

2. Run the script:
   ```bash
   python l1_cache_simulation.py
   ```

3. Customize configurations:
   - Modify parameters like `cache size`, `block size`, `number of accesses`, and `miss penalty` in the `main` section of the script.

---

## Outputs

- **Hit Rate vs Miss Rate**: Evaluates cache efficiency for different configurations.
- **Latency Analysis**: Shows the trade-off between latency and cache size.
- **Throughput Analysis**: Highlights how throughput changes with cache configurations.

---

## Applications

- **Educational Tool**: Demonstrates cache design concepts for students and educators.
- **Performance Optimization**: Provides insights for engineers to optimize cache performance.
- **Research and Analysis**: Offers a foundation for exploring advanced caching mechanisms.

---

Feel free to fork the repository, experiment with configurations, and contribute enhancements!
