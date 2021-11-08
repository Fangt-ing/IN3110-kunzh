import re, os, sys
from requesting_urls import get_html


def find_dates(html_string, output=None):
    """
    Finds all the absolute and releative URLs with the given html_string (string).
    Saves to (output.txt) file when output is given. Returns all matched urls.

    Args:
        html_string (str): HTML html strings.
    Return:
        results (list): list of found datetime.
    """
    # Detail explainations for regular expression to be found on regex101.com
    year = r"(?P<Y>[1-9]\d{3})"
    months = r"(?P<M>Jan\w*|Feb\w*|Mar\w*|Apr\w*|May\w*|Jun\w*|Jul\w*|Aug\w*|Sep\w*|Oct\w*|Nov\w*|Dec\w*)"
    day = r"(?P<D>[1-3]?\d)"
    # Different datetime-format
    YMD = rf"{year}\s{months}\s{day}?"
    DMY = rf"{day}?\s{months}\s{year}"
    MDY = rf"{months}\s{day}?,?\s{year}"
    ISO = rf"{year}[-\s](?P<M>[01]\d)[-\s](?P<D>[0-3]\d)"

    tYMD = re.findall(rf"({YMD})", Rowling)
    tDMY = re.findall(rf"({DMY})", Rowling)
    tMDY = re.findall(rf"({MDY})", Rowling)
    tISO = re.findall(rf"({ISO})", Rowling)
    time_match = tYMD + tDMY + tMDY + tISO
    time_match = [item for item in time_match if item != []]

    dYMD = [re.sub(rf"({YMD})", r"\g<Y>/\g<M>/\g<D>", d[0]) for d in time_match]
    dDMY = [re.sub(rf"({DMY})", r"\g<Y>/\g<M>/\g<D>", d[0]) for d in time_match]
    dMDY = [re.sub(rf"({MDY})", r"\g<Y>/\g<M>/\g<D>", d[0]) for d in time_match]
    dISO = [re.sub(rf"({ISO})", r"\g<Y>/\g<M>/\g<D>", d[0]) for d in time_match]
    dates = dYMD + dDMY + dMDY + dISO
    dates = [itm for itm in dates if itm != []]

    months = [
        "Jan\w*",
        "Feb\w*",
        "Mar\w*",
        "Apr\w*",
        "May\w*",
        "Jun\w*",
        "Jul\w*",
        "Aug\w*",
        "Sep\w*",
        "Oct\w*",
        "Nov\w*",
        "Dec\w*",
    ]
    digi_months = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
    ]
    for month, digi_month in zip(months, digi_months):
        digi_dates = [re.sub(month, digi_month, date) for date in dates]

    results = [i[:8] + i[8].zfill(2) if len(i) == 9 else i for i in digi_dates]
    results.sort()

    full_url = re.findall(
        r'"canonical"(?:.)*?href="(https?://(?:.)*?(?="))', html_string
    )
    if output:
        filename = sys.argv[0]
        dir = filename.split(".")[1].strip("\\")
        try:
            os.mkdir(f"{dir}_regex")
        except FileExistsError:
            pass
        os.chdir(f"{dir}_regex")
        with open(f"{output}.txt", "w") as f:
            f.writelines(f"{full_url[0]}\n\n")
            for match_date in results:
                f.writelines(f"{match_date}\n")
        os.chdir("..")

    return results


if __name__ == "__main__":
    url1 = "https://en.wikipedia.org/wiki/J._K._Rowling"
    url2 = "https://en.wikipedia.org/wiki/Richard_Feynman"
    url3 = "https://en.wikipedia.org/wiki/Hans_Rosling"

    Rowling = get_html(url1)
    find_dates(Rowling, "J._K._Rowling")

    Richard_Feynman = get_html(url2)
    find_dates(Richard_Feynman, "Richard_Feynman")

    Hans_Rosling = get_html(url3)
    find_dates(Hans_Rosling, "Hans_Rosling")
