"""Volume imbalance for a single order book snapshot."""

from collections.abc import Sequence


def volume_imbalance(bids: Sequence[float], asks: Sequence[float]) -> float:
    """Compare summed bid and ask volumes. An empty book has zero imbalance."""
    bid_volume = sum(bids)
    ask_volume = sum(asks)
    total = bid_volume + ask_volume
    return (bid_volume - ask_volume) / total if total else 0.0


if __name__ == "__main__":
    print(f"Synthetic imbalance: {volume_imbalance([12, 8], [5, 5]):.3f}")
