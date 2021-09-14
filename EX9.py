'''
Created on Jul 12, 2019
display image
@author: Chokeunhee
'''

import matplotlib.pyplot as plt
import matplotlib.image as pimg
import numpy as np


def function1(ax):
    global img
    figname = "image0.png"
    img = pimg.imread(figname)
    print(figname, img.shape)
    ax. imshow (img)
    ax. set_title("Original Picture")
    ax.tick_params(color="white", labelbottom=False, labelleft=False)

def function2(ax):
    global img, newimg
    newimg = img[300:340, 180:340]
    print(newimg.shape)
    ax. imshow(newimg)
    ax.set_title("trimming")
    
def function3(ax):
    global img
    figname = "image0.png"
    img = pimg.imread(figname)
    print(figname, img.shape)
    ax. imshow (img)
    ax. set_title("Original Picture")
    ax.tick_params(color="white", labelbottom=False, labelleft=False)
    
def function4(ax):
    global img, newimg
    newimg = img[300:340, 180:340]
    print(newimg.shape)
    ax. imshow(newimg)
    ax.set_title("trimming")
    
    
def function5(ax):
    global img
    figname = "image0.png"
    img = pimg.imread(figname)
    print(figname, img.shape)
    ax. imshow (img)
    ax. set_title("Original Picture")
    ax.tick_params(color="white", labelbottom=False, labelleft=False)
    
def function6(ax):
    global img, newimg
    newimg = img[300:340, 180:340]
    print(newimg.shape)
    ax. imshow(newimg)
    ax.set_title("trimming")

if __name__ == "__main__":
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2,3, figsize=(12,7))
    function1(ax1)
    function2(ax2)
    function3(ax3)
    function4(ax4)
    function5(ax5)
    function6(ax6)
    plt.tight_layout()
    plt.show()