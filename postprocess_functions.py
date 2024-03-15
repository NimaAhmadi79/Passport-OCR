import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

from subsidiary_functions import Subsidiary
#------------------------------------------------#
sub=Subsidiary()
#------------------------------------------------#


class Postprocess:

    ########################################################

    def check_I_T(self,unknown_char):
        filled_char=sub.fill_hole_vertical(unknown_char)
        # cv2.imshow("kk",filled_char)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        area= np.sum(filled_char)
        if area<=1800:
            return False
        else:
            return True
        
    ########################################################    