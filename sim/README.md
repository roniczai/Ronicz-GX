# GX-Mini v0.1: a verifiable parallel compute research baseline

This is a **small programmable integer processor simulator and matching functional Verilog RTL**, not a working GPU, FPGA implementation or chip.

## What exists

- Four parallel lanes, one common program counter (lockstep).
- Eight 32-bit registers per lane.
- Sixteen local 32-bit memory words per lane and up to sixteen instructions.
- Seven core instruction types: NOP, LDI, ADD, MUL-low32, XOR, LOAD, STORE, HALT.
- A Python functional simulator that decodes and executes an actual instruction stream.
- A Verilog implementation of the same minimal datapath and instruction sequence.
- Python and RTL test cases for multiply-add and 32-bit overflow/XOR.

The supplied multiply-add program performs `output[i] = (a[i] * b[i] + 7) mod 2^32` on four input pairs.

| Lane | a | b | expected/observed |
|---|---:|---:|---:|
| 0 | 2 | 11 | 29 |
| 1 | 3 | 13 | 46 |
| 2 | 5 | 17 | 92 |
| 3 | 7 | 19 | 140 |

These are small **functional test values**, not speed or power benchmarks.

## Run yourself

Requires Python 3.10+. The Python test suite uses the standard library:

```sh
python sim/gx_core.py
python -m unittest discover -s sim -p "test_*.py" -v
```

For Verilog, install Icarus Verilog:

```sh
iverilog -g2012 -o gx_core_test rtl/gx_program_core.sv rtl/tb_gx_program_core.sv
vvp gx_core_test
```

The Verilog testbench uses independently calculated expected outputs. See the GitHub Actions runs for CI execution.

## Engineering limits

- No independent per-lane scheduling or branch divergence.
- No raster pipeline, display output, graphics memory controller, DMA, PCIe, shader compiler or drivers.
- No timing closure, synthesis resource estimates, power measurements or real silicon.
- Data and instruction arrays are loaded by the simulation testbench, not a real host processor.
- The Verilog program ROM is indexed by the low four PC bits; no general instruction-fetch fault logic.
- The Python simulator rejects out-of-range addresses; the Verilog proof assumes the testbench supplies valid addresses.

**Provenance:** This baseline was prepared with ChatGPT assistance and published as research scaffolding. The applicant should execute it independently, inspect the code, make personally attributable changes and record their own results before describing it as personally engineered. Don't submit simulated output as footage of real hardware.

