# Definición básica de una clase
class Persona:
    """
    Clase que representa a una persona.
    """
    # Atributo de clase
    especie = "Humano"
    
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.
        :param nombre: Nombre de la persona.
        :param edad: Edad de la persona.
        """
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        """
        Método que imprime un saludo.
        """
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona("Alice", 30)
persona1.saludar()  # Llamada al método saludar

print("---")

# Acceder al atributo de clase
print(f"Especie: {Persona.especie}")

print("---")

# Clase con herencia
class Empleado(Persona):
    """
    Clase que representa a un empleado, heredando de Persona.
    """
    def __init__(self, nombre, edad, salario):
        """
        Constructor de la clase Empleado.
        :param nombre: Nombre del empleado.
        :param edad: Edad del empleado.
        :param salario: Salario del empleado.
        """
        # Llamar al constructor de la clase base
        super().__init__(nombre, edad)
        self.salario = salario

    def mostrar_salario(self):
        """
        Método que muestra el salario del empleado.
        """
        print(f"{self.nombre} tiene un salario de {self.salario}.")

# Crear una instancia de la clase Empleado
empleado1 = Empleado("Bob", 25, 50000)
empleado1.saludar()  # Método heredado de Persona
empleado1.mostrar_salario()  # Método de Empleado

print("---")

# Encapsulamiento
class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria.
    """
    def __init__(self, titular, saldo):
        """
        Constructor de la clase CuentaBancaria.
        :param titular: Titular de la cuenta (instancia de Persona).
        :param saldo: Saldo inicial de la cuenta.
        """
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        """
        Método para depositar dinero en la cuenta.
        :param cantidad: Cantidad a depositar.
        """
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se han depositado {cantidad}. Saldo actual: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        """
        Método para retirar dinero de la cuenta.
        :param cantidad: Cantidad a retirar.
        """
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se han retirado {cantidad}. Saldo actual: {self.__saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def mostrar_saldo(self):
        """
        Método para mostrar el saldo de la cuenta.
        """
        print(f"Saldo actual: {self.__saldo}")

# Crear una instancia de la clase Persona
titular = Persona("Charlie", 40)

# Crear una instancia de la clase CuentaBancaria
cuenta1 = CuentaBancaria(titular, 1000)
print(f"Titular de la cuenta: {cuenta1.titular}")
cuenta1.mostrar_saldo()
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.retirar(1500)  # Fondos insuficientes

print("---")

# Métodos estáticos y de clase
class Utilidades:
    """
    Clase con métodos estáticos y de clase.
    """
    @staticmethod
    def sumar(a, b):
        """
        Método estático para sumar dos números.
        :param a: Primer número.
        :param b: Segundo número.
        :return: Suma de a y b.
        """
        return a + b

    @classmethod
    def mostrar_especie(cls):
        """
        Método de clase que muestra la especie.
        Esta asociado a la clase en si misma, y no a la instancia
        """
        print(f"Especie: {cls.especie}")

# Llamada a un método estático
resultado = Utilidades.sumar(3, 4)
print(f"La suma de 3 y 4 es {resultado}")

# Añadir atributo de clase especie para el método de clase
Utilidades.especie = "Humano"
# Llamada a un método de clase
Utilidades.mostrar_especie()

print("---")

# Propiedades
class Producto:
    """
    Clase que representa un producto.
    """
    def __init__(self, nombre, precio):
        """
        Constructor de la clase Producto.
        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        """
        self.nombre = nombre
        self.__precio = precio  # Atributo privado

    @property
    def precio(self):
        """
        Propiedad para obtener el precio del producto.
        """
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        """
        Propiedad para establecer el precio del producto.
        :param nuevo_precio: Nuevo precio del producto.
        """
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser positivo.")

# Crear una instancia de la clase Producto
producto1 = Producto("Laptop", 1000)
print(f"El precio de {producto1.nombre} es {producto1.precio}")

# Modificar el precio utilizando el setter
producto1.precio = 1200
print(f"El nuevo precio de {producto1.nombre} es {producto1.precio}")

# Intentar establecer un precio negativo
producto1.precio = -500  # No se permite

