from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import matplotlib.pyplot as plt

from webvisualization_plots import plot_reported_cases_per_million
import altair as alt

# create app variable (FastAPI instance)
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# mount one or more static directories,
# e.g. your auto-generated Sphinx documentation with html files
app.mount(
    # the URL where these files will be available
    "/static",
    StaticFiles(
        # the directory the files are in
        directory="static/",
        html=True,
    ),
    # an internal name for FastAPI
    name="static",
)

@app.get('/test')
def testing(input: str=None):
    return {"Please input:": input}

@app.get("/", response_class=HTMLResponse)
def plot_reported_cases_per_million_html(request: Request, 
                                         countries: Optional[str] = None, 
                                         start: Optional[str] = None, 
                                         end: Optional[str] = None):
    """
    Root route for the web application.
    Handle requests that go to the path "/".
    """
    if countries:
        countries = countries.replace(' ', '').split(",")
        chart = plot_reported_cases_per_million(countries=countries, 
                                                start=start,
                                                end = end)
    return templates.TemplateResponse(
        "plot_reported_cases_per_million.html",
        {
            "request": request,
            # further template inputs here
            "countries": chart.show()
        },
    )


@app.get("/plot_reported_cases_per_million.json")
def plot_reported_cases_per_million_json(
    countries: Optional[str] = None, start: Optional[str] = None, end: Optional[str] = None):
    """Return json chart from altair"""
    # YOUR CODE
    if countries:
        countries = countries.replace(' ', '').split(",")
        # fig = plt.plot_reported_cases_per_million(countries, start, end)
        fig = plot_reported_cases_per_million(countries=countries, 
                                        start=start,
                                        end = end)
    return fig.to_dict()
        


def main():
    """Called when run as a script

    Should launch your web app
    """
    # YOUR CODE
    plot_reported_cases_per_million_html()


if __name__ == "__main__":
    # import uvicorn
    # uvicorn.run(app)
    main()