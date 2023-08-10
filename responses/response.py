from typing import TypeVar, Any
from ecore.tools.pydantic.base_model import BaseModel
from ecore.responses._response import get, save

class Response(BaseModel):
    status: bool=False
    code: str=""
    message: str=""
    language: str="ES"
    content: TypeVar("content")=None
    another_message: str=""
    error: Any=""

    class Config:
        fields = {
            "another_message": {"exclude": True},
            "error": {"exclude": True},
        }
    
    def message_get(self, another_message:str="", key:str="DS_ECORE") -> str:
        """ Método que busca el código en base de datos o memoria caché, y devuelve el mensaje
        """
        return get(self.code, another_message, key, self.language)
    
    def response_save(self, source:str, input:str, error:str="", uuid_usuario:str="dd90aafc-1f2e-49c5-990e-ead60d56bd07", key:str="DS_ECORE", gateway:str=None) -> bool:
        """ Método que almacena una validación o error en base de datos
        """
        return save(self.code, self.message, source, input, error, uuid_usuario, key, gateway)
