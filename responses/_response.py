from ecore.tools.cache import Cache
from ecore.responses.database.database import Database
from ecore.tools.extensions import is_empty
# from ecore.tools.custom_logger import exception

# @exception
def get(code:str, another_message:str="", key:str="", language:str="ES"):
    message = ""
    obj_cache = Cache.new()
    valor = obj_cache.get(f"{code}{language}")
    if valor is None:
        obj_bd = Database.new(key)
        resultado = obj_bd.responses_select(code)
        
        if not(resultado[0]):
            data = [dict({"message": "Ocurrió un error al conectarse a la base de datos. {0}"})]
            # raise Exception(data[0]["message"].format(resultado[1]))
        elif len(resultado[1]) == 0:
            data = [dict({"message": "Respuesta no contemplada."})]
            # raise Exception(data[0]["message"].format(resultado[1]))
        else:
            data = resultado[1]
        
        if isinstance(data, dict):
            message = data[0].get("message")
        else:
            message = data[0]["message"]
        
        obj_cache.add(f"{code}{language}", message)
    else:
        message = valor
    
    return message.format(another_message)

def save(code: str, message: str, fuente: str, insumo: str, error: str = "",
    uuid_usuario: str = "dd90aafc-1f2e-49c5-990e-ead60d56bd07",
    key: str = "DS_ECORE", gateway: str = None) -> bool:
    """ Método que almacena una validación o error en base de datos
    """
    obj_bd = Database.new(key)
    code_temp = 5 if is_empty(code) or "-" not in code else int(code.split("-")[1][0])
    code = "-500" if is_empty(code) else code
    if code_temp == 5:
        obj_bd.error_inserta(source=fuente, code=code, message=message, input=insumo, error=error, user_uuid=uuid_usuario)
    elif code_temp != 2:
        obj_bd.log_inserta(source=fuente,code=code, message=message, input=insumo, user_uuid=uuid_usuario)
