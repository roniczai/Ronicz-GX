# Product brief — exploratory, not a specification

**Research date:** 2026-11-09

## Mission

Investigate whether a small team can make credible progress toward a **high-VRAM, efficient, desktop-class** graphics and compute product that supports **AI, gaming, rendering, 3D CAD and creative workflows** at a comparatively accessible price.

There are two separate products, not one confused processor:

1. **RONICZ GX Card:** proposed PCIe add-in card using original or legally licensed graphics silicon, local GDDR-class VRAM, cooling, power delivery, firmware and drivers.
2. **RONICZ GX Station:** proposed compact tower / workstation built around a **commercial x86-64 processor (initial preference Intel)**, ordinary DDR5 system DIMMs, a GPU add-in card, NVMe storage and Windows 11. It is not a unified-memory DGX Spark clone.

## Why users might care

- Creators need useful 3D rendering and video performance.
- AI practitioners may need **more dedicated VRAM** for local models and larger workloads.
- PC gamers need graphics API compatibility and reliable drivers.
- Workstation customers care about reliability, noise, heat, serviceability and software support.
- Price-sensitive buyers value the **total system cost**, not TFLOPS claims alone.

## Non-negotiable evidence standards

- No GPU silicon, PCB, driver or full GPU benchmarks exist yet.
- A vector ALU RTL file is **not** evidence of a complete GPU.
- Target VRAM is **not** present hardware.
- The marketing price is **not** a bill-of-materials estimate or committed selling price.
- Workloads and FPS must not be advertised until independently reproduced.

## Near-term deliverable

Implement and verify a small RTL compute block, create a simple public numerical model, and develop an explicit verification plan for future FPGA work.

## Product acceptance milestones

1. Correct simulation tests in CI.
2. Synthesizable, verified components with documented assumptions.
3. FPGA prototype executing a defined compute kernel with external memory.
4. Host interface and driver proof-of-concept with reproducible telemetry.
5. Graphics pipeline and API compatibility tests, only after compute functionality is demonstrated.
6. Costed hardware design and manufacturer quotes, before making retail-price claims.

