from PIL import Image, ImageFilter
import matplotlib.pyplot as plot

def displayImage(path):
    image = Image.open(path)
    plot.imshow(image)
    plot.axis(False)
    plot.show()
    return image

def toGrayscale(path):

    image = Image.open(path)
    grayImage = image.convert('L')

    return grayImage

def gaussianBlur(path,radius=2):
    image = Image.open(path)
    blurImage = image.filter(ImageFilter.GaussianBlur(radius))

    return blurImage

def displayManipulatedImages(path):
    blur = gaussianBlur(path,5)
    gray = toGrayscale(path)

    plot.subplot(1,2,1)
    plot.title("Gaussian Blur")
    plot.imshow(blur)
    plot.axis('off')
    
    plot.subplot(1, 2, 2)
    plot.title("Grayscale") 
    plot.imshow(gray,cmap='gray')
    plot.axis('off')
    
    plot.show()

import numpy as np

def display_histogram(image):
        img=Image.open(image)
        image_array=np.array(img)

        color_channels=('Red', 'Green', 'Blue')
        for i, color in enumerate(color_channels):
            histogram, bin_edges = np.histogram(image_array[:, :, i].flatten(), bins=256, range=(0, 256))
            plot.plot(bin_edges[0:-1], histogram, color=color.lower())
        plot.show()


if __name__=="__main__":
    pth = 'pic.jpg'

    displayImage(pth)
    displayManipulatedImages(pth)
    display_histogram('pic.jpg')