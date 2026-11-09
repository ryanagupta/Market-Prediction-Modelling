# First benchmark

1. Use a permitted source of timestamped bid and ask prices and volumes. Record the source, licence, symbol and depth.
2. Define the look-ahead horizon and neutral class threshold before testing.
3. Split by time, leave a gap across split boundaries for overlapping label windows, and fit preprocessing on training data only.
4. Compare a majority-class predictor, an imbalance model and a CNN using macro F1 and per-class recall.
5. If simulating a strategy, report transaction costs and assumptions separately from prediction metrics.
