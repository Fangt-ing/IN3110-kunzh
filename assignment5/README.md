# Assignment5 of IN4100

## Software version

Python 3.9.7

## Task 5.1

* manual_timing_.py runs the test of functions from test_slow_rectangle.py, each function is runned for 5 times. The time consumed by each run of coresponding function is saved to manual_report.txt.

* timeit_timing_.py runs the test of functions from test_slow_rectangle.py, each function is runned for 5 times.  In the meantime, it compares the time of coresponding function at each round to the ones in manual_timing_.py. The time consumed by each run of coresponding function and comparisons are saved to timeit_report.txt.

* cProfile_timing_.py compares the slowest function runned by using 2 different menthod defined in manual_timing_.py and timeit_timing_.py. Sata is saved to cProfile_report.txt.

## Task 4.1 Python for Instagram

The python_color2gray.py file takes in an image with extension of '.jpg, '.png', '.jpeg', '.bmp'. Then converts the image file to a grayed image, together it generates a report includes the following:

```python
Timing : python_color2gray
Image demension: (rows, columns, channels)
Average runtime running python_color2gray after 3 runs : x. xxxxxx s
Timing performed using : xyz
```

The task includes ```greyscale_filter()```. When certain image file are input, the functions will return filtered image files.

## 4.2 Sepia Filter - Add Vintage Style to your Images

The task includes```sepia_filter()```. When certain image file are input, the functions will return filtered image files.

## 4.3 The Package

In this package, according to requirements, it included filters and new function```grayscale_image(input filename, output filename=None)``` and ```sepia_image(input filename, output filename=None)``` as specified, when image file are fed into these functions they return filtered images respectively.

## 4.4 User interface

Althrough the codes are written, the user interface doesn't seem to work well.
