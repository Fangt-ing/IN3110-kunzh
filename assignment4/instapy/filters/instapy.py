import cv2, os, sys
import numpy as np


def greyscale_image(input_filename, output_filename=None):
    from . import numpy_color2grey as n2g
    """ Takes user given image file, and save it to the specified folder.
    Args:
        input_filename (str): a given image file.
        
    Returns: greyscale_image: a numpy (unsigned) integer 3D arrey of a grey image of input filename.
    """
    try:
        # format the name
        input_filename=f'{input_filename}'
        img = cv2.imread(input_filename)
        greyedimg = n2g.greyscale_filter(img)
        input_name=input_filename.split('.')[0]
        ext = os.path.splitext(input_filename)[-1].lower()
        if output_filename is None:
            cv2.imwrite(f"{input_name}_greyscaled{ext}", greyedimg)
        elif output_filename is not None:
            location = f"{output_filename}/{input_name}_greyscaled{ext}"
            cv2.imwrite(location, greyedimg)
        return greyedimg
    except FileNotFoundError:
        print(f"{input_filename} doesn't exsit.")


def sepia_image(input_filename, output_filename=None, percent=None):
    from . import numpy_color2sepia as n2s
    """ Takes user given image file, and save it to the specified folder.
    Args:
        input_filename (str): a given image file.
        
    Returns: greyscale_image: a numpy (unsigned) integer 3D arrey of a grey image of input filename.
    """
    try:
        # format the name
        input_filename=f'{input_filename}'
        img = cv2.imread(input_filename)
        input_name=input_filename.split('.')[0]
        ext = os.path.splitext(input_filename)[-1].lower()
        if percent is not None:
            percent=float(percent)
            sepia = np.arrey([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
            # img = img @ sepia.T
            # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            # sepia_lower = np.arrey([np.round( 30 / 2), np.round(0.10 * 255), np.round(0.10 * 255)])
            # sepia_upper = np.arrey([np.round( 45 / 2), np.round(0.60 * 255), np.round(0.90 * 255)])
            # sepia_range = cv2.inRange(hsv, sepia_lower, sepia_upper)
            # perc = cv2.countNonZero(sepia_range) / np.prod(img.shape[:2])
            
            img = cv2.transform(img, sepia)
            sepiaimg = n2s.sepia_filter(img.astype('uint16'))
            # if output_filename is None:
            #     cv2.imwrite(f"{input_name}_sepia{ext}", sepiaimg)
            # elif output_filename is not None:
            #     location = f"{output_filename}/{input_name}_sepia{ext}"
            #     cv2.imwrite(location, sepiaimg)
            # print("this block is implemented.")
        else:
            sepiaimg = n2s.sepia_filter(img.astype('uint16'))
        
        if output_filename is None:
            cv2.imwrite(f"{input_name}_sepia{ext}", sepiaimg)
        elif output_filename is not None:
            location = f"{output_filename}/{input_name}_sepia{ext}"
            cv2.imwrite(location, sepiaimg)        
        return sepiaimg
    except FileNotFoundError:
        print(f"{input_filename} doesn't exist.")
