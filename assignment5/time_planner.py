import os, sys, re
from bs4 import BeautifulSoup
from requesting_urls import get_html


def extract_events(url):
    """
        Extracts date, venue and discipline column from wikipedia table for FIS Alpine Ski World Cup.
        Info from https://en.wikipedia.org/wiki/202122_FIS_Alpine_Ski_World_Cup (page not working),
        changed to https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup.
        The extracted data is saved to betting_slip_empty.md.
        In addition to the extracted data, the file contains an extra cloumn for betting on the winner.

        Args:
            url (str): the url link to be observed.
        Returns:
            table_info ( list of lists ): A nested list where 
            the rows represent each 13 race date, 
            and the columns are [ date, venue, discipline ].
    """
    
    disciplines = {
        "DH": " Downhill ",
        "SL": " Slalom ",
        "GS": " Giant Slalom ",
        "SG": " Super Giant Slalom ",
        "AC": " Alpine Combined ",
        "PG": " Parallel Giant Slalom ",
    }
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('table', {"class": 'wikitable plainrowheaders'})
    # find table rows
    table_rows = table.find_all("tr")[1:]
    dates = [None]*len(table_rows)
    venue = [None]*len(table_rows)
    discipline = [None]*len(table_rows)
    # count the amount of rows for event
    rowspan_event = 0
    # count the amount or rows for venue
    rowspan_venue = 0

    # iterate through table rows
    for i, row in enumerate(table_rows):
        # remove superscript tag
        [tag.decompose() for tag in row.find_all("sup")]
        # find data cells in table
        cells = row.find_all("td")
        # find text
        ctext = [cell.get_text(strip=True) for cell in cells]

        # check event status in table @ row length >= 4:
        if cells[0].get("colspan") and len(cells) >= 4:
            dates[i] = ctext[1]
            # check if next event status
            if cells[0].get("rowspan"):
                rowspan_event = i + int(cells[0].get("rowspan"))

            # check previous venue status
            if i < rowspan_venue:
                venue[i] = venue[i-1]
                discipline[i] = disciplines[ctext[2][:2]]
            else:
                venue[i] = ctext[2]
                discipline[i] = disciplines[ctext[3][:2]]
                # compare next venue
                if cells[2].get("rowspan"):
                    rowspan_venue = i + int(cells[2].get("rowspan"))

        # check previous event
        elif i < rowspan_event:
            dates[i] = ctext[0]
            # compare the previous venue
            if i < rowspan_venue:
                venue[i] = venue[i-1]
                discipline[i] = disciplines[ctext[1][:2]]
            else:
                venue[i] = ctext[1]
                discipline[i] = disciplines[ctext[2][:2]]
                # compare the next venue
                if cells[1].get("rowspan"):
                    rowspan_venue = i + int(cells[1].get("rowspan"))

        # normal row @ length >= 5
        elif len(cells) >= 5:
            dates[i] = ctext[2]
            # check the next venue
            if i < rowspan_venue:
                venue[i] = venue[i-1]
                discipline[i] = disciplines[ctext[3][:2]]
            else:
                venue[i] = ctext[3]
                discipline[i] = disciplines[ctext[4][:2]]
                # check the next venue
                if cells[3].get("rowspan"):
                    rowspan_venue = i + int(cells[3].get("rowspan"))

    dates = [i for i in dates if i != None]
    venue = [i for i in venue if i != None]
    discipline = [i for i in discipline if i != None]
    events = [(dt, vn, dp) for dt, vn, dp in zip(dates, venue, discipline)]

    return events


def create_betting_slip(events, save_as):
    dir = "datetime_filter"
    # save_as = 'betting_slip_empty.md'
    os.makedirs(dir, exist_ok=True)

    with open(f"./{dir}/{save_as}.md", "w") as f:
        f.write(f"# BETTING SLIP ({save_as})\n\nName:\n\n")
        f.write("Date | Venue | Discipline | Who wins?\n")
        f.write(" --- | --- | --- | --- \n")
        for e in events:
            dates, venue, discipline = e
            f.write(f"{dates} | {venue} | {discipline} \n")


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup"
    create_betting_slip(extract_events(url), "betting_slip_empty")
