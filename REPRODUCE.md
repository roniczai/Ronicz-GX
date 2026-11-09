# Reproduce the first public RONICZ GX experiments

These are **small learning/research experiments**, not a GPU simulator or real GPU benchmark.

## Python environment

Requires Python 3.10+.

~~~sh
git clone https://github.com/roniczai/Ronicz-GX.git
cd Ronicz-GX
python -m unittest discover -s experiments -p "test_*.py" -v
python experiments/memory_budget.py --vram-gb 24 --parameters-b 14 --bits 4
~~~

The model-weight estimator uses **decimal GB** and excludes many real runtime allocations (e.g., activation space, KV cache, kernel workspace). The fit output does not guarantee an AI model runs.

## RTL simulation

Install \`iverilog\` and \`vvp\` (Icarus Verilog).

~~~sh
iverilog -g2012 -o gx_alu_test rtl/gx_vector_alu.sv rtl/tb_gx_vector_alu.sv
vvp gx_alu_test
~~~

Expected successful message:

~~~text
PASS: 8-lane 32-bit integer vector ALU operations
~~~

This covers only the provided deterministic ALU test vectors, and does **not** establish timing closure, RTL verification completeness, resource/power efficiency, FPGA behaviour or silicon validity.

## Published CI

The same commands run in [the repository workflow](.github/workflows/validate.yml). See [Actions](https://github.com/roniczai/Ronicz-GX/actions) for commit-linked verification results.

## What would strengthen this

Randomized property testing, broader parameterized lanes, boundary/overflow tests, independent reference models, synthesis results, real kernels, and eventually FPGA measurements. Please contribute test cases or reproducible improvements.

