import os, sys, cv2
import time as tm
import numpy as np
from numba import jit
from python_color2sepia import python_color2sepia
from numpy_color2sepia import numpy_color2sepia


@jit(nopython=True)
def sepiascale_filter(image):
    """
    Takes image as input of extention with '.jpg', '.png', '.jpeg', '.bmp', returns sepia_scale version. Weighted sum of RGB values are 0.07, 0.72 and 0.21 respectively.
    Channel orders are 0(B), 1(G) and 2(R).
    
    Args:
        image (ndarry): 3D NumPy array of the image stored with dementions as [rows, columns, channels]. 
    Returns:
        image (ndarray): the sepia_scaled image with item values of the set weighted values as unit8 type.
    """
    sepia = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
    for i in range(len(image)):
        image[i] = image[i]  @ sepia.T
    return image


def numba_color2sepia(filename):
    """
    Takes the given image file, process it and save it to sepia scale.
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

    image = cv2.imread(filename)
    global demension
    demension = image.shape
    pythonname = sys.argv[0].strip('.\\').split('.')
    sepia_image = sepiascale_filter(image.astype("float64"))
    cv2.imwrite(f"{pythonname[0]}_sepiascale{ext}", sepia_image)

def report(filename):
    """
    Record the time and its average of sepiascale_filter() for 3 runs.
    The time and avg_time is then write to python report color2sepia.txt
    Args:
        The image file to be processed.
    """
    python0=tm.perf_counter()
    for i in range(3):
        python_color2sepia(filename)
    python1=tm.perf_counter()
    pythont=(python1 - python0)/3
    
    numpy0=tm.perf_counter()
    for i in range(3):
        numpy_color2sepia(filename)
    numpy1=tm.perf_counter()
    numpyt=(numpy1 - numpy0)/3
    
    numba0=tm.perf_counter()
    for i in range(3):
        numba_color2sepia(filename)
    numba1=tm.perf_counter()
    numbat=(numba1 - numba0)/3
    
    with open(f"numba_report_color2sepia.txt", "w") as f:
        f.write("Timing : python_color2sepia\n")
        f.write(f"Image demension: {demension}\n")
        f.write(f"Average runtime running python_color2sepia after 3 runs : {numbat} s\n")
        f.write(f"Average runtime of numba_color2sepia is {pythont/numbat:.3f} times faster than python_color2sepia\n")
        f.write(f"Average runtime of numba_color2sepia is {numpyt/numbat:.3f} times slower than numpy_color2sepia\n")
        f.write("Timing performed using: time.perf_counter()\n")
        
if __name__ == "__main__":
    report('rain.jpg')