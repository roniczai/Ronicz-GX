"""Functional tests of GX-Mini toy instruction set and lane arithmetic."""
import unittest
from gx_core import (
    Core, encode, MASK32, OP_LDI, OP_ADD, OP_MUL, OP_XOR,
    OP_LOAD, OP_STORE, OP_HALT,
)


class CoreTests(unittest.TestCase):
    def test_vector_multiply_add(self):
        a, b = [2, 3, 5, 7], [11, 13, 17, 19]
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
        for lane in range(4):
            core.memory[lane][0], core.memory[lane][1] = a[lane], b[lane]
        core.run()
        self.assertEqual([core.memory[i][2] for i in range(4)], [29, 46, 92, 140])
        self.assertEqual(len(core.trace), len(program))
        self.assertTrue(core.halted)

    def test_integer_wrap_and_xor(self):
        core = Core(program=[
            encode(OP_LOAD, rd=0, imm=0),
            encode(OP_LOAD, rd=1, imm=1),
            encode(OP_ADD, rd=2, ra=0, rb=1),
            encode(OP_XOR, rd=3, ra=2, rb=1),
            encode(OP_STORE, rd=3, imm=2),
            encode(OP_HALT),
        ])
        vals = [MASK32, 0, 6, 0x80000000]
        for lane, a in enumerate(vals):
            core.memory[lane][0] = a
            core.memory[lane][1] = 2
        core.run()
        expected = [((a + 2) & MASK32) ^ 2 for a in vals]
        self.assertEqual([core.memory[l][2] for l in range(4)], expected)

    def test_halt_and_bounds(self):
        core = Core([encode(OP_HALT)])
        core.run()
        with self.assertRaises(RuntimeError):
            core.step()
        with self.assertRaises(ValueError):
            Core([encode(OP_LOAD, imm=31), encode(OP_HALT)]).run()
        with self.assertRaises(RuntimeError):
            Core([encode(OP_LDI, rd=1, imm=5)]).run(max_steps=4)
        with self.assertRaises(ValueError):
            encode(OP_ADD, rd=8)
        with self.assertRaises(ValueError):
            Core([0xD000]).run()


if __name__ == "__main__":
    unittest.main()

