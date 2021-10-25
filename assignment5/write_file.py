import os, sys


def creat_file(output=None):
    if output:
        filename = sys.argv[0]
        dir = filename.split(".")[1].strip("\\")
        try:
            os.mkdir(f"{dir}")
        except FileExistsError:
            pass
        os.chdir(f"{dir}")
        with open(f"{output}.txt", "w") as f:
            f.writelines(f"{full_url} \n\n")
            f.writelines(f"{url_list}")
        os.chdir("..")
