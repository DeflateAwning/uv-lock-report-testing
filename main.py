import polars as pl

def main():
    print("Hello from uv-lock-report-testing!")

    df = pl.DataFrame({
        "a": [1, 2, 3],
        "b": ["x", "y", "z"]
    })
    print(f"Sample dataframe:\n{df}")


if __name__ == "__main__":
    main()
