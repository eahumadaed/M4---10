class Campaña:
    def __init__(self, nombre, anuncios=[]):
        self.nombre = nombre
        self.anuncios = anuncios

    @property
    def anuncios(self):
        return self._anuncios

    @anuncios.setter
    def anuncios(self, valor):
        self._anuncios = valor

    def __str__(self):
        tipo_anuncios = {
            "Video": 0,
            "Display": 0,
            "Social": 0
        }
        for anuncio in self.anuncios:
            tipo_anuncios[anuncio.__class__.__name__] += 1
        return f"Nombre de la campaña: {self.nombre}\n" \
               f"Anuncios: {tipo_anuncios['Video']} Video, " \
               f"{tipo_anuncios['Display']} Display, " \
               f"{tipo_anuncios['Social']} Social"
