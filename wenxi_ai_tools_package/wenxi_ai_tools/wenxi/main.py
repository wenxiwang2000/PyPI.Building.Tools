import pandas as pd
import argparse
from pathlib import Path


def run():
    """
    Simple CSV → XLSX converter
    """

    parser = argparse.ArgumentParser(
        description="Convert CSV file to Excel (.xlsx)"
    )

    parser.add_argument(
        "input",
        help="Input CSV file"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output Excel file",
        default=None
    )

    args = parser.parse_args()

    input_path = Path(args.input)

    if not input_path.exists():
        print("Input file not found.")
        return

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_suffix(".xlsx")

    df = pd.read_csv(input_path)

    df.to_excel(output_path, index=False)

    print("✔ Conversion complete")
    print(f"Saved to: {output_path}")
