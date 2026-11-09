# What a technical reviewer can verify today

**Review date: 9 November 2026**

## 1. Original RTL experiment

- [rtl/gx_vector_alu.sv](../rtl/gx_vector_alu.sv): synthesizable-design-style SystemVerilog for eight parallel 32-bit integer lanes.
- Operations: 32-bit wraparound add, AND, XOR, and low 32-bit integer multiply.
- [rtl/tb_gx_vector_alu.sv](../rtl/tb_gx_vector_alu.sv): deterministic self-checking Icarus Verilog simulation.
- **What it demonstrates:** a very small combinational hardware building block passes its targeted functional cases.
- **What it does not demonstrate:** GPU scheduling, graphics pipeline, external-memory operation, power/area/timing, FPGA deployment, custom silicon or TFLOPS throughput.

## 2. Model-weight memory sizing script

- [experiments/memory_budget.py](../experiments/memory_budget.py): decimal GB model-weight estimator with a configurable illustrative overhead and reserve.
- [experiments/test_memory_budget.py](../experiments/test_memory_budget.py): limited Python unit tests.
- **What it demonstrates:** a reproducible arithmetic sizing calculation.
- **What it does not demonstrate:** real GPU VRAM, AI inference, full model fitness or framework compatibility.

## 3. Continuous integration

- [GitHub Actions workflow](../.github/workflows/validate.yml) executes Python and Verilog tests.
- The baseline workflow completed successfully on **9 November 2026**.
- [View workflow runs](https://github.com/roniczai/Ronicz-GX/actions).

## Current evidence boundary

RONICZ GX is a **research initiative with small working examples**, not a commercially implemented GPU architecture. Proposed 12–48 GB VRAM is **not built hardware**. No gaming benchmark, performance-per-watt improvement, thermal claim or production compatibility claim should be inferred.

A judge who prefers completed work should also examine the applicant's **independently verifiable earlier hardware and software projects**, rather than treating this pre-prototype effort as a completed achievement.

## Reproduction

See [REPRODUCE.md](../REPRODUCE.md).

