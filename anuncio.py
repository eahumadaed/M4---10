class Anuncio:
    def __init__(self, alto, ancho):
        self.alto = self._validar_dimension(alto)
        self.ancho = self._validar_dimension(ancho)

    @staticmethod
    def _validar_dimension(valor):
        return valor if valor > 0 else 1

    @property
    def url_archivo(self):
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, valor):
        self._url_archivo = valor

    @property
    def url_clic(self):
        return self._url_clic

    @url_clic.setter
    def url_clic(self, valor):
        self._url_clic = valor

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor):
        if valor in self.SUB_TIPOS:
            self._sub_tipo = valor
        else:
            raise SubTipoInvalidoException("Subtipo no válido")

    @staticmethod
    def mostrar_formatos():
        pass

class Video(Anuncio):
    SUB_TIPOS = ("Corto", "Mediano", "Largo")

    def __init__(self, duracion):
        super().__init__(1, 1)
        self.duracion = self._validar_duracion(duracion)

    @staticmethod
    def _validar_duracion(valor):
        return valor if valor > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    SUB_TIPOS = ("Banner", "Skyscraper", "Square")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

class Social(Anuncio):
    SUB_TIPOS = ("Post", "Story", "Ad")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
