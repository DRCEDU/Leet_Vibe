# Data Science: From School to Work, Part V  
**How to profile your Python project**  
*Vincent Margot, June 26, 2025*  
[Read the original article](https://towardsdatascience.com/data-science-from-school-to-work-part-v/)

---

> _Make it work, then make it beautiful, then if you really, really have to, make it fast. 90 percent of the time, if you make it beautiful, it will already be fast. So really, just make it beautiful!_  
> — Joe Armstrong (co-designer of Erlang)

This article is the final part of a series on Python for data science, focusing on **profiling**: tracking and optimizing your code’s performance (memory, time, CPU/GPU). Profilers help identify bottlenecks and resource-heavy code.

---

## I. Memory Profilers

### 1. `memory_profiler`

- **Install:**  
  ```bash
  pip install memory_profiler
  # or with uv
  uv add memory_profiler
  ```

- **Executable Profiling:**  
  Use `mprof` to monitor any executable’s memory usage.
  ```bash
  mprof run ollama run gemma3:4b
  mprof plot
  # or with uv
  uv run mprof run ollama run gemma3:4b
  uv run mprof plot
  ```
  *Figure: Output of `mprof plot` shows a memory usage graph over time.*

- **Python Code Profiling:**  
  Decorate functions with `@profile` and run with the memory profiler.
  ```python
  @profile
  def my_func():
      a = [1] * (10 ** 6)
      b = [2] * (2 * 10 ** 7)
      del b
      return a

  if __name__ == '__main__':
      my_func()
  ```
  Run:
  ```bash
  python -m memory_profiler monitoring.py
  # or
  uv run -m memory_profiler monitoring.py
  ```
  *Output: Table with columns for line number, memory usage, increment, occurrences, and line contents.*

  > **Note:** `memory_profiler` is no longer actively maintained.

### 2. `tracemalloc`

- **Built-in Python module** for tracking memory allocations.
- Provides traceback for allocations, statistics by file/line, and snapshot comparisons.
- Useful for identifying memory leaks.
- *See referenced articles for detailed usage.*

---

## II. Time Profilers

### 1. `line_profiler`

- **Install:**  
  ```bash
  pip install line_profiler
  # or
  uv add line_profiler
  ```

- **Usage:**  
  Decorate functions with `@profile` and run with `kernprof`.
  ```python
  @profile
  def create_list(lst_len: int):
      arr = []
      for i in range(0, lst_len):
          arr.append(i)

  def print_statement(idx: int):
      if idx == 0:
          print("Starting array creation!")
      elif idx == 1:
          print("Array created successfully!")
      else:
          raise ValueError("Invalid index provided!")

  @profile
  def main():
      print_statement(0)
      create_list(400000)
      print_statement(1)

  if __name__ == "__main__":
      main()
  ```
  Run:
  ```bash
  kernprof -lv monitoring.py
  # or
  uv run kernprof -lv monitoring.py
  ```
  *Output: Tables per function with line number, hits, time, per-hit time, and code.*

---

## III. CPU/GPU Profilers

### 1. `cProfile`

- **Built-in Python module** for function-level profiling.
- Use with `snakeviz` for visualization.
  ```bash
  pip install snakeviz
  python -m cProfile -o output.prof your_script.py
  snakeviz output.prof
  ```
  *Figure: Snakeviz provides a graphical view of function call times.*

### 2. `Scalene`

- **Install:**  
  ```bash
  pip install scalene
  # or
  uv add scalene
  ```

- **Features:**  
  - Profiles CPU, GPU, and memory.
  - Line-level and function-level profiling.
  - CLI and web interface.
  - AI-powered optimization suggestions (supports OpenAI, BedRock, Azure, Ollama).

- **Example script:**
  ```python
  import random
  import math
  import numpy as np
  import cupy as cp

  def memory_waster():
      memory_hogs = []
      for _ in range(10):
          memory_copy = [random.random() for _ in range(10**6)]
          memory_hogs.append(memory_copy)
      return memory_hogs

  def cpu_waster():
      meaningless_result = 0
      for i in range(10000):
          for j in range(10000):
              temp = (i**2 + j**2) * random.random()
              temp = temp / (random.random() + 0.01)
              temp = abs(temp**0.5)
              meaningless_result += temp
              angle = random.random() * math.pi
              temp += math.sin(angle) * math.cos(angle)
          if i % 100 == 0:
              random_mess = [random.randint(1, 1000) for _ in range(1000)]
              random_mess.sort()
              random_mess.reverse()
              random_mess.sort()
      return meaningless_result

  def gpu_convolution():
      image_size = 128
      kernel_size = 64
      image = np.random.random((image_size, image_size)).astype(np.float32)
      kernel = np.random.random((kernel_size, kernel_size)).astype(np.float32)
      image_gpu = cp.asarray(image)
      kernel_gpu = cp.asarray(kernel)
      result = cp.zeros_like(image_gpu)
      for y in range(kernel_size // 2, image_size - kernel_size // 2):
          for x in range(kernel_size // 2, image_size - kernel_size // 2):
              pixel_value = 0
              for ky in range(kernel_size):
                  for kx in range(kernel_size):
                      iy = y + ky - kernel_size // 2
                      ix = x + kx - kernel_size // 2
                      pixel_value += image_gpu[iy, ix] * kernel_gpu[ky, kx]
              result[y, x] = pixel_value
      result_cpu = cp.asnumpy(result)
      cp.cuda.Stream.null.synchronize()
      return result_cpu

  def main():
      print("\n1/ Wasting some memory (controlled)...")
      _ = memory_waster()
      print("\n2/ Wasting CPU cycles (controlled)...")
      _ = cpu_waster()
      print("\n3/ Wasting GPU cycles (controlled)...")
      _ = gpu_convolution()

  if __name__ == "__main__":
      main()
  ```

- **Install `cupy` for GPU profiling:**  
  ```bash
  pip install cupy-cuda12x
  # or
  uv add install cupy-cuda12x
  ```

- **Run Scalene:**  
  ```bash
  scalene scalene_tuto.py
  # or
  uv run scalene scalene_tuto.py
  ```
  - Use `--cli` for command-line output.
  - *Figure: Scalene CLI output uses color codes for CPU (blue), memory (green), and GPU (yellow).*
  - *Web interface provides a big-picture view and line-level details, with icons for optimizable code.*

- **AI Suggestions:**  
  - Scalene can suggest optimizations using AI models (OpenAI, BedRock, Azure, Ollama).
  - *Note: AI-generated optimizations may not always be correct.*

---

## Conclusion

Profiling is essential for identifying and optimizing resource-heavy code.  
- `memory_profiler` and `line_profiler` are easy to set up and provide detailed, readable reports.
- `cProfile` and `Scalene` offer comprehensive profiling and visualization, with Scalene adding AI-powered suggestions.
- Regular profiling helps avoid performance issues and unnecessary hardware upgrades.

---

**For more details, code, and figures, see the full article:**  
[Data Science: From School to Work, Part V](https://towardsdatascience.com/data-science-from-school-to-work-part-v/) 