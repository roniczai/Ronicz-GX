# RONICZ GX
### A personal-computing initiative: powerful graphics and AI tools should be within reach of more people.

[![Research validation](https://github.com/roniczai/Ronicz-GX/actions/workflows/validate.yml/badge.svg)](https://github.com/roniczai/Ronicz-GX/actions/workflows/validate.yml)
![Stage](https://img.shields.io/badge/stage-research%20concept-7789d8)
![License](https://img.shields.io/badge/code%20license-MIT-7386c6)

**An independent, public R&D project from RONICZ Technovationz Pvt. Ltd., Kochi, India.**

> **Research status, 9 November 2026:** A working **8-lane integer vector-ALU simulation** and tested Python memory-budgeting tool are available here. **No RONICZ GPU silicon, graphics card, FPGA demonstrator, Windows GPU driver, production motherboard or finished workstation has been built.** Memory variants, performance, efficiency and compatibility remain proposed goals, not specifications or product announcements.

## Why this exists

Personal computers once gave individuals tools previously reserved for institutions. Today, local AI, advanced 3D, gaming, content creation and simulation increasingly demand computational resources that many learners and independent creators struggle to access.

**Our goal is to explore how more people might own, upgrade, repair and use serious computing power.**

We are not building only for enterprise buyers. The primary design lens is the **person at a desk**: the student, gamer, maker, developer, animator, researcher, photographer or small-business operator who wants to create without depending entirely on rented compute.

This is an **accessibility ambition**, not a claim that cheaper products or improved social outcomes have already been demonstrated.

## Two connected product tracks

| Research track | Proposed direction | Current stage |
|---|---|---|
| **RONICZ GX Card** | Discrete PCIe graphics/compute card family for gaming, AI, rendering and creation, with **12 GB, 24 GB or 48 GB** of proposed dedicated VRAM | Architecture exploration only |
| **RONICZ GX Station** | Complete modular desktop workstation with a **commercial x86-64 CPU**, separate DDR5 system RAM, discrete graphics VRAM, storage, cooling and Windows compatibility goals | System concept only |

The proposed **GX 12 / GX 24 / GX 48** names indicate **memory-capacity targets**, not actual cards. GDDR-class graphics memory, potentially GDDR7, depends on feasible controllers, PHY IP, packaging and board development. CPU choice initially favors mainstream x86-64 compatibility; no processor-vendor agreement is claimed.

## What could distinguish it? Research hypotheses, not established inventions

1. **Useful performance per watt:** investigate sustained real-workload throughput, thermals and acoustics, not only peak theoretical FLOPS.
2. **Dedicated memory for local work:** explore 12–48 GB GPU-memory options while keeping system RAM separate and user-upgradable.
3. **Consumer-first software:** aim for real-world Windows gaming, creative software, rendering and open AI workflows; software compatibility remains one of the largest obstacles.
4. **Repairable, modular ownership:** evaluate replaceable cooling parts, documented system service procedures and upgrade paths.
5. **Public, falsifiable engineering:** publish assumptions, source references, tests, limitations and failures.

These ideas are **design goals**. They have not been established as novel, patentable or commercially feasible. Researching another company's proprietary GPU design is not a license to copy its IP.

## What we have actually produced

- [Original 8-lane integer vector ALU RTL](rtl/gx_vector_alu.sv), with [self-checking simulation testbench](rtl/tb_gx_vector_alu.sv).
- [Small Python model-weight memory estimator](experiments/memory_budget.py), with [unit tests](experiments/test_memory_budget.py). It is not a GPU benchmark or proof of actual VRAM performance.
- [Automated Python and RTL validation](.github/workflows/validate.yml). See the GitHub Actions results.
- [Full architecture and research questions](research/ARCHITECTURE.md).
- [Project website source](docs/index.html) for a future GitHub Pages/custom-domain deployment.

**Reproduce the experiments** using [REPRODUCE.md](REPRODUCE.md).

## Evidence ladder

| Stage | Evidence required | Status |
|---|---|---|
| Small architectural building blocks | Source code, self-checking tests, repeatable outputs | **Initial experiments published** |
| GPU-like compute architecture | Scheduler, register/memory hierarchy, executable kernels | **Not demonstrated** |
| FPGA proof of concept | Specified FPGA board, synthesis, workload measurements | **Not built** |
| Discrete GPU + graphics stack | Hardware, PCIe, memory, rendering pipeline, drivers | **Not built** |
| GX Station | Assembly, OS validation, component compatibility, thermal testing | **Not built** |

## Read the project

- [Public-interest mission and measurable access outcomes](research/MISSION.md)
- [Consumer-first product definition](research/PRODUCT.md)
- [CPU, discrete GPU and Windows architecture](research/ARCHITECTURE.md)
- [Aspirational GX 12 / 24 / 48 targets](research/TARGETS.md)
- [Hardware, software and verification roadmap](research/ROADMAP.md)
- [Open design questions](research/OPEN_QUESTIONS.md)
- [Engineering and adoption risks](research/RISKS.md)
- [Current technical evidence](research/EVIDENCE.md)
- [Research log](research/LOG.md)
- [References](research/SOURCES.md)

## Contribute

We welcome documented technical corrections, simulator improvements, hardware verification ideas, test programs and software compatibility research. See [CONTRIBUTING.md](CONTRIBUTING.md).

**Research is not a preorder, product reservation or promise of release.** RONICZ GX is independent of NVIDIA, Intel, AMD, Microsoft and other named vendors.

## Transparent project chronology

This GitHub repository was originally created **4 March 2026** under the name \`rayhan\` for an unrelated project. It was renamed and repurposed for public RONICZ GX research on **9 November 2026**. Repository creation date is not the GPU project's start date.

© 2026 RONICZ Technovationz Pvt. Ltd. Code and original documentation are made available under [MIT](LICENSE), except third-party material as separately licensed.

