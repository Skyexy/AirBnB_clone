#!/usr/bin/python3
""" file storage module for object class """
import json
import models
import os


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

    def sho(self, obj_name, obj_id):
        """find object with id `obj_id`"""
        if "{}.{}".format(obj_name, obj_id) not in self.__objects:
            raise Exception("** no instance found **")
        else:
            return self.__objects["{}.{}".format(obj_name, obj_id)]

    def delet(self, obj_name, obj_id):
        """ delete object with obj_name and obj_id """
        if "{}.{}".format(obj_name, obj_id) not in self.__objects:
            raise Exception("** no instance found **")
        else:
            return self.__objects.pop("{}.{}".format(obj_name, obj_id))

    def update(self, obj_name, obj_id, attr, value, **kwargs):
        """update object with ob_name ob_id att and value"""
        if "{}.{}".format(obj_name, obj_id) not in self.__objects:
            raise Exception("** no instance found **")
        else:
            model = self.__objects["{}.{}".format(obj_name, obj_id)]
            setattr(model, attr, value)

    def update_dict(self, obj_name, obj_id, dict={}):
        """update object with ob_name ob_id att and value"""
        if "{}.{}".format(obj_name, obj_id) not in self.__objects:
            raise Exception("** no instance found **")
        else:
            model = self.__objects["{}.{}".format(obj_name, obj_id)]
            res = ast.literal_eval(dict)
        if res == {}:
            raise Exception("**insert dictionary**")
        else:
            for key in res:
                setattr(model, key, res[key])
