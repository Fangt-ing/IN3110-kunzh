import sys, os, cv2
import numpy as np
import time as tm
from python_color2gray import python_color2gray

def grayscale_filter(image):
    """
    Takes image as input of extention with '.jpg', '.png', '.jpeg', '.bmp', returns gray_scale version. Weighted sum of RGB values are 0.07, 0.72 and 0.21 respectively.
    Channel orders are 0(B), 1(G) and 2(R).
    
    Args:
        image (ndarry): 3D NumPy array of the image stored with dementions as [rows, columns, channels]. 
    Returns:
        image (ndarray): the gray_scaled image with item values of the set weighted values as unit8 type.
    """
    # this function turns the default BGR to RGB orders.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image[:, :, 0]*0.07 + image[:, :, 1]*0.72 + image[:, :, 2]*0.21

    return image.astype('uint8')


def numpy_color2gray(filename):
    """
    Takes the given image file, process it and save it to gray scale.
    Args:
        The image file to be processed.
    """
    ext = os.path.splitext(filename)[-1].lower()
    picext = ['.jpg', '.png', '.jpeg', '.bmp']
    try:
        if ext in picext:
            with open(filename, 'r') as f:
                pass
    except Exception as InvalidExt:
        print(f'The file must be of image type: {InvalidExt}!')

    img = cv2.imread(filename)
    global demension
    demension = img.shape
    pythonname = sys.argv[0].strip('.\\').split('.')
    grayed_image = grayscale_filter(img)
    cv2.imwrite(f"{pythonname[0]}_grayscale{ext}", grayed_image)

def python_time():
    t0 = tm.perf_counter()
    for i in range(3):
        python_color2gray('rain.jpg')
    t1 = tm.perf_counter()
    python_avg = (t1-t0)/3
    return python_avg

def report(filename):
    """
    Record the time and its average of grayscale_filter() for 3 runs.
    The time and avg_time is then write to python report color2gray.txt
    Args:
        The image file to be processed.
    """

    ts = tm.perf_counter()  # ts = time start
    for i in range(3):
        numpy_color2gray(filename)
    te = tm.perf_counter()  # te = time end
    avg_time = (te - ts) / 3

    with open(f"numpy_report_color2gray.txt", "w") as f:
        f.write("Timing : python_color2gray\n")
        f.write(f"Image demension: {demension}\n")
        f.write(
            f"Average runtime running python_color2gray after 3 runs : {avg_time:f} s\n"
        )
        f.write(f"Average runtime of numpy_color2gray is {python_time()/avg_time:.3f} times faster than python_color2gray\n")
        f.write("Timing performed using: time.perf_counter()\n")


if __name__ == "__main__":
    report('rain.jpg')