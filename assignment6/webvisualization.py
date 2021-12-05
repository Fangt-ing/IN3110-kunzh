from typing import Optional
from fastapi import FastAPI, Request, File, Form, UploadFile, requests
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import os

from webvisualization_plots import plot_reported_cases_per_million
import altair as alt

# create app variable (FastAPI instance)
app = FastAPI()
templates = Jinja2Templates(directory="templates")
sphinx_docs = Jinja2Templates(directory="docs\\build\\html\\")
# mount one or more static directories,
# e.g. your auto-generated Sphinx documentation with html files
app.mount(
    # the URL where these files will be available
    "/FastAPI Docs",
    StaticFiles(
        # the directory the files are in
        directory="docs\\build\\html\\",
        html=True,
    ),
    # an internal name for FastAPI
    name="static",
)
# os.path.join(os.path.dirname(__file__), "docs")

# app.mount(
#     # the URL where these files will be available
#     "/static",
#     StaticFiles(
#         # the directory the files are in
#         directory="static/",
#         html=True,
#     ),
#     # an internal name for FastAPI
#     name="static",
# )

def get_country_list():
    """Returns list of all countries.

    Returns:
        country_list [list]: all countries with covide reported.
    """
    df = pd.read_csv(
        "owid-covid-data.csv",
        sep=",",
        usecols=["location"] + ["date"] + ['new_cases_per_million'],
        parse_dates=["date"],
        date_parser=lambda col: pd.to_datetime(col, format="%Y-%m-%d"),
    )
    country_list = list(df.location.unique())

    return country_list

@app.get("/")
def plot_reported_cases_per_million_html(request: Request):
    """
    Root route for the web application.
    Handle requests that go to the path "/".
    """

    return templates.TemplateResponse(
        "plot_reported_cases_per_million.html",
        {
            "request": request,
            # further template inputs here
            "countries": get_country_list(), # from data frame countries
            # "start": start,
            # "end":  end,
        },
    )
    
@app.get('/help')
def help(request: Request):
    """Display help page info about webvisualization_plots.py

    Returns:
        templates.TemplateResponse [jinjia2 template]: Displays help inof on webvisualization_plots.html
    """
    return templates.TemplateResponse(
        "webvisualization_plots.html",{
            "request": request
        }
    )

@app.get('/FastAPI_docs')
def FastAPI_docs(request: Request):
    """Display FastAPI documentation about webvisualization.py

    Returns:
        templates.TemplateResponse [jinjia2 template]: Displays help inof on webvisualization.html
    """
    return sphinx_docs.TemplateResponse(
        "index.html",{
            "request": request
        }
    )

@app.get("/plot_reported_cases_per_million.json")
def plot_reported_cases_per_million_json(
    countries: Optional[str] = None, start: Optional[str] = None, end: Optional[str] = None):
    """Return json chart from altair"""
    # YOUR CODE
    if countries:
        countries = countries.split(",")
    else:
        countries =[]
    chart = plot_reported_cases_per_million(countries=countries, 
                                    start= start,
                                    end = end)
    # fig = plots.plot_daily_cases_altair(countries)
    return chart.to_dict()

def main():
    """Called when run as a script

    Should launch your web app
    """
    # YOUR CODE
    import uvicorn
    uvicorn.run(app)

if __name__ == "__main__":
    main()