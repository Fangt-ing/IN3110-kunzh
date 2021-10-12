import cv2, os, sys
import numpy as np


def greyscale_image(input_filename, output_filename=None, choice='numpy'):
    
    """ Takes user given image file, and save it to the specified folder.
    Args:
        input_filename (str): a given image file.
        
    Returns: greyscale_image: a numpy (unsigned) integer 3D array of a grey image of input filename.
    """
    try:
        # format the name
        input_filename=f'{input_filename}'
        img = cv2.imread(input_filename)
        input_name=input_filename.split('.')[0]
        ext = os.path.splitext(input_filename)[-1].lower()
        if choice == 'python':
            from . import python_color2grey as p2g
            greyedimg = p2g.greyscale_filter(img)
        elif choice == 'numpy':
            from . import numpy_color2grey as n2g
            greyedimg = n2g.greyscale_filter(img)
        elif choice == 'numba':
            from . import numba_color2grey as nb2g
            greyedimg = nb2g.greyscale_filter(img)
        
        if output_filename is None:
            cv2.imwrite(f"{input_name}_greyscaled{ext}", greyedimg)
        elif output_filename is not None:
            location = f"{output_filename}/{input_name}_greyscaled{ext}"
            cv2.imwrite(location, greyedimg)
        return greyedimg
    except FileNotFoundError:
        print(f"{input_filename} doesn't exsit.")


def sepia_image(input_filename, output_filename=None, choice='numpy', percent=None):
    """ Takes user given image file, and save it to the specified folder.
    Args:
        input_filename (str): a given image file.
        
    Returns: greyscale_image: a numpy (unsigned) integer 3D array of a grey image of input filename.
    """
    try:
        # format the name
        input_filename=f'{input_filename}'
        img = cv2.imread(input_filename)
        input_name=input_filename.split('.')[0]
        ext = os.path.splitext(input_filename)[-1].lower()
        
        # if percent is not None:
        #     percent=float(percent)
        #     sepia = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
        #     img = cv2.transform(img, sepia * percent)
                
        if choice == 'python':
            from . import python_color2sepia as p2s
            sepiaimg = p2s.sepia_filter(img.astype('uint16'))
        elif choice == 'numpy':
            from . import numpy_color2sepia as n2s
            sepiaimg = n2s.sepia_filter(img.astype('uint16'))
        elif choice == 'numba':
            from . import numba_color2sepia as nb2g
            sepiaimg = nb2g.sepiascale_filter(img.astype('uint16'))
        
        if output_filename is None:
            cv2.imwrite(f"{input_name}_sepia{ext}", sepiaimg)
        elif output_filename is not None:
            location = f"{output_filename}/{input_name}_sepia{ext}"
            cv2.imwrite(location, sepiaimg)        
        return sepiaimg
    except FileNotFoundError:
        print(f"{input_filename} doesn't exist.")
