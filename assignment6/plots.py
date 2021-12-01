import io
from functools import lru_cache

import altair as alt
import pandas as pd
import requests

import matplotlib

matplotlib.use("agg")

import matplotlib.pyplot as plt

data_url = "https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv?raw=true"



def download_dataset(
    path,
    parse_dates=[
        "date",
    ],
    data_url=data_url,
):
    """Download a dataset from covid19-nor-data archive"""
    url = f"{data_url}/{path}"
    print(f"Downloading {url}")
    r = requests.get(f"{data_url}/{path}")
    r.raise_for_status()
    print(f"Downloaded {len(r.content) // 1024}kB")
    return pd.read_csv(io.BytesIO(r.content), parse_dates=parse_dates)


@lru_cache()
def country_data():
    # get raw case data
    cases = all_cases = pd.read_csv(
        "owid-covid-data.csv"
    )

    # aggregate data by country
    cases = (
        all_cases.groupby(["location", "date"])
        .sum()
        .reset_index()
    )
    # discard ukjent country where per 100k doesn't make sense
    cases = cases[~cases.location.str.contains("Unknown")]

    # 'cases' is a cumulative sum
    # reverse that to calculate the daily new case count
    cases["daily cases"] = 0

    for country in cases.location.unique():
        mask = cases.location == country
        country_cases = cases.loc[mask]
        diff = country_cases.cases.diff()
        # set first value from cases
        diff.iloc[0] = country_cases.iloc[0].cases
        cases.loc[country_cases.index, "daily cases"] = diff.astype(int)


    # per100k is "daily new cases per 100k population"
    cases["per100k"] = (
        (cases["daily cases"] * 1e5 / (cases["population"] + 1))
    )

    # limit data to 2021
    return cases[cases.date.dt.year]


def get_countries():
    """Return unique country names"""
    return country_data().location.unique()


def plot_daily_cases_altair(countries=None):
    # get data
    cases = country_data()
    # if countries specified, filter data
    if countries:
        # countries specified, only display those
        cases = cases[cases.location.isin(countries)]

    # return altair Chart
    return (
        alt.Chart(cases)
        .mark_line()
        .encode(
            x="date",
            y=alt.Y(
                "per100k",
                scale=alt.Scale(domain=(0, 100)),
            ),
            color="location",
            tooltip=[
                "date",
                "location",
                "per100k",
                "cases",
                "population",
            ],
        )
        .interactive()
    )


def figure_to_png_bytes(figure):
    """Convert a matplotlib figure to PNG bytes"""
    buf = io.BytesIO()
    # bbox_inches="tight" ensures nothing is cropped,
    # but size can be variable
    figure.savefig(buf, format="png", bbox_inches="tight")
    return buf.getvalue()


def plot_daily_cases_mpl(countries=None):
    # get data
    cases = country_data()
    # if countries specified, filter data
    if countries:
        # countries specified, only display those
        cases = cases[cases.location.isin(countries)]

    fig, ax = plt.subplots()
    fig.set_size_inches(4, 3)
    fig.set_dpi(200)

    cases.set_index("date").groupby("location").per100k.plot(legend=True, ax=ax)
    ax.set_ylim(0, 100)
    # shift the legend to just outside the right edge
    ax.legend(
        loc="upper left",
        bbox_to_anchor=(1.02, 1),
        borderaxespad=0,
    )
    # return figure rendered as PNG bytes
    return figure_to_png_bytes(fig)