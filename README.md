# Passport OCR System

---

## Overview:

This project actually is an image processing for automatic passport information extraction. It aims to develop a Passport OCR (Optical Character Recognition) system that identifies essential fields from passport images, such as surname, passport number, and other pertinent information, and extracts their text for storage in a PostgreSQL database. The system utilizes computer vision techniques, template matching, image preprocessing, and barcode scanning to achieve accurate extraction of information from passport images.

---

### Dependencies:

The system relies on the following libraries and tools:
- OpenCV
- NumPy
- Matplotlib
- Pyzbar
- Pandas
- MATLAB for additional functionalities

---

**Example of what will be extracted:**

[Insert sample image showcasing extracted passport information]

---

### Challenges and Solutions

Throughout the development, several challenges were encountered, including the need for accurate
character separation, noise management, and dealing with characters stuck together due to noise.
These were overcome through innovative solutions like connected component analysis, custom
thresholding methods, and the development of specialized functions for handling specific cases.

---

### Main Algorithm:

The primary algorithm employed in this system is Template Matching, which is utilized to locate the position of specific fields within the passport image. Templates are created for each field, and template matching is performed to identify the coordinates of these fields. Additionally, template matching is used to extract characters from the separated fields.

---

### Preparing the Execution Environment:

The development environment includes VsCode for coding and Jupyter Notebook for testing and exploration. Necessary libraries such as OpenCV, NumPy, and Matplotlib are installed within the environment.

---

### Preprocessing Stages:

1. Convert photos to grayscale using OpenCV.
2. Invert the pixels of photos.
3. Implement threshold operation on the photos.
4. Normalize photos to adjust pixel values.

[Insert image showing the result after preprocessing steps]

---

### Locating Fields with Template Matching:

Template matching involves rotating templates on the passport image and computing convolutions to identify field coordinates. After preprocessing, templates are separated for each field using software tools, and their coordinates are determined using cv2.TM_CCOEFF.

[Insert sample image of a template]

---

### Separating Characters from Fields:

[Insert images illustrating character separation process]

Characters within fields are separated by performing vertical summation on cropped sections of the image. This process involves adding pixels vertically and identifying character positions based on variations in pixel sums. Techniques such as derivative calculation, threshold determination, and connected components are utilized to minimize errors in character separation.

[Insert images illustrating character separation process]


[Insert images illustrating character separation threshold]

---

### Handling Stuck Characters Due to Noise:

To address issues such as stuck characters due to noise, post-processing techniques are implemented. Functions like check_extract_char, connected components, and hole filling are employed to rectify errors in character separation.

[befor connected]
[after connected]

---

### Recognizing Separated Characters:

Separated characters are recognized using template matching against prepared templates of English alphabets. The character with the highest matching score is selected as the recognized character.

---

### Scanning Barcode:

The system includes a function to scan the barcode present on passports, extracting important information encoded within.

---

### Utilizing Two Parallel Lines at the Bottom of Passports:

Information present in two parallel lines at the bottom of passports is extracted using summation techniques. The distinct pattern of these lines aids in accurate extraction of information.

[Insert image of the two parallel lines]

---

### Sample Result:

[Insert sample image showcasing the extracted information from a passport]

---

This README provides an overview of the Passport OCR System, outlining its functionality, dependencies, and processing stages. For detailed implementation instructions and usage guidelines, please refer to the documentation within the repository.


