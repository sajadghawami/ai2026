"""Compare predictions with the correct labels.

Usage:
  python3 score.py predictions.csv practice_labels.csv
  python3 score.py predictions.csv test_labels.csv

predictions.csv needs the columns: id, prediction
The second file needs the columns: id, label
"""
import csv
import sys


def read(path, column):
    with open(path, newline="", encoding="utf-8") as f:
        return {row["id"].strip(): row[column].strip() for row in csv.DictReader(f)}


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    predictions = read(sys.argv[1], "prediction")
    labels = read(sys.argv[2], "label")
    missing = [i for i in labels if i not in predictions]
    if missing:
        sys.exit(f"No prediction for {len(missing)} ids, e.g. {missing[:5]}")
    misses = [(i, predictions[i], labels[i]) for i in labels if predictions[i] != labels[i]]
    correct = len(labels) - len(misses)
    print(f"Score: {correct} / {len(labels)} = {correct / len(labels):.0%}")
    for i, predicted, label in misses:
        print(f"  {i}: predicted {predicted}, correct is {label}")


if __name__ == "__main__":
    main()
