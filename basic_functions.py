import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
from pyzbar.pyzbar import decode

#from extractchar_functions import Extract
from getfiles_functions import Getfiles
#from postprocess_functions import Postprocess
from preprocess_functions import Preprocess
from subsidiary_functions import Subsidiary
#------------------------------------------------#
#extract=Extract()
getfiles=Getfiles()
#post=Postprocess()
pre=Preprocess()
sub=Subsidiary()
#------------------------------------------------#


class Basic:
    ##################################################################
    #Template matching

    def templatematching(self,image,template):
        #Perform template matching on a given image using a specified template    

        # Get the height and width of the template image
        template_height,template_width = template.shape

        # Get the height and width of the input imag
        image_height,image_width=image.shape

        # Define the list of template matching methods to use
        methods=[cv2.TM_CCOEFF]##,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

        # Make a copy of the input image
        copy_img=image.copy()

        for method in methods:

            # Perform template matching using the current method
            result=cv2.matchTemplate(copy_img,template,method)
            
            # Find the location of the best match in the result image
            _,_,min_loc,max_loc=cv2.minMaxLoc(result)

            # Determine the location based on the method used
            if method in [cv2.TM_SQDIFF , cv2.TM_SQDIFF_NORMED]:
                location=min_loc
            else:
                location=max_loc

            # Calculate the coordinates of the top-right the matched region and 
            # #The bottom right corner of the original photo is aligned with the bottom right corner of the photo
            
            pt1=(location[0]+template_width,location[1])
            pt2=(image_width,location[1]+template_height)
            
        return(pt1,pt2,location)
    
    ##################################################################
    #Croping borders of templates           

    def crop_templates(self,template,key):
        #key for identify it is exteracted charecter or template. 1 is for extracted and 0 for templates
        #Perform croping on templates to have charecter Without any border
 
        if(key==0):
            #Transfer template image to grayscale
            template= cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

            #Reversing value of each pixel
            template=pre.revrese(template)

            #Perform theresholfing function with 180 thershhold
            template=pre.thresholding(template,120)
            #perfrom normalization on thersholded template
            template=pre.normalize(template)
        

        #Get height and width of template
        height,width=template.shape
        
        #Perfrom horizontal summation on this template 
        horizontal_sum_array=sub.horizontal_summation(template)

        #Perfrom vertical summation on this template
        vertical_sum_array=sub.vertical_summation(template)


        start_width=0 #index of start of width charecter in raw template
        end_width=0 #index of end of width charecter in raw template
        start_height=0 #index of start of height charecter in raw template
        end_height=0 #index of end of height charecter in raw template


        #Find index of start charecter in the horizontal direction
        for i in range(len(vertical_sum_array)):
            if(vertical_sum_array[i+1]>0):
                start_width=i+1
                break

        #Find index of end charecter in the horizontal direction        
        for i in range(len(vertical_sum_array)):

            if(i==(len(vertical_sum_array))-1):
                end_width=i 
                break

            if(vertical_sum_array[i]>0 and vertical_sum_array[i+1]==0):
                end_width=i+1     
                break

        #Find index of start charecter in the vertical direction             
        for i in range(len(horizontal_sum_array)):
            if(horizontal_sum_array[i+1]>0):
                start_height=i+1  
                break 

        #Find index of end charecter in the vertical direction         
        for i in range(len(horizontal_sum_array)):

            if(i==(len(horizontal_sum_array))-1):
                end_height=i 
                break

            if(horizontal_sum_array[i]>0 and horizontal_sum_array[i+1]==0):
                end_height=i+1   
                break                

        #Removing borders from raw_template        
        tele_template=template[start_height:end_height,start_width:end_width]
        return tele_template

    #################################################################

    def find_char(self,chars_iamge,templates_image):
        array_of_matched=[]

        value_of_each_char=[]
        
        for char in chars_iamge:
            #first index is a unkonw char ,second is max value conv, and third is a templated that is matched
            maximum=(None,0,None)
            
            temp=(0,0,None)
            value_of_each_template=[]
            i=0

            for i,template in enumerate(templates_image):
                result=cv2.matchTemplate(char,template,cv2.TM_CCOEFF)
                temp_max=np.max(result)
                if temp_max > maximum[1]:

                    maximum=(char,temp_max,template,i)



                temp=(temp_max,i,result)
                value_of_each_template.append(temp)
                i=i+1   
            value_of_each_template.sort()
            value_of_each_char.append(value_of_each_template)     


                    

            array_of_matched.append(maximum)
                

        return array_of_matched,value_of_each_char    
    
    #################################################################

    def scan_barcodes(self,image):
        
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #perform theresholding 
        thresholded_img=pre.thresholding(gray,120)

        # Use ZBar to detect and decode barcodes
        barcodes = decode(thresholded_img)

        # Print the barcode data
        for barcode in barcodes:
            data = barcode.data.decode("utf-8")

        return data    
