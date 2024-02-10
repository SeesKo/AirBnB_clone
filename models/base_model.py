#!/usr/bin/python3
"""
Provides foundation for creating other classes
with common attributes and methods.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class that defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """Initializes BaseModel instance."""
        if not kwargs:
            # New instance, assign attributes
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            # Instance from dictionary, convert attributes
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(
                            self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    )
                elif key != '__class__':
                    # Handling __class__ attribute
                    setattr(self, key, value)

    def __str__(self):
        """String representation of BaseModel."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
