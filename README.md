# K-Means Clustering for Images
K-means clustering applied to the color of images.  Applications of this technology are image compression or interesting effects for posting on social media.

<p align="center">
  <img src="./GIF/ImageProgresion.gif" alt="Changing K value">
</p>

This was done as a fun and quick side project, so feel free to enjoy it, bugs and all :).

# Tool
```bash
$ python3 main.py [K value] [input_image] [output_image]
```
The program is written in python3 and is invoked by running the `main.py` file.  It must take in three arguments, the first being the `k value` which tells the program how many colors the new image should use.  This is followed by the `input image` which specifies the source file and the `output image` which is the new file location that the image will be written to.  The input and output images are allowed to be the same.

Below is an example usage:
```bash
$ python3 main.py 100 Brett.jpeg Brett_100.jpeg
```

## Dependencies

The tool relies on [matplotlib](https://matplotlib.org/) to open and save images.  They are loaded in as a [numpy](https://numpy.org/) matrix of `height x width x 3 color channels`.  Matplotlib was selected because the only image manipulation needed was loading and saving, and it enables a much wider range of file formats to be selected than writing a new image loader.

To install all the dependencies, simply run the below command.
```bash
$ pip3 install matplotlib
```

# Design
The code is broken up into three files to enable ease of reading.
## `main.py`
Driver program that is invoked when an image is to be modified.  This also includes example code of how to run the k-means algorithm on other data.

## `KMeans.py`
Main implementation of the [k-means algorithm](https://en.wikipedia.org/wiki/K-means_clustering#Standard_algorithm_(na%C3%AFve_k-means)).  This file defines the KMeans class which exposes two main functions to the user.
* `fit(data)`:  trains the model to update the member `nodes` to contain the K centroids.  This function takes in an array of arrays, which is a list of points.
* `predict(X)`:  Returns the closest centroid stored inside the `nodes` member variable in this class.  The `fit()` function must be called before calling this function.  This function takes in one single point for classification.

The class can be configured with the constructor to define the *K* value, `thresh` which determines the maximum amount the centers move before terminating, and `iters` the number of iterations before halting.

The means are initalized to K random points in the image without resampling (we assume there are more pixels than there are colors it can use).  The algorithm then follows a two step process.  
1.  Predict the closest node for every point in the training data.  
2. Update all the centers to be the mean of all the training points in its class.

The termination criteria is either a set number of iterations or once the image means have been moved by less than the defined threshold,`thresh`, whichever occurs first.

## `image.py`
A wrapper class around matplotlib's image loading and saving so that the main function doesn't have to worry about how images are loaded.  This abstraction provides the benefit of allowing different image systems to be easily plugged in by just replacing this one file.  Exposed interface of the `Image` class are shown below.
* `get_byte_array()`: returns the image as one continues array of points with the 3-channel colors.
* `save_image(data, out_filename)`: saves the byte array image to the given filename.
