
from plt_temp import make_dataframe


def test_make_dataframe():
    hours = [
        "2026-10-26T12:00",
        "2026-10-26T10:00",
        "2026-10-26T11:00",
    ]

    temperatures = [12.0, 10.0, 11.0]

    df = make_dataframe(hours, temperatures)


    assert len(df) == 3


    assert list(df.columns) == [
        "time",
        "temperature_c",
    ]


    assert df["time"].is_monotonic_increasing


    assert df["temperature_c"].tolist() == [
        10.0,
        11.0,
        12.0,
    ]
