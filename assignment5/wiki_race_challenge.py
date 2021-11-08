import sys, os, re
from requesting_urls import get_html
from filter_urls import find_articles
import time as tm

def shortest_path(start, end):
    """
    Finds the shortest path from the [start/ url] to [end/ url]. 
    Args:
        start (str): a given url in string format.
        end (str): a url to be found from the given url.
    Returns:
        (list, None): if the path was found, returns a list. Otherwise return None.
    """
    new_urls = [start]  # list to add all new urls to explore:
    path = {start: [start]}  # dictionary to create the shortest path:
    
    try:
        while (len(new_urls))>0:
            # remove the url currently visiting from the url list:
            current_page = new_urls.pop(0)
            html_string = get_html(current_page)
            # urls = find_articles(html_string)
            # non-duplicated urls:
            urls = list(dict.fromkeys(find_articles(html_string)))
            # print(current_page)
            # print(urls)
            for url in urls:
                # print(url)
                # check if we found the end url:
                if url == end:
                    return (path[current_page] + [url])

                # check if the shortest path to current url exists
                if url not in path and url != current_page:
                #     # path[current_page] holds the shortest path to current page,
                #     # we need to add current url to this path:
                    path[url] = path[current_page] + [url]
                    new_urls.append(url)
    except IndexError:
        pass
    return None

def race(start, end):
    """
    Run the race, and record the time for finding the shortest path.
    Write the time consumed for finding the paths, or for the entire process.
    Args:
        start (str): a given url in string format.
        end (str): a url to be found from the given url.
    """
    t0 = tm.perf_counter()
    result = shortest_path(start, end)
    t1 = tm.perf_counter()
    
    filename = sys.argv[0]
    dir = filename.split(".")[1].strip("\\")
    try:
        os.mkdir(f"{dir}")
    except FileExistsError:
        pass
    os.chdir(f"{dir}")
    
    if result:
        with open(f"shortest_way.txt", "a") as f:
            f.write(f"From the start url {start}\n")
            f.write(f"To the end url {end}\n")
            f.write(f"Time comsumed: {t1-t0} seconds.\n")
            f.write("The shortest path is:\n")
            for url in result:
                f.write(f"{url}\n\n")
    else:
        with open(f"shortest_way.txt", "a") as f:
            f.write(f"From the start url {start}\n")
            f.write(f"To the end url {end}\n")
            f.write(f"Time comsumed: {t1-t0} seconds.\n")
            f.write(f"There is no path found in between the start and end urls.\n\n")    
    os.chdir("..")

if __name__ == "__main__":
    start1 = "https://en.wikipedia.org/wiki/Parque_18_de_marzo_de_1938"
    end1 = "https://en.wikipedia.org/wiki/Bill_Mundell"
    race(start1, end1)
    
    start2 = "https://en.wikipedia.org/wiki/Nobel_Prize"
    end2 = "https://en.wikipedia.org/wiki/Array_data_structure"
    race(start2, end2)
    
    