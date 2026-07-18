import argparse
from report import build_race_report, save_report


def main():
    parser = argparse.ArgumentParser(description="OpenF1 race weekend analyzer")
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--country", type=str, required=True)
    parser.add_argument("--out", type=str, default="race_report.json")
    args = parser.parse_args()

    report = build_race_report(args.year, args.country)
    save_report(report, args.out)
    print(f"Saved report for {args.country} {args.year} to {args.out}")


if __name__ == "__main__":
    main()
