import cv2, os, sys
import numpy_color2sepia as n2s


def sepia_image(input_filename, output_filename=None):
    """ Takes user given image file, and save it to the specified folder.
    Args:
        input_filename (str): a given image file.
        
    Returns: grayscale_image: a numpy (unsigned) integer 3D array of a gray image of input filename.
    """
    try:
        # format the name
        input_filename=f'{input_filename}'
        img = cv2.imread(input_filename)
        sepiaimg = n2s.sepia_filter(img.astype('uint16'))
        input_name=input_filename.split('.')[0]
        ext = os.path.splitext(input_filename)[-1].lower()
        if output_filename is None:
            cv2.imwrite(f"{input_name}_sepia{ext}", sepiaimg)
        elif output_filename is not None:
            location = f"{output_filename}/{input_name}_sepia{ext}"
            cv2.imwrite(location, sepiaimg)
        return sepiaimg
    except FileNotFoundError:
        print(f"{input_filename} doesn't exist.")