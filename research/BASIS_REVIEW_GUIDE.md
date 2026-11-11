# Personal engineering reviewer guide

**Applicant:** Rahul Raj, electronics and communication engineer, Kochi, India.

**Application is personal:** RONICZ is part of the applicant's professional history and the label used for the research. The Basis Fellowship application belongs to Rahul Raj as an individual.

## Where to start

1. [What exists and what does not](EVIDENCE.md).
2. [Programmable compute demonstration](../sim/README.md).
3. [Source with instructions for reproduction](../REPRODUCE.md).
4. [Longer-term engineering questions](OPEN_QUESTIONS.md) and [roadmap](ROADMAP.md).

## Personal track record (historical, separate from this code)

The applicant reports having built an agricultural spraying hexacopter around 2018-19, an experimental self-balancing vehicle and an Arduino Uno-compatible etched PCB. Two user-supplied screenshots of a social post dated 12 February 2019 show an assembled six-motor drone with a liquid tank. These photographs establish an assembled prototype was depicted, but **do not independently prove the flight, spraying performance, authorship or university involvement**. Those statements should remain attributed to the applicant's account unless verified separately.

The current RONICZ GX effort is **new research**, not a continuation of the earlier agricultural engineering project.

## Technical provenance and limitations

The initial 8-lane vector ALU, memory-budget tool and GX-Mini programmable compute demonstrator were prepared with ChatGPT assistance as public research starting points. The applicant has not yet supplied an independently built FPGA core, personally recorded processor demonstration or fabricated GPU. Future personally authored engineering changes should be separately identified with dated commits and test logs.

This repository does **not** prove an original GPU silicon design, manufactured graphics card, 12/24/48 GB VRAM product, Windows driver or measurable performance advantage.

## What a skeptical reviewer can reproduce

- Python model test cases with deterministic input and reference output.
- Functional Verilog testbench runs in GitHub Actions.
- Read the explicit architecture and risk boundaries before inferring hardware capabilities.

**Reason to include this link in Basis:** it is evidence of a current research direction and publicly testable preparatory work. Stronger proof of the applicant's own engineering should come from real project photographs, independently reproducible improvements, and authenticated development history.
