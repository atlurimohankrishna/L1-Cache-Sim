import time
from collections import OrderedDict
import random
import matplotlib.pyplot as plt

class L1Cache:
    def __init__(self, size_kb, block_size):
        self.size_kb = size_kb
        self.block_size = block_size
        self.cache_size = (size_kb * 1024) // block_size  # Number of blocks in cache
        self.cache = OrderedDict()

    def access(self, address):
        block_number = address // self.block_size
        if block_number in self.cache:
            # Cache hit: Move the block to the end (most recently used)
            self.cache.move_to_end(block_number)
            return True
        else:
            # Cache miss: Add the block to the cache
            if len(self.cache) >= self.cache_size:
                # Evict the least recently used block
                self.cache.popitem(last=False)
            self.cache[block_number] = None
            return False

def simulate_cache(cache_size_kb, block_size, num_accesses, address_range, miss_penalty):
    cache = L1Cache(cache_size_kb, block_size)
    
    hits = 0
    misses = 0

    addresses = [random.randint(0, address_range - 1) for _ in range(num_accesses)]
    start_time = time.time()

    for address in addresses:
        if cache.access(address):
            hits += 1
        else:
            misses += 1

    end_time = time.time()

    hit_rate = hits / num_accesses
    miss_rate = misses / num_accesses
    time_taken = end_time - start_time

    latency = (hits * 1 + misses * miss_penalty) / num_accesses
    throughput = num_accesses / time_taken

    return hit_rate, miss_rate, time_taken, latency, throughput

def simulate_for_cache_sizes(start_kb, end_kb, step_kb, block_sizes, num_accesses, address_range, miss_penalty):
    results = []

    for block_size in block_sizes:
        cache_sizes = list(range(start_kb, end_kb + 1, step_kb))
        for size_kb in cache_sizes:
            hit_rate, miss_rate, time_taken, latency, throughput = simulate_cache(size_kb, block_size, num_accesses, address_range, miss_penalty)
            results.append((size_kb, block_size, hit_rate, miss_rate, time_taken, latency, throughput))
            print(f"Cache Size: {size_kb} KB, Block Size: {block_size} Bytes, Hit Rate: {hit_rate:.2%}, Miss Rate: {miss_rate:.2%}, Time Taken: {time_taken:.4f} seconds, Latency: {latency:.4f}, Throughput: {throughput:.2f} accesses/second")

    return results

def plot_results(results):
    cache_sizes = sorted(list(set(result[0] for result in results)))
    block_sizes = sorted(list(set(result[1] for result in results)))

    for block_size in block_sizes:
        filtered_results = [r for r in results if r[1] == block_size]
        hit_rates = [r[2] for r in filtered_results]
        miss_rates = [r[3] for r in filtered_results]
        latencies = [r[5] for r in filtered_results]
        throughputs = [r[6] for r in filtered_results]

        plt.figure()
        plt.plot(cache_sizes, hit_rates, label="Hit Rate", marker="o")
        plt.plot(cache_sizes, miss_rates, label="Miss Rate", marker="o")
        plt.xlabel("Cache Size (KB)")
        plt.ylabel("Rate")
        plt.title(f"Hit Rate vs Miss Rate (Block Size: {block_size} Bytes)")
        plt.legend()
        plt.grid(True)
        plt.show()

        plt.figure()
        plt.plot(cache_sizes, latencies, label="Latency", marker="o", color="purple")
        plt.xlabel("Cache Size (KB)")
        plt.ylabel("Latency (cycles)")
        plt.title(f"Latency vs Cache Size (Block Size: {block_size} Bytes)")
        plt.legend()
        plt.grid(True)
        plt.show()

        plt.figure()
        plt.plot(cache_sizes, throughputs, label="Throughput", marker="o", color="green")
        plt.xlabel("Cache Size (KB)")
        plt.ylabel("Throughput (accesses/second)")
        plt.title(f"Throughput vs Cache Size (Block Size: {block_size} Bytes)")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    # Configuration
    START_CACHE_SIZE_KB = 2  # Start with 2KB
    END_CACHE_SIZE_KB = 64  # End with 64KB
    STEP_CACHE_SIZE_KB = 2  # Step size of 2KB
    BLOCK_SIZES = [2, 4, 8, 16, 32, 64, 128, 256]  # Varying block sizes
    NUM_ACCESSES = 100000  # Number of memory accesses
    ADDRESS_RANGE = 65536  # Address space range (64KB)
    MISS_PENALTY = 50  # Miss penalty in cycles

    results = simulate_for_cache_sizes(
        START_CACHE_SIZE_KB, END_CACHE_SIZE_KB, STEP_CACHE_SIZE_KB, BLOCK_SIZES, NUM_ACCESSES, ADDRESS_RANGE, MISS_PENALTY
    )

    plot_results(results)





