# RONICZ GX

**An open research initiative toward an independent desktop graphics and AI computing platform.**

> **Status: Research / concept, 9 November 2026.** No RONICZ GPU chip, discrete graphics card, driver, benchmark, or finished workstation is being claimed. Every specification and price below is a goal to investigate, not a shipped capability.

RONICZ GX explores two proposed product directions:

- **GX Card:** a PCIe discrete GPU with dedicated graphics memory for gaming, creative applications, rendering and AI compute.
- **GX Station:** a Windows 11 x86-64 workstation using an Intel-compatible desktop platform, *separate* DDR5 system memory and dedicated GPU VRAM.

The exploratory line-up is **GX 12 / GX 24 / GX 48**, referring to potential **12, 24 and 48 GB of dedicated VRAM**. GDDR7 is a research preference, dependent on eventual silicon, controller, licensing and board feasibility. A **₹250,000 high-end target price** is a commercial hypothesis, not a quote, promise, preorder price, or demonstrated 50% discount.

## What is actually here

- Technical assumptions and open questions in [research/](research/).
- An original, small, **8-lane integer vector ALU RTL experiment** in [rtl/](rtl/). This is *one experimental component*, not a GPU.
- A transparent CPU-executed **VRAM capacity calculator** with tests in [experiments/](experiments/). It does not benchmark GPU hardware.
- A concept-stage responsive [project website](docs/index.html), prepared for GitHub Pages and a future RONICZ subdomain.
- A [validation workflow](.github/workflows/validate.yml).

### Quick start

From the repository root:

~~~bash
python -m unittest discover -s experiments -p "test_*.py" -v
python experiments/memory_budget.py --vram-gb 24 --parameters-b 14 --bits 4
~~~

For RTL simulation, install Icarus Verilog:

~~~bash
iverilog -g2012 -o /tmp/gx_alu rtl/gx_vector_alu.sv rtl/tb_gx_vector_alu.sv
vvp /tmp/gx_alu
~~~

## Project map

| File | Purpose |
| --- | --- |
| [research/PRODUCT.md](research/PRODUCT.md) | Scope, user workloads, success criteria |
| [research/ARCHITECTURE.md](research/ARCHITECTURE.md) | Host CPU, GPU IP, memory, driver, software architecture |
| [research/TARGETS.md](research/TARGETS.md) | Clearly marked aspirational product targets |
| [research/COST.md](research/COST.md) | Cost reality, target-price method and risks |
| [research/ROADMAP.md](research/ROADMAP.md) | Evidence-based development gates |
| [research/RISKS.md](research/RISKS.md) | Engineering and business risk register |
| [research/LOG.md](research/LOG.md) | Timestamped evidence log |
| [research/SOURCES.md](research/SOURCES.md) | Primary-source references |

## Contributing and evidence

Please open an issue describing reproducible experiments, documented technical risks, FPGA/RTL improvements, benchmarks or public standards references. We separate **hypothesis**, **simulation**, **prototype**, **independently measured hardware**, and **commercial product**.

The underlying GitHub repository was created on **4 March 2026** under its prior name, \`rayhan\`. **That date is not a claim that RONICZ GX research began then.** RONICZ GX public research materials were first prepared on **9 November 2026**.

Code and documentation here are published under the [MIT License](LICENSE), except third-party material explicitly identified as otherwise licensed. RONICZ, RONICZ GX and named competitors retain their respective trademarks. This project is independent of NVIDIA, Intel and AMD.

