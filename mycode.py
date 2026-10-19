from __future__ import annotations

from pathlib import Path

import pandas as pd


def build_sample_data() -> pd.DataFrame:
    """Return the small versioned sample table."""
    return pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie", "GF1", "GF18"],
            "Age": [25, 30, 35, 20, 9],
            "City": ["New York", "Los Angeles", "Chicago", "City1", "Kandirvan"],
        }
    )


def save_sample_data(output_path: Path = Path("data/sample_data.csv")) -> Path:
    """Write the sample table to CSV and return its path."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    build_sample_data().to_csv(output_path, index=False)
    return output_path


if __name__ == "__main__":
    path = save_sample_data()
    print(f"CSV saved to {path}")
