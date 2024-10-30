from validadorclave.modelo.validador import ReglaValidacionGanimedes, ReglaValidacionCalisto, Validador
from validadorclave.modelo.errores import (
    NoCumpleLongitudMinimaError,
    NoTieneLetraMayusculaError,
    NoTieneLetraMinusculaError,
    NoTieneNumeroError,
    NoTieneCaracterEspecialError,
    NoTienePalabraSecretaError
)

def validar_clave(clave, reglas):
    for regla in reglas:
        validador = Validador(regla)
        try:
            if validador.es_valida(clave):
                print(f"La clave es válida para la regla {regla.__class__.__name__}")
        except NoCumpleLongitudMinimaError as e:
            print(f"Error: {regla.__class__.__name__}: {e}")
        except NoTieneLetraMayusculaError as e:
            print(f"Error: {regla.__class__.__name__}: {e}")
        except NoTieneLetraMinusculaError as e:
            print(f"Error: {regla.__class__.__name__}: {e}")
        except NoTieneNumeroError as e:
            print(f"Error: {regla.__class__.__name__}: {e}")
        except NoTieneCaracterEspecialError as e:
            print(f"Error: {regla.__class__.__name__}: {e}")
        except NoTienePalabraSecretaError as e:
            print(f"Error: {regla.__class__.__name__}: {e}")

if __name__ == "__main__":
    clave = "Hola1234@"
    reglas = [ReglaValidacionGanimedes(8), ReglaValidacionCalisto(8)]
    validar_clave(clave, reglas)