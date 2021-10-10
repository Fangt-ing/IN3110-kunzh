from assignment4.instapy.numpy_color2gray import numpy_color2gray
import os
import cv2


@numpy_color2gray(filename=)
def grayscale_image(input_filename, output_filename=None):
    img = cv2.imread(input_filename)
    location = output_filename
    cv2.imwrite(os.path.join(location, input_filename), img)
    

# def sepia_image(input_filename, output_filename=None):
    

if __name__ == "__main__":
    grayscale_image('rain.jpg', 'D:\\ProgramData\\GitHub\IN3110-kunzh\\assignment4\\instapy')