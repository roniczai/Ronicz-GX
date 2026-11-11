"""GX-Mini v0.1: educational 4-lane lockstep integer processor simulator.

This is a small functional simulation, not a GPU, graphics pipeline,
cycle-accurate hardware model, FPGA image, or manufactured device.
AI-assisted research baseline: independently reproduce and review before
claiming personal implementation or physical hardware results.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Sequence

LANES = 4
REGS = 8
WORDS_PER_LANE = 16
MASK32 = (1 << 32) - 1

OP_NOP = 0
OP_LDI = 1
OP_ADD = 2
OP_MUL = 3
OP_XOR = 4
OP_LOAD = 6
OP_STORE = 7
OP_HALT = 15


def encode(op: int, rd: int = 0, ra: int = 0, rb: int = 0, imm: int = 0) -> int:
    """Encode a 16-bit toy instruction; rd is also STORE's source register."""
    if not (0 <= op < 16 and 0 <= rd < REGS and 0 <= ra < REGS
            and 0 <= rb < REGS and 0 <= imm < 256):
        raise ValueError("invalid instruction field")
    ins = (op << 12) | (rd << 9)
    if op in (OP_LDI, OP_LOAD, OP_STORE):
        return ins | imm
    return ins | (ra << 6) | (rb << 3)


@dataclass
class Core:
    program: Sequence[int]
    memory: list[list[int]] = field(default_factory=lambda: [
        [0] * WORDS_PER_LANE for _ in range(LANES)
    ])
    registers: list[list[int]] = field(default_factory=lambda: [
        [0] * REGS for _ in range(LANES)
    ])
    pc: int = 0
    halted: bool = False
    trace: list[dict] = field(default_factory=list)

    def __post_init__(self) -> None:
        if len(self.memory) != LANES or any(len(m) != WORDS_PER_LANE for m in self.memory):
            raise ValueError("memory must be 4 x 16 words")
        if not self.program or len(self.program) > 16:
            raise ValueError("program must contain 1-16 instructions")
        if any(not isinstance(ins, int) or not 0 <= ins <= 0xFFFF for ins in self.program):
            raise ValueError("instructions must be 16-bit integers")

    def step(self) -> None:
        if self.halted:
            raise RuntimeError("already halted")
        if not 0 <= self.pc < len(self.program):
            raise RuntimeError("program counter outside instruction memory")
        ins = self.program[self.pc]
        op, rd, ra, rb = (ins >> 12) & 15, (ins >> 9) & 7, (ins >> 6) & 7, (ins >> 3) & 7
        imm = ins & 255
        if op not in (OP_NOP, OP_LDI, OP_ADD, OP_MUL, OP_XOR, OP_LOAD, OP_STORE, OP_HALT):
            raise ValueError(f"unknown opcode 0x{op:x}")
        if op in (OP_LOAD, OP_STORE) and imm >= WORDS_PER_LANE:
            raise ValueError("memory address out of range")
        self.trace.append({"pc": self.pc, "opcode": op, "instruction": f"0x{ins:04x}"})
        for lane in range(LANES):
            r = self.registers[lane]
            if op == OP_LDI:
                r[rd] = imm
            elif op == OP_ADD:
                r[rd] = (r[ra] + r[rb]) & MASK32
            elif op == OP_MUL:
                r[rd] = (r[ra] * r[rb]) & MASK32
            elif op == OP_XOR:
                r[rd] = r[ra] ^ r[rb]
            elif op == OP_LOAD:
                r[rd] = self.memory[lane][imm]
            elif op == OP_STORE:
                self.memory[lane][imm] = r[rd]
        if op == OP_HALT:
            self.halted = True
        else:
            self.pc += 1

    def run(self, max_steps: int = 32) -> None:
        for _ in range(max_steps):
            if self.halted:
                return
            self.step()
        if not self.halted:
            raise RuntimeError("program did not halt within step limit")


def demo() -> None:
    """Run vector multiply-add on four independently stored lane inputs."""
    a = [2, 3, 5, 7]
    b = [11, 13, 17, 19]
    program = [
        encode(OP_LOAD, rd=1, imm=0),
        encode(OP_LOAD, rd=2, imm=1),
        encode(OP_MUL, rd=3, ra=1, rb=2),
        encode(OP_LDI, rd=4, imm=7),
        encode(OP_ADD, rd=5, ra=3, rb=4),
        encode(OP_STORE, rd=5, imm=2),
        encode(OP_HALT),
    ]
    core = Core(program=program)
    for lane in range(LANES):
        core.memory[lane][0] = a[lane]
        core.memory[lane][1] = b[lane]
    core.run()
    actual = [core.memory[lane][2] for lane in range(LANES)]
    expected = [(a[lane] * b[lane] + 7) & MASK32 for lane in range(LANES)]
    print("RONICZ GX-Mini v0.1 | SOFTWARE SIMULATION ONLY")
    for item in core.trace:
        print(f"PC={item['pc']:02d}  instruction={item['instruction']}  opcode={item['opcode']}")
    print(f"A:        {a}")
    print(f"B:        {b}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    if actual != expected:
        raise AssertionError("core result does not match independent reference")
    print("PASS: all four lanes match independent Python calculation")


if __name__ == "__main__":
    demo()

