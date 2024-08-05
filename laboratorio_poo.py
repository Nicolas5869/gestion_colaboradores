import json

class Colaborador:

    def __init__(self, dni, nombre, apellido, edad, salario):
        self.__dni = self.validar_dni(dni)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__salario = self.validar_salario(salario)

    @property
    def dni(self):
        return self.__dni
    
    @property
    def nombre(self):
        return self.__nombre.capitalize()
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, nuevo_salario):
        self.__salario = self.validar_salario(nuevo_salario)

    @dni.setter
    def dni(self, nuevo_dni):
        self.__dni = self.validar_dni(nuevo_dni)

    def validar_salario(self, salario):
        try: 
            salario_num = float(salario)
            if salario_num <= 0:
                raise ValueError("El salario debe ser un numero positivo")
            return salario_num
        except ValueError:
            raise ValueError("El salario debe ser un numero valido")
        
    def validar_dni(self, dni):
        try:
            dni_num = int(dni)
            if len(str(dni)) not in [7, 8]:
                raise ValueError ("El dni debe tener entre 7 y 8 dígitos")
            if dni_num <= 0:
                raise ValueError("El dni debe ser un numero positivo")
            return dni_num
        except ValueError:
            raise ValueError("El dni debe ser numerico y estar compuesto por 7 u 8 dígitos")

    def to_dict(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "salario": self.salario
        }

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class ColaboradorTiempoCompleto(Colaborador):

    def __init__(self, dni, nombre, apellido, edad, salario, departamento):
        super().__init__(dni, nombre, apellido, edad, salario)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento
    
    def to_dict(self):
        data = super().to_dict()
        data['departamento'] = self.departamento
        return data
    
    def __str__(self):
        return f'{super().__str__()} - departamento: {self.departamento}'

class ColaboradorTiempoParcial(Colaborador):
    def __init__(self, dni, nombre, apellido, edad, salario, horas_semanales):
        super().__init__(dni, nombre, apellido, edad, salario)
        self.__horas_semanales = horas_semanales
    
    @property
    def horas_semanales(self):
        return self.__horas_semanales
    
    def to_dict(self):
        data = super().to_dict()
        data["horas_semanales"] = self.__horas_semanales
        return data
    
    def __str__(self):
        return f"{super().__str__()} - horas Semanales: {self.horas_semanales}"

class GestionColaboradores():
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
                return datos
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer el archivo: {error}')
    
    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)
        except IOError as error:
            print (f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')

    def crear_colaborador(self, colaborador):
        try:
            datos = self.leer_datos()
            dni = colaborador.dni
            if not str(dni) in datos.keys():
                datos[dni] = colaborador.to_dict()
                self.guardar_datos(datos)
                print(f'Guardado exitoso')
            else:
                print(f'El colaborador con el num de DNI: {dni} ya existe')
        except Exception as error:
            print (f'Error inesperado {error}')

    def leer_colaborador(self, dni):
        try:
            datos = self.leer_datos()
            if dni in datos:
                colaborador_data = datos[dni]
                if 'departamento' in colaborador_data:
                    colaborador = ColaboradorTiempoCompleto(**colaborador_data)
                else:
                    colaborador = ColaboradorTiempoParcial(**colaborador_data)
                print(f'Colaborador encontrado con DNI: {dni}')
                return colaborador
            else:
                return None
        except Exception as e:
            print(f'Error al leer el colaborador: {e}')
            return None
        
    def actualizar_colaborador(self, dni, nuevo_salario):
        try:
            datos = self.leer_datos()
            if str(dni) in datos.keys():
                datos[dni]['salario'] = nuevo_salario
                self.guardar_datos(datos)
                print(f'Salario actualizado correctamente para el colaborador DNI: {dni}')
            else:
                print(f"El DNI {dni} no existe")
        except Exception as e:
            print(f"Error al actualizar el colaborador: {e}")

    def eliminar_colaborador(self, dni):
        try:
            datos = self.leer_datos()
            if str(dni) in datos.keys():
                del datos[dni]
                self.guardar_datos(datos)
                print(f'El colaborador con DNI {dni} ha sido eliminado correctamente')
            else:
                print(f"El DNI {dni} no existe para eliminar")
        except Exception as e:
            print(f"Error al eliminar el colaborador: {e}")