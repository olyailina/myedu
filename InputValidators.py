import re
from datetime import datetime


class InputValidators:
    @staticmethod
    def is_lastname_valid(lastname: str):
        return True if re.compile('^[a-z\-]{2,50}$').match(lastname) else False

    @staticmethod
    def is_firstname_valid(firstname: str):
        return True if re.compile('^[a-z\-]{2,50}$').match(firstname) else False

    @staticmethod
    def is_dob_valid(dob: str):
        try:
            datetime.strptime(dob, '%Y-%m-%d')
        except ValueError:
            return False
        return True

    @staticmethod
    def is_email_valid(email: str):
        return True if re.compile('[^@]+@[^@]+\.[^@]+').match(email) else False

    @staticmethod
    def is_login_valid(login: str):
        return True if re.compile('^[a-z0-9]{2,50}$').match(login) else False

    @staticmethod
    def is_city_valid(city: str):
        return True if re.compile('^[a-z\-]{2,50}$').match(city) else False

    @staticmethod
    def is_street_valid(street: str):
        return True if re.compile('^[a-z0-9]{2,50}$').match(street) else False

    @staticmethod
    def is_building_valid(building: int):
        return True if re.compile('^[0-9]{1,3}$').match(str(building)) else False

    @staticmethod
    def is_block_valid(block: int):
        return True if re.compile('^[0-9]$').match(str(block)) else False

    @staticmethod
    def is_entrance_valid(entrance: int):
        return True if re.compile('^[0-9]{1,2}$').match(str(entrance)) else False

    @staticmethod
    def is_floor_valid(floor: int):
        return True if re.compile('^[0-9]{1,2}$').match(str(floor)) else False

    @staticmethod
    def is_apptnumber_valid(apptnumber: int):
        return True if re.compile('^[0-9]{1,2}$').match(str(apptnumber)) else False
