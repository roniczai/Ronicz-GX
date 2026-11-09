# Product concept: an individual-first graphics ecosystem

**Stage:** Pre-prototype architecture research.

## 1. RONICZ GX Card

Potential family names: **GX 12**, **GX 24**, **GX 48**, referring to **12 / 24 / 48 GB dedicated graphics memory goals**.

Intended consumer workloads: PC gaming, Blender and related 3D workflows, CAD/visualization, video and content creation, graphics programming, local AI inference and experimental scientific compute.

Required investigation includes real graphics pipelines, rasterization, shader compilation, display output, video engines, tensor/vector compute, PCIe and memory controllers, Windows kernel/user drivers, application validation, cooling and reliability.

**A card cannot become a full NVIDIA competitor merely by increasing VRAM.** The entire graphics software ecosystem matters.

## 2. RONICZ GX Station

A proposed **complete personal computer**, rather than an AI-only box.

- A commercial x86-64 host CPU (Intel platform a first candidate, no affiliation implied).
- **Standard desktop DDR5 system RAM** on a suitable motherboard.
- A discrete GX GPU with its own separate VRAM, if developed.
- NVMe storage, network connectivity, ports, appropriate power delivery and a maintainable cooling system.
- Windows 11 compatibility goal, alongside Linux research support.
- User-facing workloads spanning gaming, 3D, design, local AI, rendering and ordinary desktop computing.
- No unified-memory architecture proposed for this initial form factor.

A working GX Station concept may initially need to use a **licensed or existing third-party GPU** for system integration testing. That would not mean RONICZ has built its own GPU.

## Principles

**Consumer first.** Individuals, learning communities and independent studios are the primary design center; SMB buyers are welcome.

**Ownable and upgradeable.** Investigate standard PC components, good serviceability and long-lived driver support.

**Measured efficiency.** Real sustained workloads, frame times, inference throughput, wattmeter or validated board sensors, noise and thermal conditions.

**Independence without exaggeration.** No proprietary architecture cloning, unlicensed IP reuse, fictional results, 'works on all motherboards' guarantees or premature product preorder.

## Unresolved choices

Original GPU ASIC versus licensing, processor and motherboard model, memory bus width and packaging, fabrication feasibility, Windows driver scope, gaming API approach, certification and the economic viability of manufacturing.

## Current deliverables

A tiny original RTL ALU experiment, simple model-weight memory estimator, unit/RTL tests, documentation and a concept website. None of these amount to an integrated GPU system.

