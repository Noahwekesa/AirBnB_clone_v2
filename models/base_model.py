#!/usr/bin/python3
"""
Base_model module - defines all common attributes/methods for other classes
"""
import uuid
import datetime
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """initialize variables & methods"""
        if kwargs is not None and len(kwargs) > 0:
            # if kwargs: # cmd line equivalent to the one above
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                try:
                    if value.isdigit():
                        value = int(value)
                    elif value.replace('.', '', 1).isdigit():
                        value = float(value)
                except AttributeError:
                    pass
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """
     updates the public instance attribute 'updated_at' with the current time
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        method that returns a dictionary containing all keys or values of
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        """
        string representation of an object/instance in this format:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)
