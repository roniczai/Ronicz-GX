"""Simple model-weight VRAM budgeting, not GPU hardware simulation or benchmark.

The estimate counts quantized weights plus an optional fractional overhead.
It omits KV cache, activations, kernel workspace, fragmentation, driver
reservations and runtime-specific overheads. Real deployments may need much more.
All displayed capacity quantities here use decimal GB (10^9 bytes).
"""
from __future__ import annotations
import argparse


def weights_gb(parameters_b: float, bits_per_weight: float) -> float:
    """Decimal GB of raw model weights at nominal bits per parameter."""
    if parameters_b <= 0 or bits_per_weight <= 0:
        raise ValueError("parameters and precision must be positive")
    return parameters_b * bits_per_weight / 8.0


def budget(vram_gb: float, parameters_b: float, bits: float,
           overhead_fraction: float = 0.20, reserve_gb: float = 2.0) -> dict:
    if vram_gb <= 0 or reserve_gb < 0 or overhead_fraction < 0:
        raise ValueError("invalid memory budget")
    base = weights_gb(parameters_b, bits)
    estimated = base * (1 + overhead_fraction)
    available = max(0.0, vram_gb - reserve_gb)
    return {
        "installed_vram_gb": vram_gb,
        "weight_storage_gb": round(base, 3),
        "estimated_weights_plus_overhead_gb": round(estimated, 3),
        "available_after_reserve_gb": round(available, 3),
        "approximate_weight_fit_only": estimated <= available,
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--vram-gb", type=float, required=True)
    p.add_argument("--parameters-b", type=float, required=True)
    p.add_argument("--bits", type=float, required=True)
    p.add_argument("--overhead", type=float, default=0.20)
    p.add_argument("--reserve-gb", type=float, default=2.0)
    args = p.parse_args()
    result = budget(args.vram_gb, args.parameters_b, args.bits, args.overhead, args.reserve_gb)
    for key, value in result.items():
        print(f"{key}: {value}")
    print("NOTE: approximate weight-fit only; NOT a guarantee that a model will run.")


if __name__ == "__main__":
    main()

