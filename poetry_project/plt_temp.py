
import matplotlib.pyplot as plt
import pandas as pd
import requests


URL = "https://api.open-meteo.com/v1/forecast"

PARAMS = {
    "latitude": 55.75,
    "longitude": 37.61,
    "hourly": "temperature_2m",
}


def make_dataframe(hours, temperatures):
    df = pd.DataFrame({
        "time": pd.to_datetime(hours),
        "temperature_c": temperatures,
    })
    return df.sort_values("time").reset_index(drop=True)


def main():
    response = requests.get(
        URL,
        params=PARAMS,
        timeout=15,
    )

    response.raise_for_status()
    data = response.json()

    hours = data["hourly"]["time"][:24]
    temperatures = data["hourly"]["temperature_2m"][:24]

    df = make_dataframe(hours, temperatures)

    df.to_csv("temperature_24h.csv", index=False)
    print("Сохранено в temperature_24h.csv")

    plt.plot(df["time"], df["temperature_c"], marker="o")
    plt.xticks(rotation=45)
    plt.title("Температура в Москве (24 часа)")
    plt.xlabel("Время")
    plt.ylabel("°C")
    plt.tight_layout()

    plt.savefig("temperature_24h.png")
    plt.close()

    print("Сохранено в temperature_24h.png")


if __name__ == "__main__":
    main()
