#clase >es> un molde para crear objetos >tiene> variables y funcion(parametros)/metodo(parametros)
#metodo >es> una funcion que pertenece a una clase
#objeto >es> una instancia de una clase
#constructor >es> una funcion que se ejecuta cuando se crea un objeto

#variables >es> un espacio en memoria que guarda un valor

#dicc = {}
#dicc["clave"] = "valor"
#dicc["clave"] = "valor2"

#ista = []
#lista.append("hola")
#lista.append("chau")


import unittest

from dispositivo import Dispositivo
from database import Database

class MyTest(unittest.TestCase):

    def setUp(self):             #se agrega a cada metodo
        dispositivo_1 = {        #diccionario dispositivo_1
            "id": 1,             #clave:valor
            "nombre": "teclado", #clave:valor
            "marca": "genius",   #clave:valor
        }                        #diccionario dispositivo_1
        dispositivo_2 = {
            "id": 2,
            "nombre": "mouse",
            "marca": "logitech",
        }
        dispositivo_3 = {
            "id": 3,
            "nombre": "memoria",
            "tipo": "ram",
        }

        self.database_template = {"dispositivos": [
            dispositivo_1,
            dispositivo_2,
            dispositivo_3,
        ]}

        self.dispositivo_1 = Dispositivo(1, "teclado", "genius")
        self.dispositivo_2 = Dispositivo(2, "mouse", "logitech")
        self.dispositivo_3 = Dispositivo(diccionario=dispositivo_3)
        self.dispositivo_4 = Dispositivo(4, "placa de red", tipo="wireless", marca="tp-link")

    def compare_dispositivos(self, dispositivo_1: Dispositivo, dispositivo_2: Dispositivo):
        if dispositivo_1.id != dispositivo_2.id:
            return False
        if dispositivo_1.nombre != dispositivo_2.nombre:
            return False
        if dispositivo_1.marca != dispositivo_2.marca:
            return False
        if dispositivo_1.tipo != dispositivo_2.tipo:
            return False
        return True

    def test_create_database(self):
        database = Database(self.database_template)
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_1, database.database[0]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_2, database.database[1]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_3, database.database[2]))

    def test_delete_by_id(self):
        database = Database(self.database_template)
        database.delete_by_id(id=2)
        self.assertEqual(len(database.database), 2)
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_1, database.database[0]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_3, database.database[1]))

    def test_add_dispositivo(self):
        database = Database(self.database_template)
        database.add_dispositivo(self.dispositivo_4)
        self.assertEqual(len(database.database), 4)
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_1, database.database[0]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_2, database.database[1]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_3, database.database[2]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_4, database.database[3]))

    def test_add_diccionario(self):
        diccionario = {
            "id": 5,
            "nombre": "placa de video",
            "tipo": "pci-e",
            "marca": "ati",
        }
        database = Database(self.database_template)
        database.add_dispositivo(diccionario=diccionario)
        self.assertEqual(len(database.database), 4)
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_1, database.database[0]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_2, database.database[1]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_3, database.database[2]))
        self.assertTrue(self.compare_dispositivos(
            Dispositivo(diccionario=diccionario), database.database[3]))

if __name__ == '__main__':
    unittest.main()
