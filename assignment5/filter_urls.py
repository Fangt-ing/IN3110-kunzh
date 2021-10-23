import os, sys, re


def find_urls(html_string, base_url=None, output=None):
    """
    Finds all the absolute and releative URLs with the given html_string.
    """
    url_list=[]
    # find the base_url as http: or https:
    rel_url=re.findall(r'<a(?:.)*?href="([^#](?:.)*?)(?=[#"])', html_string)
    abs_url=re.findall(r'<a.href="(https?:(?:.)*?(?="))', html_string)
    if base_url:
        base_url = base_url
    else:
        base_url=re.findall()

    url_list.append(base_url[0].text.ecode('utf-8'))
    if output:
        filename=sys.argv[0]
        dir=filename.split('.')[1].strip('\\')
        try:
            os.mkdir(f"{dir}")
        except FileExistsError:
            pass
        os.chdir(f"{dir}")
        with open(f"{output}.txt", "w") as f:
            f.write(f"{url_list} \n\n")
            # f.write(f"{rps.text.encode('utf-8')}")
        os.chdir('..')
        
    return url_list


def find_articles(html_string, output=None):
    """
    """
    urls = find_urls(text)

    return article_url_list
