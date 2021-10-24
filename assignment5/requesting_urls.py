import os, sys
import requests as rqs


def get_html(url, params=None, output=None):
    """
    Request from the given url, parameters (optional).
    Then write (if output directory is defined) to the specified output directory.
    Args:
        url (string): the URL to request data from.
        param(dictionary): a dictionary holding key-values. Default as none.
        ouput(string): requested data will be saved to this file as output.txt.
    Returns:
        response: requested info from the given URL with params (optional).
    """
    rps = rqs.get(url, params=params)
    html_string = str(rps.text.encode('utf-8'))

    if output:
        filename=sys.argv[0]
        dir=filename.split('.')[1].strip('\\')
        try:
            os.mkdir(f"{dir}")
        except FileExistsError:
            pass
        os.chdir(f"{dir}")
        with open(f"{output}.txt", "w") as f:
            f.write(f"{rps.url} \n\n")
            f.write(f"{rps.text.encode('utf-8')}")
        os.chdir('..')
    
    return html_string


if __name__ == "__main__":
    get_html("https://en.wikipedia.org/wiki/Studio_Ghibli", output="Studio_Ghibl")
    get_html("https://en.wikipedia.org/wiki/Star_Wars", output="Star_Wars")
    get_html(
        "https://en.wikipedia.org/w/index.php",
        params={"title": "Main_Page", "action": "info"},
        output="Main_Page",
    )

