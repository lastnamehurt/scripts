from __future__ import absolute_import

# Put Third Party/Django Imports Here:
from faker import Faker

# Put Zenefits Imports Here:

fake = Faker('en_US')


def _random_company_name():
    return fake.company()


def random_fullName():
    return fake.name()


def random_email():
    return fake.email()


def random_company_name():
    return fake.company()


def random_zipCode():
    return '94118'  # fake generator causes validation error


def random_phone_number():
    return '757-640-5555'


def random_password():
    return fake.password()


def random_title():
    return fake.bs()


