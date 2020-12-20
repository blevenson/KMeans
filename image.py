# Python class to load in an image
# @author Brett Levenson

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class Image:
    def __init__(self, file_name):
        self.img = mpimg.imread(file_name)
        self.height, self.width, self.channels = self.img.shape

    def get_raw(self):
        return self.img

    # return the image as one array of 3-tuples
    def get_byte_array(self):
        output = []
        for row in self.img:
            for cell in row:
                output.append(cell.copy())

        return output

    # given updated byte array, save image
    def save_image(self, data, out_filename):
        mpimg.imsave(out_filename, np.reshape(data, (self.height, self.width, 3)))
