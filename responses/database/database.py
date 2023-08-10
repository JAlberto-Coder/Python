from ecore.orm.dao import Dao
from ecore.system.models.log import Log
from ecore.system.models.error import Error
from ecore.system.models.response import Response

class Database:
    def __init__(self, data_source: str) -> None:
        self.data_source = data_source
    
    @staticmethod
    def new(data_source: str):
        return Database(data_source)
    
    def responses_select(self, code: str, language: str = "ES") -> any:
        try:
            filters = {
                "code": code,
                "language": language,
            }
            obj_dao = Dao("DS_ECORE")
            return obj_dao.read_all_with_filters(Response, filters)
        except Exception as e: 
            return False, str(e)
    
    def log_inserta(self, source: str, code: str, message: str, input: str, user_uuid: str = "") -> bool:
        try:
            if not isinstance(input, str):
                input = str(input)
            
            obj_log = Log()
            obj_log.source = source
            obj_log.code = code
            obj_log.message = message
            obj_log.input = input
            obj_log.ug = user_uuid

            obj_dao = Dao(self.data_source)
            resultado = obj_dao.create(obj_log)
            
            return True, ""
        except Exception as e:
            return False, str(e)
        
    def error_inserta(self, source: str, code: str, message: str, insumo: str, error: str, user_uuid: str = "") -> bool:
        try:
            if not isinstance(input, str):
                input = str(input)
            
            obj_error = Error()
            obj_error.source = source
            obj_error.code = code
            obj_error.message = message
            obj_error.input = input
            obj_error.error = error
            obj_error.ug = user_uuid
            
            obj_dao = Dao(self.data_source)
            resultado = obj_dao.create(obj_error)
            
            return True, ""
        except Exception as e:
            return False, str(e)
