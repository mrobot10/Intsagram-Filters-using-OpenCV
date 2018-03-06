# Intsagram-Filters-using-OpenCV
Using Python and OpenCV library, I created a function called insta_like() that takes 2 parameters 
1- an image
2- a desired filter
and insta_like() outputs a filtered image of the original one 



We'll implement 5 different instagram filters to an image using opencv, numpy, and matplotlib libraries.

Firslt, I will define several functions that would help us in implementing our main function insta_like()

I will show the histogram of an image which can conclude some info from the image without seeing it just from the histogram

I will use gamma correction that helps us to make an image darker or lighter



We are going to make a histogram function that takes an image and outputs the histogram on image 
(going to be useful sometimes to have more knowledge in contrast and brightness.



Gamma correction function

gamma <1 darker

gamma >1 lighter

O = I^1/G when O: output image

I: input image

G: gamma value

So to apply gamma correction we need first to scale the color range from [0,255] to [0,1.0] then apply the equation above 
then return to the original scale of the colors [0,255].



