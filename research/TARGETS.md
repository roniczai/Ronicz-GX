# Aspirational target matrix — not tested or announced specifications

| Attribute | GX 12 | GX 24 | GX 48 |
|---|---|---|---|
| Dedicated VRAM **goal** | 12 GB | 24 GB | 48 GB |
| Preferred technology to **investigate** | GDDR7 | GDDR7 | GDDR7 |
| Usage hypothesis | Gaming / creator | AI / 3D / creator | Large local models / rendering |
| Physical interface goal | PCIe x16 | PCIe x16 | PCIe x16 |
| Windows driver | Not developed | Not developed | Not developed |
| GPU architecture | Not determined | Not determined | Not determined |
| TDP / board power | TBD | TBD | TBD |
| Memory bandwidth | TBD | TBD | TBD |
| Compute throughput | TBD | TBD | TBD |
| Ray tracing | Feasibility study | Feasibility study | Feasibility study |
| Cooling | Thermal modelling required | Thermal modelling required | Thermal modelling required |
| Target retail price | Unset | Unset | **At most ₹250,000, conditional** |
| Commercial availability | None | None | None |

These configurations are targets; GPU memory interface width and chip count are deliberately **not specified** before deciding on a memory controller, package and PCB feasibility.

## GX Station concept

- Host: commercial x86-64 Intel-compatible platform, with actual Intel CPU selection later.
- RAM: separate 32/64/128 GB DDR5 configurations to evaluate, not a product offering.
- GPU: a future discrete RONICZ GX add-in card with local VRAM.
- OS: Windows 11 Pro target; Linux research environment may be easier for early work.
- Storage: NVMe SSD.
- Power, cooling, size and system price: **not yet established**.
- Important: ₹250,000 is the high-end **card** target, **not** a priced fully built workstation.

## Benchmark protocol (future)

Publish real game settings and FPS distributions; Blender Benchmark scene/version and render time; 3D application tasks; FP32/FP16/BF16/INT8 compute with methodology; AI model/inference tokens/s and memory use; wall power and board power; sustained thermal and acoustical data at stated ambient conditions.

Do not compare NVIDIA FP4 sparse theoretical AI FLOPS to another device's FP32 FLOPS as though equivalent.

