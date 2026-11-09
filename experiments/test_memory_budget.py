import unittest
from memory_budget import budget, weights_gb


class MemoryBudgetTests(unittest.TestCase):
    def test_weights(self):
        self.assertAlmostEqual(weights_gb(8, 4), 4.0)
        self.assertAlmostEqual(weights_gb(14, 16), 28.0)

    def test_fit(self):
        self.assertTrue(budget(24, 14, 4)["approximate_weight_fit_only"])
        self.assertFalse(budget(12, 14, 16)["approximate_weight_fit_only"])

    def test_reserve(self):
        result = budget(12, 7, 8, overhead_fraction=0, reserve_gb=2)
        self.assertEqual(result["available_after_reserve_gb"], 10)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            weights_gb(-1, 8)
        with self.assertRaises(ValueError):
            budget(0, 7, 4)


if __name__ == "__main__":
    unittest.main()

