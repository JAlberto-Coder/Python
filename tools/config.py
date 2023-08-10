import configparser
from typing import Type
from ecore.tools.extensions import is_empty

def get(section:str, param:str="", default_value:str="", file:str="config.ini", data_type:Type=str) -> any:
    """ Método que busca la sección o el valor del parámetro de un archivo .ini"""
    config = configparser.ConfigParser()
    config.read(file)
    if section not in config.sections() or (
        len(param) > 0 and param not in config[section]
    ):
        return default_value
    if len(param) > 0:
        if is_empty(config.get(section, param)):
            return default_value
        else:
            if data_type is bool:
                return config.getboolean(section, param)
            elif data_type is int:
                return config.getint(section, param)
            else:
                return config.get(section, param)
    else:
        obj_params = {
            option: config.get(section, option) for option in config.options(section)
        }

        return obj_params


def guardar(section:str, param:str="", value:str="", file:str="config.ini") -> bool:
    """ Método que guarda en el archivo de configuración el ``valor`` deseado, ordenandolo
        dependiendo de la ``sección`` y ``parámetro`` que se le indiquen.
    """
    config = configparser.ConfigParser()
    config.read(file)
    config.set(section, param, value)

    with open(file, "w", "utf-8") as archivo_config:
        config.write(archivo_config)

    return True
