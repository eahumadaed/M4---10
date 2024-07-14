from campaña import Campaña
from anuncio import Video
from error import SubTipoInvalidoException, LargoExcedidoException

def main():
    campaña = Campaña("Campaña 1", [Video(10)])
    try:
        nuevo_nombre = input("Ingrese un nuevo nombre para la campaña: ")
        if len(nuevo_nombre) > 250:
            raise LargoExcedidoException("El nombre excede los 250 caracteres.")
        campaña.nombre = nuevo_nombre
    except LargoExcedidoException as e:
        with open("error.log", "a") as file:
            file.write(str(e) + "\n")

    try:
        nuevo_subtipo = input("Ingrese un nuevo subtipo para el anuncio: ")
        campaña.anuncios[0].sub_tipo = nuevo_subtipo
    except SubTipoInvalidoException as e:
        with open("error.log", "a") as file:
            file.write(str(e) + "\n")

if __name__ == "__main__":
    main()
