#!/usr/bin/python3

"""
this is a module containg the BaseModel class
"""

import uuid
from datetime import datetime


class BaseModel():
    """
    BaseModel which will serve as the parent of all other model class
    """

    def __init__(self):
        """ Initialize instance attributes """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ returns an informal representation of the instance """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the updated_at attribute of the instance """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ converts the instance to a dictionary """

        instance_dict = self.__dict__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["__class__"] = self.__class__

        return (instance_dict)
