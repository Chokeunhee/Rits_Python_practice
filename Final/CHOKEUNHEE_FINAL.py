'''
Created on Jul 17, 2019
1. Displaying Original picture (image0.png)
2. trimming picture (to see only the bear)
3. Visualization of Published data (Programming Language ratings)
    - Source: www.tiobe.com
4. Changing Image using image filter (Contour)
5. Changing Image using image filter (EMBOSS)
6. Parametric equation, the butterfly curve
@author: Chokeunhee
'''
import matplotlib.pyplot as plt
import matplotlib.image as pimg
import numpy as np
from PIL import Image, ImageFilter

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
    newimg = img[130:280, 80:250]
    print(newimg.shape)
    ax. imshow(newimg)
    ax.set_title("trimming")
    ax.tick_params(color="white", labelbottom=False, labelleft=False)
    
def function3(ax):
    A1 = np.array([18,19,17,18,16,14,22,15,18])
    A2 = np.array([16,15,16,20,18,16,17,9,12])
    A3 = np.array([5,6,4,5,2,4,4,5,8])
    A4 = np.array([10,9,8,10,7,4,7,5,4])
    A5 = np.array([10,7,5,6,2,3,2,3,1])
    year = np.arange(2010,2019)
    ax.plot(year,A1,'r',label="Java",marker='^')
    ax.plot(year,A2,'g',label="C",marker='.')
    ax.plot(year,A3,'b',label="Python",marker='*')
    ax.plot(year,A4,'pink',label="C++",marker='+')
    ax.plot(year,A5,'black',label="PHP",marker='v')
    ax.legend()
    ax.set_xlabel("Year")
    ax.set_ylabel("Ratings(%)")
    ax.set_title("Programming Languages ratings (Source: www.tiobe.com)")
    
def function4(ax):
    img = Image.open("image0.png")
    img2 =img.filter(ImageFilter.CONTOUR)
    ax.imshow(img2)
    ax.set_title("Image Filter: Contour")
    ax.tick_params(color="white", labelbottom=False, labelleft=False)
     
def function5(ax):
    img = Image.open("image0.png")
    img2 =img.filter(ImageFilter.EMBOSS)
    ax.imshow(img2)
    ax.set_title("Image Filter: EMBOSS")
    ax.tick_params(color="white", labelbottom=False, labelleft=False)
   
def function6(ax):
    t = np.linspace(0,30,1000)
    x = 100*(np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t/12)**5))
    y = 100*(np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t/12)**5))
    ax.plot(x,y)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Butterfly curve")
               
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