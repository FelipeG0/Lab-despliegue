from pydantic import BaseModel

class DataModel(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    u: float
    g: float
    r: float
    i: float
    z: float
    redshift: float
    class_QSO: bool
    class_STAR: bool

#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ["u","g","r","i","z","redshift","class_QSO","class_STAR"]
