# What a technical reviewer can verify today

**Review date: 12 November 2026**

## 1. Original RTL experiment

- [rtl/gx_vector_alu.sv](../rtl/gx_vector_alu.sv): synthesizable-design-style SystemVerilog for eight parallel 32-bit integer lanes.
- Operations: 32-bit wraparound add, AND, XOR, and low 32-bit integer multiply.
- [rtl/tb_gx_vector_alu.sv](../rtl/tb_gx_vector_alu.sv): deterministic self-checking Icarus Verilog simulation.
- **What it demonstrates:** a very small combinational hardware building block passes its targeted functional cases.
- **What it does not demonstrate:** GPU scheduling, graphics pipeline, external-memory operation, power/area/timing, FPGA deployment, custom silicon or TFLOPS throughput.

## 2. Programmable parallel compute proof of concept

- [GX-Mini design and reproduction guide](../sim/README.md) documents a 4-lane, 32-bit lockstep integer core with a shared instruction sequence.
- [Python simulator](../sim/gx_core.py) executes seven instruction types plus NOP: load immediate, ADD, MUL, XOR, LOAD, STORE and HALT.
- [RTL prototype](../rtl/gx_program_core.sv) and [simulation testbench](../rtl/tb_gx_program_core.sv) cover vector multiply-add and integer overflow/XOR.
- [Independent Python test suite](../sim/test_gx_core.py) checks program execution, output values and error cases.
- The small example computes output values [29, 46, 92, 140] for four input lanes, with a separate reference calculation.
- **What it demonstrates:** a minimal programmable parallel integer datapath simulated in software and functional RTL, assuming the current tests pass in CI.
- **What it does not demonstrate:** real memory bandwidth, a graphics pipeline, arbitrary programs, timing/power estimates, GPU drivers, FPGA deployment or a silicon implementation.
- **Provenance:** initial code was prepared with ChatGPT assistance. This is an openly documented research scaffold, not evidence the applicant independently engineered every line or already implemented a GPU.

## 3. Model-weight memory sizing script

- [experiments/memory_budget.py](../experiments/memory_budget.py): decimal GB model-weight estimator with a configurable illustrative overhead and reserve.
- [experiments/test_memory_budget.py](../experiments/test_memory_budget.py): limited Python unit tests.
- **What it demonstrates:** a reproducible arithmetic sizing calculation.
- **What it does not demonstrate:** real GPU VRAM, AI inference, full model fitness or framework compatibility.

## 4. Continuous integration

- [GitHub Actions workflow](../.github/workflows/validate.yml) executes Python and Verilog tests.
- The baseline workflow completed successfully on **9 November 2026**.
- [View workflow runs](https://github.com/roniczai/Ronicz-GX/actions).

## Current evidence boundary

RONICZ GX is a **research initiative with small working examples**, not a commercially implemented GPU architecture. Proposed 12–48 GB VRAM is **not built hardware**. No gaming benchmark, performance-per-watt improvement, thermal claim or production compatibility claim should be inferred.

A judge who prefers completed work should also examine the applicant's **independently verifiable earlier hardware and software projects**, rather than treating this pre-prototype effort as a completed achievement.

## Reproduction

See [REPRODUCE.md](../REPRODUCE.md).
