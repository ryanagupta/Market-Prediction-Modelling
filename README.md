# Limit Order Book Modelling

**Status** · Starter scaffold

The goal is to predict short-horizon mid-price direction from bid and ask data and compare a CNN with simple baselines.

## Run the starter

From the repository root, run `python src/baseline.py` with Python 3.10 or later. It prints order book imbalance for a synthetic snapshot.

- `src/baseline.py` calculates volume imbalance.
- `experiments/README.md` outlines the first benchmark and data requirements.

The first milestone is a chronological benchmark of a majority-class predictor and an imbalance model. CNN training and cost-aware backtests are planned.
