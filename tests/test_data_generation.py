from pathlib import Path

import pandas as pd

from mycode import build_sample_data, save_sample_data


def test_sample_table_has_expected_shape() -> None:
    frame = build_sample_data()
    assert list(frame.columns) == ["Name", "Age", "City"]
    assert len(frame) == 5


def test_sample_table_can_be_saved(tmp_path: Path) -> None:
    output = save_sample_data(tmp_path / "data" / "sample.csv")
    assert output.is_file()
    assert pd.read_csv(output).equals(build_sample_data())
