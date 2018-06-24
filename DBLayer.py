from Configurator import Configurator
from DBManager import DBManager
from InputValidators import InputValidators


class DBLayer:

    def __init__(self):
        self.configurator = Configurator()
        self.dbmanager = DBManager(self.configurator.config['DBPATH'])
        self.dbmanager.recreate_tables()

    @staticmethod
    def format_input_text(text: str):
        return text.strip().lower()

    def add_badman(self, lastname: str, firstname: str, dob: str):
        if not InputValidators.is_lastname_valid(lastname) \
                or not InputValidators.is_firstname_valid(firstname) \
                or not InputValidators.is_dob_valid(dob):
            return 'invalid input'

        lastname = DBLayer.format_input_text(lastname)
        firstname = DBLayer.format_input_text(firstname)
        dob = DBLayer.format_input_text(dob)

        badman_count = self.dbmanager.select_scalar(
            'SELECT COUNT(*) '
            'FROM badman '
            'WHERE lastname=' + lastname +
            ' AND firstname=' + firstname +
            ' AND dob=' + dob
        )
        if badman_count > 0:
            return 'already exist'
        else:
            self.dbmanager.execute('INSERT INTO badman values (' + lastname + ',' + firstname + ',' + dob + ')')
            return 'added'

    def add_goodman(self, email: str, login: str):
        if not InputValidators.is_email_valid(email) \
                or not InputValidators.is_login_valid(login):
            return 'invalid input'

        email = DBLayer.format_input_text(email)
        login = DBLayer.format_input_text(login)

        email_count = self.dbmanager.select_scalar(
            'SELECT COUNT(*) '
            'FROM goodman '
            'WHERE email=' + email
        )

        login_count = self.dbmanager.select_scalar(
            'SELECT COUNT(*) '
            'FROM goodman '
            'WHERE login=' + login
        )

        if email_count > 0:
            return 'email already exist'
        elif login_count > 0:
            return ' login already exist'
        else:
            self.dbmanager.execute('INSERT INTO goodman values (' + email + ',' + login + ')')
            return 'added'
