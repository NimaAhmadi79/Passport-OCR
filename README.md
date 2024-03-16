# Passport OCR System

---

## Overview:

This project actually is an image processing for automatic passport information extraction. It aims to develop a Passport OCR (Optical Character Recognition) system that identifies essential fields from passport images, such as surname, passport number, and other pertinent information, and extracts their text for storage in a PostgreSQL database. The system utilizes computer vision techniques, template matching, image preprocessing, and barcode scanning to achieve accurate extraction of information from passport images.

---

**Dependencies**:

The system relies on the following libraries and tools:
- OpenCV
- NumPy
- Matplotlib
- Pyzbar
- Pandas
- MATLAB for additional functionalities

---

**Example of what will be extracted:**

![alt text](https://github.com/NimaAhmadi79/Passport-OCR/blob/master/images%20for%20readme/1.PNG)

---

**Challenges and Solutions:**

Throughout the development, several challenges were encountered, including the need for accurate
character separation, noise management, and dealing with characters stuck together due to noise.
These were overcome through innovative solutions like connected component analysis, custom
thresholding methods, and the development of specialized functions for handling specific cases.

---

**Main Algorithm:**

The primary algorithm employed in this system is Template Matching, which is utilized to locate the position of specific fields within the passport image. Templates are created for each field, and template matching is performed to identify the coordinates of these fields. Additionally, template matching is used to extract characters from the separated fields.

---

**Preparing the Execution Environment:**

The development environment includes VsCode for coding and Jupyter Notebook for testing and exploration. Necessary libraries such as OpenCV, NumPy, and Matplotlib are installed within the environment.

---

**Preprocessing Stages:**

1. Convert photos to grayscale using OpenCV.
2. Invert the pixels of photos.
3. Implement threshold operation on the photos.
4. Normalize photos to adjust pixel values.

sample input after performing preprocessing:

![alt text](https://github.com/NimaAhmadi79/Passport-OCR/blob/master/images%20for%20readme/2.PNG)

---

**Locating Fields with Template Matching:**

Template matching involves rotating templates on the passport image and computing convolutions to identify field coordinates. After preprocessing, templates are separated for each field using software tools, and their coordinates are determined using cv2.TM_CCOEFF.

father's name template:

![alt text](https://github.com/NimaAhmadi79/Passport-OCR/blob/master/images%20for%20readme/3.PNG)

---

**Separating Characters from Fields:**

example of identifying filed and taking it from an image:

![alt text](https://github.com/NimaAhmadi79/Passport-OCR/blob/master/images%20for%20readme/4.PNG)

Characters within fields are separated by performing vertical summation on cropped sections of the image. This process involves adding pixels vertically and identifying character positions based on variations in pixel sums. Techniques such as derivative calculation, threshold determination, and connected components are utilized to minimize errors in character separation.


plot of summation before determining threshold:

![alt text](https://github.com/NimaAhmadi79/Passport-OCR/blob/master/images%20for%20readme/5.PNG)

plot of summation after determining a threshold:

![alt text](https://github.com/NimaAhmadi79/Passport-OCR/blob/master/images%20for%20readme/6.PNG)

---

**Handling Stuck Characters Due to Noise:**

To address issues such as stuck characters due to noise, post-processing techniques are implemented. Functions like check_extract_char, connected components, and hole filling are employed to rectify errors in character separation.

before performing connected components:

![alt text](https://github.com/NimaAhmadi79/Passport-OCR/blob/master/images%20for%20readme/7.PNG)

before performing connected components:

![alt text](https://github.com/NimaAhmadi79/Passport-OCR/blob/master/images%20for%20readme/8.PNG)

---

**Recognizing Separated Characters:**

Separated characters are recognized using template matching against prepared templates of English alphabets. The character with the highest matching score is selected as the recognized character.

---

**Scanning Barcode:**

The system includes a function to scan the barcode present on passports, extracting important information encoded within.

---

**Utilizing Two Parallel Lines at the Bottom of Passports:**

Information present in two parallel lines at the bottom of passports is extracted using summation techniques. The distinct pattern of these lines aids in the accurate extraction of information.


![alt text](https://github.com/NimaAhmadi79/Passport-OCR/blob/master/images%20for%20readme/9.PNG)

---

**Sample Output:**

![alt text](https://github.com/NimaAhmadi79/Passport-OCR/blob/master/images%20for%20readme/10.PNG)

--- 

**References:**

- `Numpy`: https://numpy.org/
- `Pandas`: https://pandas.pydata.org/
- `OpenCV`: https://opencv.org/
- `Pyzbar`: https://pypi.org/project/pyzbar/
- `Matplotlib`: https://matplotlib.org/
- `MATLAB`: https://www.mathworks.com/

**Contributors:**

- Nima Ahmadi


**Contact:**

For any inquiries, please contact Nima87760@gmail.com.





