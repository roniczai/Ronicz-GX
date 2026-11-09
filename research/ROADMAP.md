# Public research roadmap: demonstrate first, claim later

This is a sequence of **engineering evidence gates**, not a product launch commitment. Schedule, funding, team and available tools will determine whether each gate can be reached.

## Gate 0 — public research baseline: achieved

- Clearly mark RONICZ GX as a research concept.
- Publish a minimal original 8-lane integer vector ALU and testbench.
- Publish a Python memory-capacity model with tests.
- Document hardware, software, consumer needs and open risks.
- Publish an accessible concept website source.

**Evidence:** successful GitHub Actions tests. Not evidence of GPU hardware.

## Gate 1 — credible compute architecture: planned

- Define and test instruction/control flow, vector-mask behaviour, register file and memory access.
- Develop a software reference implementation with independently checkable outputs.
- Add representative compute kernels and coverage, synthesis reports and resource accounting.
- Publish failures and fixes.

**Exit evidence:** repeatable simulation, design review and implementation limitations.

## Gate 2 — verified FPGA compute demonstration: planned

- Select platform within actual means.
- Implement a host-controlled compute kernel, data transfer, external-memory interface and telemetry.
- Publish a traceable test procedure, exact hardware and reproducible logs.

**Exit evidence:** independent hardware measurement, not only simulation.

## Gate 3 — GPU platform and GX Station prototype feasibility: planned

- Study consumer application software, driver approaches, Windows/WDDM requirements and graphics pipeline.
- Build a GX Station reference *using existing compatible components if necessary*.
- Test system architecture with separate DDR5 and discrete GPU memory.
- Identify licensing, IP, fabrication and maintainability constraints.

**Exit evidence:** honest prototype specification, tested system, validated compatibility matrix.

## Gate 4 — independent graphics hardware and wider access: exploratory long term

- Establish whether original GPU silicon or legally licensed commercial graphics silicon can be manufactured.
- Develop graphics and creator application support with measured, sustainable performance.
- Validate thermals, power, reliability, repairability and regulatory compliance.
- Only announce product availability when these capabilities exist and can be supported.

Projects may pivot or stop at any gate. Consumer affordability remains a **mission to investigate**, never an unverified promise.

