# System architecture and CPU choice

## Answer: x86-64 vs Arm

For the first Windows 11 gaming and creator workstation, **x86-64** is the practical host CPU choice for mainstream PC software and driver integration. Intel is a candidate supplier. Arm can be revisited for an appliance-like AI station. **A discrete GPU does not itself need to use the x86 or Arm ISA.** It can implement a purpose-designed GPU instruction and execution architecture.

No CPU vendor partnership is claimed.

## Conceptual system

~~~text
 Windows 11 x86-64 PC                      Proposed discrete graphics card
 ┌───────────────────────────┐    PCIe     ┌───────────────────────────────┐
 │ Intel/AMD host processor  ├────────────┤ PCIe endpoint / DMA / BARs    │
 │ DDR5 system RAM           │            │ Command processor / scheduler │
 │ NVMe / networking / I/O   │            │ Compute execution units      │
 │ WDDM + user-mode driver   │            │ Raster / texture / display   │
 └───────────────────────────┘            │ Dedicated VRAM controller    │
                                          │ GDDR-class memory + cooling  │
                                          └───────────────────────────────┘
~~~

System DDR5 and GPU VRAM are **separate allocations**. Data crosses PCIe as needed. This is not coherent unified memory.

## Minimum subsystems required

- **Compute:** thread/warp scheduling, scalar/vector arithmetic, load/store, cache, memory ordering, synchronization, preemption.
- **Graphics:** shader stages, rasterization, texture sampling/filtering, depth/stencil, blending, render targets, display engine, HDMI/DisplayPort compliance.
- **AI:** supported arithmetic precisions, tensor primitives and a compiler/backend.
- **Memory:** licensed/validated GDDR controller and PHY, ECC policy (if any), addressing, bandwidth and signal integrity.
- **Host:** PCIe controller, DMA, MMU/IOMMU, firmware, enumeration, reset and power management.
- **Software:** assembler/ISA, shader compiler, driver, Vulkan or Direct3D support, WDDM for Windows, kernel/user-mode integration, debugging and update system.
- **Board:** VRM, PDN, thermal solution, fans, safety, EMC/EMI, manufacturing test and reliability verification.
- **Business:** licenses, foundry/OSAT, yield, board assembly, component sourcing, warranty, support and logistics.

## Software strategy

Start with a compute reference model and simple RTL blocks. Investigate open ecosystem interfaces such as Vulkan compute / SPIR-V and open GPU research projects only within their licenses. Full Windows DirectX gaming compatibility is a later, expensive driver and hardware program; do not advertise it as implemented.

## Motherboard support

Target mainstream PCIe x16 systems. PCIe supports backward compatibility, but **"all motherboards" is not testable as a guarantee**. Firmware, electrical power, PCIe lane topology, system chassis, thermal limits, Secure Boot and driver support all require compatibility qualification.

## R&D sequencing

Reference algorithms → RTL components → simulation → FPGA compute prototype → host transport and software → custom silicon feasibility → discrete GPU graphics capabilities → certifications, supply chain, mass production.

