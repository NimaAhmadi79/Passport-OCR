import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os


from basic_functions import Basic
from getfiles_functions import Getfiles
from postprocess_functions import Postprocess
from preprocess_functions import Preprocess
from subsidiary_functions import Subsidiary
#------------------------------------------------#
basic=Basic()
getfiles=Getfiles()
post=Postprocess()
pre=Preprocess()
sub=Subsidiary()
#------------------------------------------------#

class Extract:

    ##############################################################

    def find_cut_avg(self,derivative,cut_index_arr):

        help=0 
        
        for i in range(len(derivative)):
            if(help>60):
                break
            if(derivative[i]==0):
                help=help+1
            if(derivative[i]!=0):
                help=0

            if (derivative[i]==1):
                f_index=i
                for j in range(i,len(derivative)):
                    if (derivative[j])==-1:
                        e_index=j
                        cut_index_arr.append(f_index)
                        cut_index_arr.append(e_index+2)
                        break

        for i in range(len(cut_index_arr)):
            if(i==len(cut_index_arr)-1):
                break
            if(i%2!=0):
                start=cut_index_arr[i]
                end=cut_index_arr[i+1]
                avrage=(start+end)/2
                avrage=np.round(avrage,decimals=0)
                avrage=int(avrage)
                cut_index_arr[i]=avrage
                cut_index_arr[i+1]=avrage+1  

    ##############################################################

    def check_extract_char(self,char_image):
        
        char_height,char_width=char_image.shape
        separated_char=[]
        if char_width<30:
            separated_char.append(char_image)
            return True,separated_char
        else:
            copy=char_image.copy()
            filled=sub.fill_hole(copy)
            ver_sum=sub.vertical_summation(filled)
            max=ver_sum.max()
            threshhold=(max/2)-3 
            ver_sum_th=pre.binary_thresh_array(ver_sum,threshhold)
            derative=sub.deriv(ver_sum_th)
            cut_index=[]
            self.find_cut_avg(derative,cut_index)
            for i in range(0,len(cut_index)):
                if(i%2==0):
                    char = char_image[1:char_height,cut_index[i]:cut_index[i+1]]
                    separated_char.append(char)
        
            return False,separated_char

    ##############################################################

    def find_cut_for_lines(self,derivative,cut_index_arr):
    
        for i in range(len(derivative)):
        
            if (derivative[i]==1):
                f_index=i
                for j in range(i,len(derivative)):
                    if (derivative[j])==-1:
                        e_index=j
                        cut_index_arr.append(f_index)
                        cut_index_arr.append(e_index+2)
                        break

        for i in range(len(cut_index_arr)):
            if(i==len(cut_index_arr)-1):
                break
            if(i%2!=0):
                start=cut_index_arr[i]
                end=cut_index_arr[i+1]
                avrage=(start+end)/2
                avrage=np.round(avrage,decimals=0)
                avrage=int(avrage)
                cut_index_arr[i]=avrage
                cut_index_arr[i+1]=avrage+1 

    ##############################################################

    def find_cut(self,derivative,cut_index_arr):

        help=0 
        
        for i in range(len(derivative)):
            if(help>60):
                break
            if(derivative[i]==0):
                help=help+1
            if(derivative[i]!=0):
                help=0

            if (derivative[i]==1):
                f_index=i
                for j in range(i,len(derivative)):
                    if (derivative[j])==-1:
                        e_index=j
                        cut_index_arr.append(f_index)
                        cut_index_arr.append(e_index+2)
                        break

    ##############################################################

    def extract_charecter(self,rectangled_image):  
        rec_height,rec_width=rectangled_image.shape
        vertical_sum=sub.vertical_summation(rectangled_image)
    
        vertical_sum_thresh=pre.binary_thresh_array(vertical_sum,1)
     
        cut_index_array=[]
        der=sub.deriv(vertical_sum_thresh)
        self.find_cut(der,cut_index_array)
        image_of_character=[]
        for i in range(0,len(cut_index_array)):
            if(i%2==0):
                char = rectangled_image[1:rec_height,cut_index_array[i]:cut_index_array[i+1]]
                should_seprate,seprated_char=self.check_extract_char(char)
                if should_seprate:
                    image_of_character.append(seprated_char[0])
                else:
                    for j in range(len(seprated_char)):
                        image_of_character.append(seprated_char[j])
                        
        return image_of_character,vertical_sum_thresh,cut_index_array,der