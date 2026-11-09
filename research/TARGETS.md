# Product directions and proposed validation criteria

**These are exploratory goals, not product specifications, benchmark claims or configurations available to buy.**

| Goal | GX 12 | GX 24 | GX 48 |
|---|---|---|---|
| Dedicated graphics-memory capacity | 12 GB | 24 GB | 48 GB |
| Intended usage lens | Mainstream gaming / creators | Creators / gaming / local AI | High-memory creator and enthusiast work |
| GPU memory technology | To investigate; GDDR-class | To investigate; GDDR-class | To investigate; GDDR-class |
| Host interface | PCIe add-in card goal | PCIe add-in card goal | PCIe add-in card goal |
| Gaming graphics pipeline | Not implemented | Not implemented | Not implemented |
| Rendering and video engines | Not implemented | Not implemented | Not implemented |
| AI compute software stack | Not implemented | Not implemented | Not implemented |
| Windows drivers | Not implemented | Not implemented | Not implemented |
| Power, thermals and acoustics | Not measured | Not measured | Not measured |
| Memory bandwidth and compute | Unknown | Unknown | Unknown |
| Hardware availability | None | None | None |

Theoretical throughput, feature support, power draw and memory-chip configuration cannot be responsibly specified until the architecture is validated. Higher VRAM does not automatically imply higher graphics performance.

## Complete GX Station: proposed feature scope

- Commercial x86-64 CPU, initially evaluating mainstream Intel-compatible hardware.
- User-upgradable **DDR5 system RAM**, physically separate from GPU VRAM.
- Discrete add-in graphics card with locally attached VRAM.
- Standard NVMe storage, modern networking, appropriate USB/display connectivity.
- Windows 11 usability target and Linux research option.
- Serviceable thermal and power systems, diagnostics and sensible acoustics.
- Games, 3D applications, rendering, local AI and everyday desktop software as user test categories.

## Future acceptance testing

Report **actual measured** FPS and frame times under stated game presets, Blender scene/version render times, model tokens/s and end-to-end memory footprint, measured wall/board power under load, thermal stability, fan noise, driver quality, crash rates and the exact tested system configuration.

Compare equivalent precision and workload settings; do not mix different vendor theoretical FLOPS numbers. No comparisons or parity claims are currently supported by evidence.

