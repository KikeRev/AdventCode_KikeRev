import pandas as pd
import os
import argparse

def solver(file: str) -> int:
    if not os.path.exists(file):
        raise FileNotFoundError(f"The file '{file}' does not exist. Please provide a valid path.")

    df = pd.read_csv(file, header=None)

    source1 = list(df[0].sort_values())
    source2 = list(df[1].sort_values())

    return sum([abs(source1[i] - source2[i]) for i in range(len(source1))])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file',
        type=str,
        help='path of the input file'
    )

    args = parser.parse_args()
    try:
        result = solver(args.file)
        print(f"The result is: {result}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
