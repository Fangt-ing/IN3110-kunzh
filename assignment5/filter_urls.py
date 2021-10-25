import os, sys, re


def find_urls(html_string, base_url=None, output=None):
    """
    Finds all the absolute and releative URLs with the given html_string (string).
    Saves to (output.txt) file when output is given. Returns all matched urls.

    Args:
        html_string (str): HTML html strings.
    Return:
        url_list (list): list of found wikipedia URLs.
    """
    # f(ind) the f*_url:, detials for regular expression explaination can be found on regex101.com
    # find the full_url from the given string.
    full_url = re.findall(
        r'"canonical"(?:.)*?href="(https?://(?:.)*?(?="))', html_string
    )

    # find relative url
    frel_url = re.findall(r'<a(?:.)*?href="([\/][^\/](?:.)*?)(?=#|")', html_string)
    if base_url:
        rel_url = [f"{base_url}{url}" for url in frel_url]
    else:
        fbase_url = re.findall(r"https://(?:.)*?(?=/)", full_url[0])
        rel_url = [f"{fbase_url[0]}{url}" for url in frel_url]
    # find same_protocol urls
    fsame_proto = re.findall(r'<a(?:.)*?href="(//(?:.)*?)"', html_string)
    same_proto = [f"https:{url}" for url in fsame_proto]
    # find absolute urls
    fabs_url = re.findall(r'<a(?:.)*?href="(https?:(?:.)*?(?="))', html_string)
    abs_url = [f"{url}" for url in fabs_url]

    url_list = rel_url + same_proto + abs_url
    # url_list = [url for url in url_list]

    if output != None:
        filename = sys.argv[0]
        dir = filename.split(".")[1].strip("\\")
        try:
            os.mkdir(f"{dir}")
        except FileExistsError:
            pass
        os.chdir(f"{dir}")
        with open(f"{output}.txt", "w") as f:
            f.writelines(f"{full_url[0]}\n\n")
            for matched_url in url_list:
                f.writelines(f"{matched_url}\n")
        os.chdir("..")

    return url_list


def find_articles(html_string, output=None):
    """
    Find articles urls from the given html code pieces,
    saves to a output.txt file when output specified.Returns all matched urls.

    Args:
        html_string (str): HTML html strings.
    Return:
        article_url_list (list): list of found wikipedia URLs.
    """

    urls = find_urls(html_string)
    exclude = "File:|Wikipedia:|User:|MediaWiki:|Template:|Help:|Category:|Portal:|Draft:|TimedText:|Module:|Special:|Media:|Talk:"
    regex = rf"(?!.*?({exclude}).*?)(http.*?wikipedia\.org.*?$)"
    matched = [re.findall(regex, url) for url in urls]
    article_url_list = [i[0][1] for i in matched if i != []]

    if output != None:
        filename = sys.argv[0]
        dir = filename.split(".")[1].strip("\\")
        try:
            os.mkdir(f"{dir}")
        except FileExistsError:
            pass
        os.chdir(f"{dir}")
        with open(f"{output}.txt", "w") as f:
            for matched_url in article_url_list:
                f.writelines(f"{matched_url}\n")
        os.chdir("..")

    return article_url_list


if __name__ == "__main__":
    from requesting_urls import get_html

    url1 = "https://en.wikipedia.org/wiki/Nobel_Prize"
    url2 = "https://en.wikipedia.org/wiki/Bundesliga"
    url3 = "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup"

    Nobel_Prize = get_html(url1)
    nu = find_urls(Nobel_Prize, output="Nobel_Prize")
    find_articles(Nobel_Prize, "Nobel_Prize_wiki_articles")

    Bundesliga = get_html(url2)
    find_urls(Bundesliga, output="Bundesliga")
    find_articles(Bundesliga, output="Bundesliga_wiki_articles")

    FIS_Alpine_Ski_World_Cup = get_html(url1)
    find_urls(FIS_Alpine_Ski_World_Cup, output="FIS_Alpine_Ski_World_Cup")
    find_articles(
        FIS_Alpine_Ski_World_Cup, output="FIS_Alpine_Ski_World_Cup_wiki_articles"
    )
