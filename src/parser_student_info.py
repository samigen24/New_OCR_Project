from New_OCR_Project.src.parser_generic import Registration

import re

class StudentInfo(Registration):
    def __init__(self, text):
        Registration.__init__(self, text)

    def parse(self):
        return{
            'student_name': self.get_name(),
            'student_matric_no': self.get_matric_no(),
            'student_dept': self.get_department(),
            'student_faculty': self.get_faculty()

        }

    def get_name(self):
        pattern = "Name \(Surname First\): (.*)"
        match = re.findall(pattern, self.text)
        if len(match) > 0:
            return match[0].strip()

    def get_matric_no(self):
        pattern = "Matric No.\/Reg. No.: (\d{9})"
        match = re.findall(pattern, self.text)
        if len(match) > 0:
            return match[0].strip()

    def get_department(self):
        patter = "Department: (.*)"
        match = re.findall(patter, self.text)
        if len(match) > 0:
            return match[0].strip()

    def get_faculty(self):
        pattern = "Faculty: (.*)Session"
        match = re.findall(pattern, self.text)
        if len(match) > 0:
            return match[0].strip()




