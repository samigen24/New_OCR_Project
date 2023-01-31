import imgp

from pdf2image import convert_from_path
pages = convert_from_path(r'../resources/docs/receipt.pdf', poppler_path = r"C:\poppler-22.12.0\Library\bin")
# pages[0].show()
img = imgp.preprocess_image(pages[0])
# Image.fromarray(img).show()

# Extract Name, Semester, year, degree, class, date


import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(img, lang='eng')
# print(text)


import re

pattern1 = "Name \(Surname First\): (.*)"
match1 = re.findall(pattern1, text)
print(match1[0].strip())

pattern2 = "Matric No.\/Reg. No.: (\d{9})"
match2 = re.findall(pattern2, text)
print(match2[0].strip())

patter3 = "Department: (.*)"
match3 = re.findall(patter3, text)
print(match3[0].strip())

pattern4 = "Faculty: (.*)Session"
match4 = re.findall(pattern4, text)
print(match4[0].strip())







