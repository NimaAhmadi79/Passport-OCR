**Passport Information Extraction System**

This repository contains the implementation of a Passport Information Extraction System developed as a part of a project. The system is designed to extract essential fields from passport images using various image processing and optical character recognition (OCR) techniques. Ultimately it stores and saves them in a database. Below is an overview of the system's functionality and components.

### Overview

The Passport Information Extraction System comprises several modules:

1. **Image Preprocessing**: This module involves preprocessing passport images to enhance readability and improve OCR accuracy. Techniques such as noise reduction, contrast enhancement, and resizing are applied to prepare the images for further processing.

2. **Character Segmentation**: Passport images are processed to identify and separate word characters.

3. **Character Recognition**: The isolated characters are then recognized using template matching techniques. Templates for English alphabets are used to match and identify each character.

4. **Quality Assessment**: A quality assessment mechanism is implemented to evaluate the sharpness and clarity of the passport images. This assessment helps in determining the overall quality of the images and their suitability for OCR.

5. **Error Detection**: Special attention is given to detecting and correcting errors, particularly in identifying the letter "I" which can be mistaken for other characters.

6. **Barcode Scanning**: The system includes a module for scanning and decoding barcodes present on the passport. This is useful for extracting additional information such as the national identification number.

7. **Bottom Lines Extraction**: Information present in the bottom lines of the passport, including passport number, expiration date, name, and gender, is extracted using horizontal summation and peak detection techniques.

8. **Post-processing**: Post-processing involves refining the extracted information and handling errors. Confidence scores are assigned to extracted text, and a mapping mechanism is employed to match extracted names with entries in a predefined database.

### Result

The system demonstrates robust performance in extracting passport information accurately from input images. The extracted information includes personal details, passport numbers, expiration dates, and other relevant data.



### Dependencies

The system relies on the following libraries and tools:
- OpenCV
- NumPy
- Matplotlib
- Pyzbar
- VsCode for debugging
- MATLAB for some additional functionalities

### Usage

To use the system, follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Run the main script with the passport image as input.
4. Review the extracted information from the output.

### Conclusion

The Passport Information Extraction System offers a reliable solution for automating the extraction of information from passport images. It demonstrates the application of various image processing and OCR techniques to achieve accurate results. Further enhancements and optimizations can be implemented for specific use cases and requirements.

For any inquiries or suggestions, feel free to contact Nima87760@gmail.com.



