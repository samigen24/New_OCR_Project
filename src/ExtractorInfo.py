# Here we'll be combining our extractor and parser

# responsible for extracting data from pdf
# let's convert pdf to image

# 1. fetch the pdf file and convert to image
from pdf2image import convert_from_path
import pytesseract  # this module converts image to text
# from PIL import Image
# import numpy as np
# import cv2
import imgp

from parser_student_info import StudentInfo


POPPLER_PATH = r"C:\poppler-22.12.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# colorful image -- gray -- resized -- adaptive threshold
# create a function for processing the image after pdf conversion before we read the text


def extract(file_path, file_format):
    # step 1: extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    # pages is an array of PIL images, i.e a bunch of images....stores the image file
    # you'll get image per pdf page...
    document_text = ''
    if len(pages) > 0:
        page = pages[0]
        processed_image = imgp.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    #return document_text

    # step 2: using parser to determine extraction of text
    if file_format == 'receipt':
        extracted_data = StudentInfo(document_text).parse()   # pass    # extract data from prescription
    else:
        raise Exception("Invalid document format: {file_format}")

    return extracted_data

# file location


if __name__ == '__main__':
    data = extract('../resources/docs/receipt.pdf', 'receipt')
    print(data)
