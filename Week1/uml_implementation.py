#!usr/bin/env python3

__author__ = "Lisa Hu"
__version__ = 2.0

from datetime import datetime
import string
from random import randint, choices, shuffle


class InvalidDateFormat(Exception):
    """
    Custom error for invalid date format
    """
    def __init__(self):
        self.__message = "Date format is invalid. Please follow the following format: yyyymmdd"
        super().__init__(self.__message)

    def __str__(self):
        return self.__message


class ValidationError(Exception):
    """
    Custom error for incorrect password
    """
    def __init__(self):
        self.__message = "Password incorrect"
        super().__init__(self.__message)

    def __str__(self):
        return self.__message


class Student:
    """
    Student object for storing information over the student.
    """
    def __init__(self, first_name: str, family_name: str, birth_date: str):
        """
        Initializing student object
        :param first_name: First name of the student
        :param family_name: Last name of the student
        :param birth_date: Date of birth of the student
        """
        self.__student_id = self.__generate_id()
        self.__first_name = first_name
        self.__last_name = family_name
        self.__birth = birth_date
        self.__age = self.get_age()
        self.__studies = list()
        self.__results = dict()

    def __str__(self):
        """
        String representation of student
        """
        return f"Student {self.__first_name} {self.__last_name} is {self.__age} years old." \
               f"{self.__first_name} studies {self.__studies}."

    @property
    def student_id(self):
        """
        Getter method for the student ID
        """
        return self.__student_id

    @property
    def age(self):
        """
        Getter method for the student's age
        """
        return self.__age

    @property
    def study(self):
        """
        Getter method for the study the student follows
        """
        return self.__studies

    @property
    def results(self):
        """
        Getter method for the student's results
        """
        return self.__results

    @staticmethod
    def __generate_id() -> int:
        """
        Generate the student ID
        :return: Integer between 100000-999999
        """
        return randint(100000, 1000000)

    def add_study(self, study: str):
        """
        Add the name of the study for the student
        :param study: Name of the study
        """
        self.__studies.append(study)

    def get_age(self, situation="not_pub") -> int:
        """
        Get the age of the student
        If the student is in a pub and it's underage, return boozing age
        :param situation: not_pub by default
        """
        today = datetime.today()
        try:
            born = datetime.strptime(self.__birth, "%Y%m%d")
        except ValueError:
            raise InvalidDateFormat

        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        if situation == "not_pub":
            return age
        else:
            if age < 18:
                return 18
            else:
                return age

    def add_result(self, subject_id: int, result: float):
        """
        Add the result of the student to the results dictionary
        :param subject_id: ID of the subject/course
        :param result: End result
        """
        self.__results[subject_id] = result


class Result:
    """
    Results object of a test
    """
    def __init__(self, student_id: Student.student_id, result_id: int, name: str,
                 result: float, date: datetime):
        """
        Initializing Results
        :param student_id: ID of the student
        :param result_id: ID of the result
        :param name: Name of the subject
        :param result: Result of the exam
        :param date: Date of exam
        """
        self.__student_id = student_id
        self.__result_id = result_id
        self.__name = name
        self.__result = result
        self.__date = date

    def __str__(self):
        """
        String representation of the result
        """
        return f"Student {self.__student_id} took the exam of {self.__name} on {self.__date}" \
               f"and received a {self.__result} ({self.__result_id})."

    @property
    def id(self):
        """
        Getter method for student ID
        """
        return self.__result_id

    @property
    def name(self):
        """
        Getter method for the subject name
        """
        return self.__name

    @property
    def date(self):
        """
        Getter method for the date of exam
        """
        return self.__date

    @property
    def result(self):
        """
        Getter method for the grade
        """
        return self.__result

    @property
    def student(self):
        """
        Getter method for the student ID
        """
        return self.__student_id


class BinStudent(Student):
    """
    Extension of student class for creating and storing the student's password.
    """
    def __init__(self, first_name: str, family_name: str, birth_date: str):
        """
        Initializing BinStudent
        :param first_name: First name of the student
        :param family_name: Last name of the student
        :param birth_date: Date of birth of the student
        """
        super().__init__(first_name, family_name, birth_date)
        self.__bin_password = self.__generate_binpwd()

    @staticmethod
    def __generate_binpwd() -> str:
        """
        Generate a random password containing:
            6 uppercase letters;
            8 lowercase letters;
            4 digits;
            7 symbols;
          in random order.
        :return: Password string
        """
        password = []
        # Get the mandatory characters
        uppers = list(string.ascii_uppercase)
        lowers = list(string.ascii_lowercase)
        digits = list(string.digits)
        symbols = list(string.punctuation)

        # Randomly choose characters from each character-set (choices -> list), add to password
        password.append(choices(uppers, k=6))
        password.append(choices(lowers, k=8))
        password.append(choices(digits, k=4))
        password.append(choices(symbols, k=7))

        # Unpack the list in the list
        pwd = [char for chosen in password for char in chosen]
        # Shuffle the characters
        shuffle(pwd)
        # Make the password a string
        bin_pwd = "".join(pwd)

        return bin_pwd

    def get_binpwd(self, request: str):
        if request == self.__bin_password:
            return self.__bin_password
        else:
            raise ValidationError
