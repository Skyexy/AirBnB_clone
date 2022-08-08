""" file storage module for object class """
import json
import models
import os
import ast


class Objects(dict):
    """class object"""

    def __getitem__(self, key):
        """get item"""
        try:
            return super(Objects, self).__getitem__(key)
        except Exception as e:
            raise Exception("** no instance found **")

    def pop(self, key):
        """pop item"""
        try:
            return super(Objects, self).pop(key)
        except Exception as e:
            raise Exception("** no instance found **")


class FileStorage:
    """ FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ init function """
        super().__init__()

    def all(self):
        """ all """
        return self.__objects

    def new(self, obj):
        """ new """
        if obj is not None:
            name = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[name] = obj

    def save(self):
        """ save objects into file """
        file = FileStorage.__file_path
        with open(file, mode="w", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    FileStorage.__objects,
                    cls=models.base_model.BaseModelEncoder
                )
            )

    def reload(self):
        """ get objects from file """
        file = FileStorage.__file_path
        if os.path.isfile(file):
            try:
                with open(file, 'r+', encoding="utf-8") as fp:
                    data = json.loads(fp.read())
                    for object_key, model_data in data.items():
                        model_name, model_id = object_key.split('.')
                        model = models.classes[model_name](**model_data)
                        self.new(model)
            except Exception as e:
                print(e)
