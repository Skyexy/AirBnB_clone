import json
import models
import os


class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj is not None:
            name = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[name] = obj.__dict__

    def save(self):
        print(self.__objects)
        with open(self.__file_path, "w", encoding="utf-8") as fp:
            json.dumps(
                self.__dict__,
            )

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r+') as fp:
                self.__objects = json.loads(fp.read())
