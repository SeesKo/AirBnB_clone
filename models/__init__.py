#!/usr/bin/python3
"""
This module initializes the FileStorage instance for the application.
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()
