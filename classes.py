class Articulo:
    articulos = []

    def __init__(self, titulo: str, autores: list, palabras_claves: list, resumen: str,
                 tamanno_archivo: int, estado='Pendiente de evaluación', portada='') -> None:
        self.__titulo = titulo
        self.__autores = autores
        self.__palabras_claves = palabras_claves
        self.__resumen = resumen
        self.__tamanno_archivo = tamanno_archivo
        self.__revisores = []
        self.__estado = estado
        self.__sennalamientos = []
        self.__portada = portada

        Articulo.articulos.append(self)

    # Decoradores
    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self.__titulo = titulo

    @property
    def autores(self) -> list:
        return self.__autores

    @autores.setter
    def autores(self, autores: list) -> None:
        self.__autores = autores

    @property
    def palabras_claves(self) -> str:
        return self.__palabras_claves

    @palabras_claves.setter
    def palabras_claves(self, palabras_claves: str) -> None:
        self.__palabras_claves = palabras_claves

    @property
    def resumen(self) -> str:
        return self.__resumen

    @resumen.setter
    def resumen(self, resumen: str) -> None:
        self.__resumen = resumen

    @property
    def tamanno_archivo(self) -> int:
        return self.__tamanno_archivo

    @tamanno_archivo.setter
    def tamanno_archivo(self, tamanno_archivo: int) -> None:
        self.__tamanno_archivo = tamanno_archivo

    @property
    def revisores(self) -> list:
        return self.__revisores

    @revisores.setter
    def revisores(self, revisores: list) -> None:
        self.__revisores = revisores

    @property
    def estado(self) -> str:
        return self.__estado

    @estado.setter
    def estado(self, estado: str) -> None:
        self.__estado = estado

    @property
    def sennalamientos(self) -> list:
        return self.__sennalamientos

    @sennalamientos.setter
    def sennalamientos(self, sennalamientos: list) -> None:
        self.__sennalamientos = sennalamientos

    @property
    def portada(self) -> str:
        return self.__portada

    @portada.setter
    def portada(self, portada: str) -> None:
        self.__portada = portada

    # Methods
    def agregar_senalamiento(self, senalamiento):
        self.__sennalamientos.append(senalamiento)

    def actualizar_estado_revision(self, nuevo_estado):
        self.estado = nuevo_estado

    @classmethod
    def get_all_articles(cls):
        return cls.articulos


class Autor:
    autores = []

    def __init__(self, nombre: str, apellidos: str, correo: str, orcid):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__correo = correo
        self.__orcid = orcid
        Autor.autores.append(self)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    @property
    def apellidos(self) -> str:
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos: str) -> None:
        self.__apellidos = apellidos

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, correo: str) -> None:
        self.__correo = correo

    @property
    def orcid(self) -> int:
        return self.__orcid

    @classmethod
    def get_all_authors(cls):
        return cls.autores


class Volumen:
    volumenes = []

    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.articulos = []
        Volumen.volumenes.append(self)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def agregar_articulo(self, articulo: Articulo):
        self.articulos.append(articulo)

    def cantidad_articulos(self):
        return len(self.articulos)

    @classmethod
    def get_all_volumes(cls):
        return cls.volumenes


class RevistaCientifica:
    def __init__(self):
        self.volumenes = []

    def agregar_volumen(self, volumen: Volumen) -> None:
        self.volumenes.append(volumen)

    def obtener_articulos_por_volumen(self, volumen: Volumen) -> list:
        return [articulo for articulo in volumen.articulos if articulo.estado == "Aceptado para publicación"]

    def obtener_articulos_por_autor(self, autor: Autor):
        for volumen in self.volumenes:
            return [articulo for articulo in volumen.articulos if autor in articulo.autores]

    def cantidad_articulos_por_volumen(self, volumen: Volumen) -> int:
        return volumen.cantidad_articulos()

    def cantidad_volumenes_sin_repeticion(self) -> int:
        vol_no_repetidos = 0
        autores = {}
        for volumen in self.volumenes:
            for articulo in volumen.articulos:
                for autor in articulo.autores:
                    if autor not in autores:
                        autores[autor] = 1
                    else:
                        autores[autor] += 1
            if len(autores.values()) == len(set(autores.values())):
                vol_no_repetidos += 1
        return vol_no_repetidos

