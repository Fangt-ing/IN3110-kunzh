import sys, os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dts
import altair as alt


def get_data_from_csv(columns, countries=None, start=None, end=None):
    """Creates pandas dataframe from .csv file.
    Data will be filtered based on data column name, list of countries to be plotted and
    time frame chosen.
    Args:
        columns (list(string)): a list of data columns you want to include
        countries ((list(string), optional): List of countries you want to include.
        If none is passed, dataframe should be filtered for the 6 countries with the highest
        number of cases per million at the last current date available in the timeframe chosen.
        start (string, optional): The first date to include in the returned dataframe.
            If specified, records earlier than this will be excluded.
            Default: include earliest date
            Example format: "2021-10-10"
        end (string, optional): The latest date to include in the returned data frame.
            If specified, records later than this will be excluded.
            Example format: "2021-10-10"
    Returns:
        cases_df (dataframe): returns dataframe for the timeframe, columns, and countries chosen
    """
    try:
        df = pd.read_csv(
            "owid-covid-data.csv",
            sep=",",
            usecols=["location"] + ["date"] + columns,
            parse_dates=["date"],
            date_parser=lambda col: pd.to_datetime(col, format="%Y-%m-%d"),
        )

        if countries:
            # group the countries when countries are specified
            by_country = pd.concat(
                [df.groupby("location").get_group(country) for country in countries]
            )
            if start and end and start > end:
                print("End must be later than start!")
                raise ValueError

            if start:
                start = pd.to_datetime(start, format="%Y-%m-%d")
            elif not start:
                start = by_country["date"].iloc[0]

            if end:
                end = pd.to_datetime(end, format="%Y-%m-%d")
            elif not end:
                end = by_country["date"].iloc[-1]

            if (start not in df.date.values) or (end not in df.date.values):
                print(
                    f"The date ranges from {df.date.iloc[0]} to {df.date.iloc[-1]},\n\
                      please choose a date from the date rage."
                )
                raise ValueError
            cases_df = by_country.loc[
                (by_country.date >= start) & (by_country.date <= end)
            ]
        else:
            # get the latest date and drop any country that don't have record on this day.
            latest = df.drop_duplicates(subset="location", keep="last").dropna(
                how="any"
            )
            # sort by new_cases_per_million, and assing the top six countries
            cases_df = latest.sort_values(by="new_cases_per_million", ascending=False)[
                :6
            ]

    except FileNotFoundError:
        print(
            "Please visit: https://ourworldindata.org/covid-cases and download the owid-covid-data.csv"
        )

    return cases_df


def plot_reported_cases_per_million(countries=None, start=None, end=None):
    """Plots data of reported covid-19 cases per million using altair.
    Calls the function get_data_from_csv to receive a dataframe used for plotting.
    Args:
        countries ((list(string), optional): List of countries you want to filter.
        If none is passed, dataframe will be filtered for the 6 countries with the highest
        number of cases per million at the last current date available in the timeframe chosen.
        start (string, optional): a string of the start date of the table, none
        of the dates will be older then this on
        end (string, optional): a string of the en date of the table, none of
        the dates will be newer then this one
    Returns:
        altair Chart of number of reported covid-19 cases over time.
    """
    # choose data column to be extracted
    columns = ["new_cases_per_million"]
    # create dataframe
    cases_df = get_data_from_csv(
        columns=columns, countries=countries, start=start, end=end
    )

    # Note: when you want to plot all countries simultaneously while enabling checkboxes, you might need to disable altairs max row limit by commenting in the following line
    # alt.data_transformers.disable_max_rows()

    chart = (
        alt.Chart(cases_df, title=f"{columns[0]} of {countries}")
        .mark_line()
        .encode(
            x=alt.X(
                "date:T",
                axis=alt.Axis(
                    format="%b, %Y", title="Date", titleFontSize=14, tickCount=20
                ),
            ),
            y=alt.Y(
                "new_cases_per_million",
                axis=alt.Axis(
                    title="Number of Reported Cases per Million",
                    titleFontSize=14,
                    tickCount=10,
                ),
            ),
            color=alt.Color("location:N", legend=alt.Legend(title="Country")),
        )
        .interactive()
    )
    return chart


def main():
    """Function called when run as a script
    Creates a chart and display it or save it to a file
    """
    chart = plot_reported_cases_per_million(countries=["Norway"], start="2021-05-10")
    # chart.show requires altair_viewer
    # or you could save to a file instead
    chart.show()


if __name__ == "__main__":
    main()

# if __name__ == '__main__':
#     print(plot_reported_cases_per_million(['new_cases_per_million'], countries=['Norway'], start = '2020.10.10', end = '2021.10.10'))
