import sys
from pathlib import Path
import argparse
import pandas as pd
from typing import Optional, List


def load_csv_with_encodings(path_str: str, encodings: List[str]) -> tuple[pd.DataFrame, Optional[str]]:
    p = Path(path_str).expanduser()
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")

    last_exc = None
    for enc in encodings:
        try:
            df = pd.read_csv(p, encoding=enc)
            return df, enc
        except Exception as e:
            last_exc = e
    # If we get here, none of the encodings worked
    raise last_exc


def compare_dataframes(df1: pd.DataFrame, df2: pd.DataFrame):
    if df1.equals(df2):
        print("Both CSV files are 100% identical.")
        return

    print("Files are NOT identical.")
    try:
        diff = df1.compare(df2)
        if diff.empty:
            print("No cell-wise differences found, but DataFrames differ (maybe index/column order or dtypes).")
        else:
            print("Differences (row/column pairs):")
            print(diff)
    except Exception as e:
        print("Could not compute cell-wise differences:", e)


def parse_args():
    p = argparse.ArgumentParser(description="Compare two CSV files and show differences.")
    p.add_argument("file1", nargs="?", help="Path to first CSV file")
    p.add_argument("file2", nargs="?", help="Path to second CSV file")
    p.add_argument("--encoding", "-e", help="Encoding to use for both files (if not set, tries utf-8, cp1252, latin1)")
    return p.parse_args()


def main():
    args = parse_args()

    # Default paths (used if user didn't provide arguments)
    default1 = r"C:\Users\iabhi\OneDrive\Desktop\inventory_export_1 (2).csv"
    default2 = r"C:\Users\iabhi\Downloads\inventory_export_1.csv"

    path1 = args.file1 or default1
    path2 = args.file2 or default2

    # Build encoding list to try
    if args.encoding:
        encodings = [args.encoding]
    else:
        encodings = ["utf-8", "cp1252", "latin1"]

    try:
        df1, enc1 = load_csv_with_encodings(path1, encodings)
        print(f"Loaded '{path1}' with encoding: {enc1}")
    except Exception as e:
        print(f"Failed to load {path1}: {e}")
        sys.exit(2)

    try:
        df2, enc2 = load_csv_with_encodings(path2, encodings)
        print(f"Loaded '{path2}' with encoding: {enc2}")
    except Exception as e:
        print(f"Failed to load {path2}: {e}")
        sys.exit(2)

    compare_dataframes(df1, df2)


if __name__ == "__main__":
    main()
