import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os


class Getfiles:

   ################################################################## 
   #Get char templates
    def get_char_templates(self):
        #Get templates and assign them to raw_templates array

        raw_templates=[]
        for char in "ABCDEFGHIJKLNMOPQRSTUVWXYZ":
            filename = f"charecters templates/{char}.PNG"
            template=cv2.imread(filename,cv2.IMREAD_COLOR)
            raw_templates.append(template)

        return raw_templates
    
    ###################################################################
    #Get sex templates
    def get_sexs_templates(self):
        #Get  number templates and assign them to raw_templates array

        raw_templates=[]
        for char in "FM":
            filename = f"sexs templates/{char}.PNG"
            template=cv2.imread(filename,cv2.IMREAD_COLOR)
            raw_templates.append(template)

        return raw_templates
    
    
    ##################################################################
    #Get number templates

    def get_numbers_templates(self):
        #Get  number templates and assign them to raw_templates array

        raw_templates=[]
        for char in "0123456789^":
            filename = f"numbers templates/{char}.PNG"
            template=cv2.imread(filename,cv2.IMREAD_COLOR)
            raw_templates.append(template)

        return raw_templates
    
    ###################################################################
    #Read images from folder
    
    def read_images_from_folder(self, folder_path):
        image_dict = {}

        # List all files in the folder
        file_list = os.listdir(folder_path)

        # Loop through each file in the folder
        for file_name in file_list:
            # Check if the file is an image (you can add more image formats as needed)
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(folder_path, file_name)

                # Read the image using OpenCV
                image = cv2.imread(image_path,0)

                # Add the image to the dictionary with the file name as the key
                image_dict[file_name] = image
        
        return image_dict
    
    ################################################################## 