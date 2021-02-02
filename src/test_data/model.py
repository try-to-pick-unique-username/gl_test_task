from dataclasses import dataclass

"""
This file contains the Data Classes related to User data model.
It's used to keep data logically structured, and maximally close to the data structures in the Application under test.
"""


@dataclass
class User:
    name: str
    email: str
    gender: str = 'Male'
    status: str = 'Active'
