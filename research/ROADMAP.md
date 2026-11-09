# Engineering roadmap: evidence gates, not delivery promises

## Gate 0 — repository baseline (2026-11-09)

- Record project scope honestly, source links and stage.
- Publish original vector ALU RTL and self-checking simulation.
- Publish memory calculator with its limitations and unit tests.
- Publish a concept-only project webpage.
- **Gate exit:** continuous integration runs test suite successfully.

## Gate 1 — 0–30 days of focused work

- Establish verifiable baseline vector/integer architecture; review open research licenses.
- Add ALU operations, lanes, masking, register file, parameterized tests.
- Study independent memory models and workload characteristics.
- **Gate exit:** test coverage and initial synthesis report.

## Gate 2 — 1–3 months (depends on equipment)

- Select accessible FPGA, simulator and host-interface approach.
- Measure resource use, throughput and power *on a specific hardware platform*.
- Prove one workload end-to-end in a repeatable environment.
- **Gate exit:** archived scripts, waveforms, hardware information and measured report.

## Gate 3 — 3–12+ months

- Develop more GPU-like scheduler/memory hierarchy and compute runtime.
- Prototype PCIe transport, host software and development API.
- Compare time, cost and risk of full original ASIC vs licensed commercial silicon.
- **Gate exit:** architecture review with evidence and realistic budget.

## Gate 4 — multi-year / substantial funding

- License or develop production-ready GPU IP, GDDR controller/PHY, PCIe IP.
- Fabrication, packaging, signal integrity, thermals, board prototype and drivers.
- Rendering, DirectX/Vulkan, video/display, game certification, QA and support.
- **Gate exit:** repeatable independent performance, reliability and economics.

Each gate can end in a pivot or cancellation. This is a research plan, not a guaranteed product launch timeline.

