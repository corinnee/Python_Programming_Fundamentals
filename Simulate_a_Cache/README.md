
# Cache Simulation Project

This repository contains a cache simulation program that simulates a hardware cache with k-way associativity and LRU (Least Recently Used) replacement strategy. This project is part of the Operating Systems assessment (A3) at UKC.

## Table of Contents
- [Introduction](#introduction)
- [Project Description](#project-description)
  - [Purpose](#purpose)
- [How to Use the Program](#how-to-use-the-program)
- [Technologies Used](#technologies-used)
- [Example Files](#example-files)

## Introduction

The cache simulation program in this repository allows you to simulate a hardware cache with specific characteristics, such as the number of bits in one word (W), the number of data bytes in the cache (C), the number of bytes in one cache block (B), and the number of lines in a block (k). The program reads a list of memory accesses and determines whether each access is served by the cache or by the main memory.

## Project Description
The cache simulation program is designed to mimic the behaviour of a hardware cache, allowing you to experiment with different cache configurations and memory access patterns. It implements the LRU replacement strategy to manage cache entries

### Purpose
The purpose of this project was to demonstrate a practical understanding of how hardware caches work and how cache simulations can help analyse memory access patterns. The [Operating_Systems_A3.pdf](./Operating_Systems_A3.pdf) is the full assessment brief that was given by the university.

## How to Use the Program

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/corinnee/Python_Programming_Fundamentals.git
   ```

2. Navigate to the project sub directory:

  ```bash
  cd Python_Programming_Fundamentals/Simulate_a_Cache
  ```
   
3. Run the cach simulation program with your input files, You can create your input file or use the provided example files (see 4_way_associative_input.txt and larger_direct_mapped_input.txt)

```bash
python cache.py < input_file.txt
```

 4. The program will simulate the cache based on the input and display the results, indicating whether each memory access is served by the cache (C) or main memory (M).
