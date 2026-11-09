# Technical architecture: discrete graphics plus a complete PC

## Design separation

The **GX Card** is a future standalone graphics add-in card. The **GX Station** is a modular Windows-capable desktop using a CPU, motherboard, system memory, storage and a discrete GPU.

A GPU does **not** need to implement x86 or Arm CPU instructions. Its compute execution design and graphics pipeline can be architecturally separate. For the first general-purpose Windows gaming/creator workstation, **x86-64 is the host-CPU preference** due to ecosystem maturity. Intel is one possible host processor supplier; Arm-based stations may be evaluated later. No vendor partnership or processor purchase has been arranged.

~~~text
                     RONICZ GX Station (system concept)
  ┌──────────────────────────────────────────────────────────┐
  │ Commercial x86-64 CPU (initial research preference)      │
  │ Standard DDR5 system RAM (separate and upgradable)       │
  │ Motherboard / UEFI / NVMe / I/O / networking              │
  │ Windows 11 target or Linux research host                 │
  │                         │                                │
  │                    PCIe x16 link                         │
  │                         ▼                                │
  │ ┌──────────────── Proposed GX Card ────────────────────┐ │
  │ │ GPU compute units + thread scheduling + cache       │ │
  │ │ Raster/graphics/display/video blocks (future)      │ │
  │ │ Memory controller / PHY + dedicated GPU VRAM        │ │
  │ │ Board VRM, thermal management, firmware / driver    │ │
  │ └──────────────────────────────────────────────────────┘ │
  └──────────────────────────────────────────────────────────┘
~~~

**System RAM and GPU VRAM are distinct.** PCIe transfers data as needed. This is not the coherent unified memory model of an appliance such as DGX Spark.

## GPU Card workstreams

**Execution:** ISA research, compute instruction scheduling, vector/tensor precision, register file, masking, loads/stores, cache coherence, memory ordering, exceptions and preemption.

**Graphics:** raster pipeline, shader compilation (and legal shader intermediates), vertex/fragment stages, texture sampling, framebuffers, blending, depth/stencil, monitor outputs, refresh and feature capability levels.

**Memory:** capacity, high-speed signalling, GDDR-class controllers, licensed memory PHY, bandwidth, packaging, signal/power integrity and error detection.

**Platform:** PCIe endpoint, DMA, BAR mappings, MMU/IOMMU integration, firmware, reset and clock/power domains, fault reporting.

**Software:** host/runtime API, shader compiler and driver stack. Windows graphics requires WDDM ecosystem compatibility. Vulkan / Direct3D / OpenCL / open AI framework paths require careful separate feasibility studies. **CUDA compatibility is not assumed.**

**Hardware delivery:** RTL-to-ASIC flow, verification, IP licenses, semiconductor fab and packaging, PCB layout, VRM, heatsink/fans, manufacturing tests, compliance and warranty.

## Experiments already available

The repository contains a deliberately small **8-lane 32-bit integer vector ALU** (add, AND, XOR and low-word multiply) with a self-checking RTL testbench. It lacks a scheduler, memory controller, shader pipeline and execution frontend. It is **not a GPU**, not proof of high TFLOPS, and is not ready for fabrication.

The Python VRAM model estimates *weight storage only*; runtime context and overhead are substantial unknowns.

## Compatibility target, not a promise

Aim for broad modern motherboard compatibility through standard interfaces, but literal 'works on all motherboards' is not valid. UEFI, power, PCIe lanes and versions, chassis clearance, thermal constraints and OS drivers require qualification on a published test matrix.

## Research sequence

1. Publish correct reference kernels and RTL components.
2. Implement register file, execution control, memory hierarchy, scheduler and test harness.
3. Run compute workloads on a realistic FPGA platform and instrument performance.
4. Prototype host communications and a reproducible software path.
5. Evaluate feasibility of a real discrete card and graphics APIs.
6. Assemble/test GX Station using existing components while independent GPU development continues.
7. Consider full custom silicon only after cost, team, licensing and validation reviews.

