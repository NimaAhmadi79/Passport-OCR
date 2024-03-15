import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

class Subsidiary:

    ##################################################################
    #Check size of area
    
    def check_size_of_area(self,image,limit):
        h,w=image.shape
        area_size=w*h
        if area_size<int(limit):
            return False
        else:
            return True   
        
    ##################################################################
    #Convert pixels 0 to negative 1

    def convert_zero(self,image):
        h,w=image.shape
        for row in range(h):
            for column in range(w):
                if image[row,column]==0:
                    image[row,column]=-1

        return image    
    
    ##################################################################  
    #derivative

    def deriv(self,arr):
        arr_copy = arr.copy()
        arr = np.append(arr, 0)
        arr_copy = np.insert(arr_copy, 0, 0)
        
        derivative=arr-arr_copy
        size=len(derivative)
        derivative=derivative[1:size-1]
        return derivative
    
    ################################################################## 
    #Vertical summation
    
    def vertical_summation(self,image_array):
        #perform vertical summation 

        height,width=image_array.shape
        #create array for summation of each column
        vertical_sum_array=np.zeros(width)
        for column in range(width):
            sum=0
            for row in range(height):              
                sum=sum+image_array[row,column]
            vertical_sum_array[column]=sum   
            
        return vertical_sum_array
    
    ##################################################################
    #Horizontal summation
    
    def horizontal_summation(self,image_array):
        #perform vertical summation 
        
        height,width=image_array.shape
        #create array for summation of each column
        horizontal_sum_array=np.zeros(height)
        for row in range(height):
            sum=0
            for column in range(width):
                sum=sum+image_array[row,column]

            horizontal_sum_array[row]=sum  
            
        return horizontal_sum_array
    
    ##################################################################
    
    def fill_hole_vertical(self,image):
        for col in range(image.shape[1]):
            start_row = None
        
            # Scan from top to bottom
            for row in range(image.shape[0]):
                # Find the first white pixel
                if image[row, col] == 1:
                    if start_row is None:
                        start_row = row
                    else:
                        # Fill the gap between the two white pixels
                        image[start_row+1:row, col] = 1
                        start_row = row
        return image

    ##################################################################

    def fill_hole_horizontal(self,image):

        for row in range(image.shape[0]):
            start_col = None
            # Scan from left to right
            for col in range(image.shape[1]):
                if image[row, col] == 1:
                    if start_col is None:
                        start_col = col

                    else:

                        image[:, start_col+1] = 1
                        start_col = col

        return image 

    ##################################################################

    def fill_hole(self,image):
        h, w = image.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)
        copy=image.copy()

        cv2.floodFill(copy, mask, (0,0), 1)
        h,w=copy.shape
        for row in range(h):
            for col in range(w):
                pixel=copy[row,col]
                if pixel==0:
                    copy[row,col]=1
                else:
                    copy[row,col]=0    
                    
        
        corrected_image=image+copy


        return corrected_image      