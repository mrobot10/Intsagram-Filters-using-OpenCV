import cv2
import numpy as np
from matplotlib import pyplot as plt

original = cv2.imread('image.format', cv2.IMREAD_UNCHANGED)
original_img = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
plt.imshow(original_img)
plt.show()
#--------------------------------------------
def histogram(image):
    color = ('b', 'g', 'r')
    for i,col in enumerate(color):
        hist = cv2.calcHist([image], [i] , None, [256], [0,256]) 
        plt.plot(hist, color = col)
        plt.xlim([0,256])
    plt.show()

#---------------------------------------------
histogram(original_img)
#-----------------------------------------------
def adjust_gamma(image, gamma = 1.0):
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, table)
#-----------------------------------------------
#Just to test gamma correction
#can be used to manipulate the image to apply a certain filter
gamma_darker = adjust_gamma(original_img, 0.3)
plt.imshow(gamma_darker)
plt.show()
gamma_lighter = adjust_gamma(original_img, 2)
plt.imshow(gamma_lighter)
plt.show()
#--------------------------------------------
def blur(image, matrix):
    blurred_image = cv2.blur(image, matrix)
    return blurred_image
#---------------------------------------------

def sharpen(image):
       kernal = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
       sharpened_image = cv2.filter2D(image, -1, kernal)
       return sharpened_image
#------------------------------------------------
blurred = blur(original_img, (5,5))  #just for testing the blur() function
plt.imshow(blurred)
plt.show()
#--------------------------------------------------
sharpened = sharpen(original_img) #just for testing the sharpen() function
plt.imshow(sharpened)
plt.show()
#---------------------------------------------------
def split_image(image):
    red = image[:, :, 2]
    green = image[:, :, 1]
    blue = image[:, :, 0]
    return red, green, blue
#---------------------------------------------------
def merge_image(red_channel, green_channel, blue_channel):
    image_merged = cv2.merge((red_channel, green_channel, blue_channel))
    return image_merged
#----------------------------------------------------
def darkness_brightness(image, operation, x):
    matrix = np.ones(image.shape, dtype="uint8") * x
    if operation == "add":
        brighter = cv2.add(image, matrix)
        return brighter
    elif operation == "sub":
        darker= cv2.subtract(image, matrix)
        return darker
    else: 
        print("Enter add or sub only!")
#----------------------------------------------------
x = darkness_brightness(original_img, "sub", 100)
y = darkness_brightness(original_img, "add", 100)
plt.imshow(x)
plt.show()
plt.imshow(y)
plt.show()

#--------------------------------------------------------
def insta_like(image, chosen_filter):
    if chosen_filter == "lily":
        blurred = blur(original_img, (5, 5))
        r1, g1, b1 = split_image(blurred)
        g_adjusted = darkness_brightness(g1, "add", 0)
        b_adjusted = darkness_brightness(b1, "sub", 255)
        lily = merge_image(r1, g_adjusted, b_adjusted)
        lily1 = darkness_brightness(lily, "add", 90)
        plt.imshow(lily1)
        plt.show()


    elif chosen_filter == "toaster":
        r2, g2, b2 = split_image(original_img)
        r_adjusted1 = darkness_brightness(r2, "add", 55)
        g_adjusted1 = darkness_brightness(g2, "add", 40)
        b_adjusted1 = darkness_brightness(b2, "sub", 10)
        toaster = merge_image(r_adjusted1, g_adjusted1, b_adjusted1)
        toaster_brighter = darkness_brightness(toaster, "add", 25)
        plt.imshow(toaster_brighter)
        plt.show()


    elif chosen_filter == "nashville":
        blurred = blur(original_img, (1, 1))
        rw, gw, bw = split_image(blurred)
        rw_adjusted = darkness_brightness(rw, "add", 30)
        gw_adjusted = darkness_brightness(gw, "add", 40)
        bw_adjusted = darkness_brightness(bw, "add", 0)
        merged_nash = merge_image(rw_adjusted, gw_adjusted, bw_adjusted)
        lighter_nash = adjust_gamma(merged_nash, 2.8)
        plt.imshow(lighter_nash)
        plt.show()

    elif chosen_filter == "lord kelvin":
        r3, g3, b3 = split_image(original_img)
        r3_adjusted = darkness_brightness(r3, "add", 100)
        g3_adjusted = darkness_brightness(g3, "add", 11)
        b3_adjusted = darkness_brightness(b3, "sub", 67)
        kelvin = merge_image(r3_adjusted, g3_adjusted, b3_adjusted)
        plt.imshow(kelvin)
        plt.show()


    elif chosen_filter == "hefe":

        r4, g4, b4 = split_image(original_img)
        b4_adjusted = adjust_gamma(b4, 0.4)
        r4_adjusted = adjust_gamma(r4, 3)
        g4_adjusted = adjust_gamma(g4, 1.3)
        hefe = merge_image(r4_adjusted, g4_adjusted, b4_adjusted)
        hefe_lighter = adjust_gamma(hefe, 2)
        plt.imshow(hefe_lighter)
        plt.show()


    else:
        print("ERROR!! Enter 1 of the 5 filters in our app!")
#------------------------------------------------------------
insta_like(original_img, "lily")
insta_like(original_img, "toaster")
insta_like(original_img, "nashville")
insta_like(original_img, "lord kelvin")
insta_like(original_img, "hefe")