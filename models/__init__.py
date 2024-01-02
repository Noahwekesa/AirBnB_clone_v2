#!/usr/bin/python3
"""
__Init__ module of all the models package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
