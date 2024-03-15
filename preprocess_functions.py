import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# from extractchar_functions import Extract
# from getfiles_functions import Getfiles
# from postprocess_functions import Postprocess
#from basic_functions import Basic
from subsidiary_functions import Subsidiary
#------------------------------------------------#
# extract=Extract()
# getfiles=Getfiles()
# post=Postprocess()
#basic=Basic()
sub=Subsidiary()
#------------------------------------------------#

class Preprocess:

    ##################################################################

    def remove_noise_edge(self,image,ver_sum,hor_sum):
        size_ver_sum=len(ver_sum)
        size_hor_sum=len(hor_sum)
        s_w=0
        e_w=0
        s_h=0
        e_h=0
        exit=False
        for i in range(size_ver_sum):
            if ver_sum[i]<10:
                for j in range(4):
                    if ver_sum[i+j]>10:
                        break
                    if(j==3):
                        s_w=i
                        exit=True
                if exit:
                    break        

        exit=False  
        revers_ver=ver_sum[::-1]
        for i in range(size_ver_sum):
            if revers_ver[i]<10:
                for j in range(4):
                    if revers_ver[i+j]>10:
                        break
                    if(j==3):
                        e_w=size_ver_sum-i
                        exit=True
                if exit:
                    break 

        exit=False
        for i in range(size_hor_sum):
            if hor_sum[i]<30:
                for j in range(4):
                    if hor_sum[i+j]>30:
                        break
                    if(j==3):
                        s_h=i
                        exit=True
                if exit:
                    break  


        exit=False
        revers_hor=hor_sum[::-1]
        for i in range(size_hor_sum):
            if revers_hor[i]<30:
                for j in range(4):
                    if revers_hor[i+j]>30:
                        break
                    if(j==3):
                        e_h=size_hor_sum-i
                        exit=True
                if exit:
                    break 


        crop=image[s_h:e_h,s_w:e_w]
        crop_ver_sum=ver_sum[s_w:e_w]
        crop_hor_sum=hor_sum[s_h:e_h]
        return crop,crop_ver_sum,crop_hor_sum

    
    ##################################################################
    #Reversing

    def revrese(self,img):
        #Reverse the colors of a given grayscale image.

        # Get the number of rows and columns in the input image
        row ,column=img.shape
        # Create an image filled with 255 (white) of the same size as the input image
        image_of_255=np.ones((row, column),dtype=np.uint8)*255

        # Subtract the input image from the all-white image to reverse the colors
        # The cv2.subtract function subtracts the pixel values element-wise
        reversed_image=cv2.subtract(image_of_255, img)
    
        return reversed_image
    
    ##################################################################
    #Thresholding with custom thresh

    def thresholding(self,img,thresh):
        #Perform binary thresholding on a given grayscale image and convert pixel to 255 or 0

        # Define the threshold value (pixel intensity value) to be used for thresholding
        threshold_value =thresh
        # max=np.max(reversed_image)
        # min=np.min(reversed_image)
    
        # Apply binary thresholding to the input image
        _, thresholded_image = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
    
        return thresholded_image

    ##################################################################
    #Normalization   

    def normalize(self,img):
        #perform normalization and transfer the amount of each pixel between 0 abd 1
        normalized_img = cv2.normalize(img, None, 0, 1.0,cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        # cv2.imshow("img_normalized",normalized_img )
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return normalized_img

    ##################################################################
    #binary thresholding for array

    def binary_thresh_array(self,array,thresh):
        # Manual function to perform thersholidng on an array

        for i in range(len(array)):
            if array[i]>thresh:
                array[i]=1
            else:
                array[i]=0
        return array 
    
    ##################################################################
    #thresholding image with custom value for thresh between 1 and 0
    
    def binary_threshold(self,image,threshold):
        
        # Perform thresholding 1
        _, thresholded_image = cv2.threshold(image, threshold, 1, cv2.THRESH_BINARY)
        
        return thresholded_image
    
    ##################################################################
    #Padding     

    def padding(self,original_image,target_height,target_width):
        #perform padding operation to specific height and width

        height, width = original_image.shape
        pad_height = max(target_height - height, 0)
        pad_width = max(target_width - width, 0)
        top_pad = pad_height // 2
        bottom_pad = pad_height - top_pad
        left_pad = pad_width // 2
        right_pad = pad_width - left_pad
        padded_image = cv2.copyMakeBorder(
        original_image, top_pad, bottom_pad, left_pad, right_pad, cv2.BORDER_CONSTANT, value=0)
        scaled_image = 255 * padded_image
        scaled_image = np.clip(scaled_image, 0, 255)
        uint8_image = scaled_image.astype(np.uint8)
        
        return uint8_image
    
    ##################################################################
    #Reduce quality

    def reduce_image_quality(self,image_path, output_path, compression_quality):
        # Read the image using OpenCV
        image = cv2.imread(image_path)

        # Get the file extension of the input image
        file_extension = image_path.split('.')[-1]

        # Parameters for saving the image with compression quality (for JPEG format)
        if file_extension.lower() in ['jpg', 'jpeg']:
            compression_params = [cv2.IMWRITE_JPEG_QUALITY, compression_quality]

            # Save the image with compression quality
            cv2.imwrite(output_path, image, compression_params)

        # For other formats like PNG, simply save the image without compression quality adjustment
        else:
            cv2.imwrite(output_path, image)  

    ##################################################################
    #Check quality

    def amount_of_quality(self,image):

        #calculate image quality 
         
        #Convert iamge forat to unit8
        image=image.astype(np.uint8)

        #Define a laplacian window 
        window=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

        #Get Conv2D from image with laplacian window detecte edges
        result = cv2.filter2D(image, -1,window)

        #Normalization because if we dont do that after summation value of each index will be very larg
        normalized_result = cv2.normalize(result, None, 0, 1.0,cv2.NORM_MINMAX, dtype=cv2.CV_32F)

        #Get hight and width of normalized_result
        row ,column=normalized_result.shape

        #Get summation of each row
        sum=0
        sum_of_row_array=[]
        for i in range(row):
            for j in range(column):
                sum=sum+normalized_result[i][j]

            sum_of_row_array.append(sum)
            sum=0    

        #Round numbers of sum_of_row_array to 1 decimal places
        sum_of_row_array=np.round(sum_of_row_array, 1)

        #Get summation of sum_of_row_array
        sum=0
        for i in range(len(sum_of_row_array)):
            sum=sum+sum_of_row_array[i]  

        #Round numbers to 1 decimal
        sum=np.round(sum,1)  
        return sum  

    ##################################################################
    #Resizing input image

    def resize(self,image,target_height,target_width):
        resized_image = cv2.resize(image, (target_width, target_height))
        return resized_image
    
    ##################################################################
    #Equalize DPI

    def equalize_dpi(self,image):
        copy_image=image.copy()
        copy_image=self.revrese(copy_image)
        _, copy_image = cv2.threshold(copy_image, 130, 255, cv2.THRESH_BINARY)
        copy_image=self.normalize(copy_image)

        ver_sum=sub.vertical_summation(copy_image)
        hor_sum=sub.horizontal_summation(copy_image)
        crop_image,crop_ver_sum,crop_hor_sum=self.remove_noise_edge(copy_image,ver_sum,hor_sum)
        T_crop_ver_sum=self.binary_thresh_array(crop_ver_sum,8)
        T_crop_hor_sum=self.binary_thresh_array(crop_hor_sum,10)
        cut_for_sw=0
        cut_for_ew=0
        cut_for_sh=0
        cut_for_eh=0

        for i in range(len(T_crop_ver_sum)):
            if(T_crop_ver_sum[i]==0):
                if T_crop_ver_sum[i+1]==1 and T_crop_ver_sum[i+2]==1 and T_crop_ver_sum[i+3]==1 and T_crop_ver_sum[i+4]==1:
                    cut_for_sw=i
                    break

        rev_ver=T_crop_ver_sum[::-1]
        for i in range(len(T_crop_ver_sum)):
            if(rev_ver[i]==0):
                if rev_ver[i+1]==1 and rev_ver[i+2]==1 and rev_ver[i+3]==1 and rev_ver[i+4]==1:
                    cut_for_ew=(len(T_crop_ver_sum ))-i
                    break

        for i in range(len(T_crop_hor_sum)):
            if(T_crop_hor_sum[i]==0):
                if T_crop_hor_sum[i+1]==1 and T_crop_hor_sum[i+2]==1 and T_crop_hor_sum[i+3]==1 and T_crop_hor_sum[i+4]==1:
                    cut_for_sh=i
                    break

        rev_hor=T_crop_hor_sum[::-1]
        for i in range(len(T_crop_hor_sum)):
            if(rev_hor[i]==0):
                if rev_hor[i+1]==1 and rev_hor[i+2]==1 and rev_hor[i+3]==1 and rev_hor[i+4]==1:
                    cut_for_eh=(len(T_crop_hor_sum ))-i
                    break

        tele=image[cut_for_sh:cut_for_eh,cut_for_sw:cut_for_ew]
        tele_height=tele.shape[0]
        tele_width=tele.shape[1]
        factor_height=619/tele_height
        factor_width=988/tele_width
        resized_tele_image=self.resize(tele,int((tele_height*factor_height)),int((tele_width*factor_width)))
        return resized_tele_image
    
    ##################################################################
    
    def remove_noise(self,image,limit):
    
        # Apply connected component labeling
        num_labels, labels = cv2.connectedComponents(image)

        # Calculate the size of each connected component
        component_sizes = np.bincount(labels.flatten())

        for i,j in enumerate(component_sizes):
            if j<limit:
                for u in range(labels.shape[0]):
                    for y in range(labels.shape[1]):
                        if labels[u,y]==i:
                            labels[u,y]=0

        for u in range(labels.shape[0]):
            for y in range(labels.shape[1]):
                        if labels[u,y]!=0:
                            labels[u,y]=255
                    
        labels=labels.astype(np.uint8)    
            
        return labels
    
    ##################################################################
    
    def check_iamge_quality(self,image,threshold):
        quality=self.amount_of_quality(image)
        if quality is not None and quality < threshold:
            raise ValueError("The quality of the image is low.Program terminated.")
        else:
            pass