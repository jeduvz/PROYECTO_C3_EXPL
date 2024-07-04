## Proyecto Final - C3 - Nivel Explorador
class Empleado():
    def _init_(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario
        self.dni = dni
        self.fecha_vinculacion = fecha_vinculacion

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def _str_(self):
        return f"Empleado: {self.obtener_nombre_completo()}, Edad: {self.edad}, Salario: {self.salario}, DNI: {self.dni}, Fecha de Vinculación: {self.fecha_vinculacion}"

# Ejemplo de uso:
empleado1 = Empleado("Juan", "Perez", 30, 30000, "12345678", "01/01/2024")
print(empleado1)
empleado2 = Empleado("Juan", "Perez", 30, 30000, "12345678", "01/01/2024")
print(empleado1)
empleado2 = Empleado("Juan", "Perez", 30, 30000, "12345678", "01/01/2024")
print(empleado1)
empleado2 = Empleado("Juan", "Perez", 30, 30000, "12345678", "01/01/2024")
print(empleado1)

class Jefe(Empleado):
    def _init_(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        super()._init_(nombre, apellido, edad, salario, dni, fecha_vinculacion)
        self.empleados_a_cargo = []

    def agregar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def obtener_empleados_a_cargo(self):
        return self.empleados_a_cargo

    def _str_(self):
        return f"Jefe: {self.obtener_nombre_completo()}, Edad: {self.edad}, Salario: {self.salario}, DNI: {self.dni}, Fecha de Vinculación: {self.fecha_vinculacion}, Empleados a Cargo: {len(self.empleados_a_cargo)}"
# Ejemplo de uso:
jefe1 = Jefe("Pedro", "Gomez", 35, 40000, "87654321", "01/01/2018")

jefe1.agregar_empleado(empleado1)
print(jefe1)

class Area():
    def _init_(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def obtener_cantidad_empleados(self):
        return len(self.empleados)

    def obtener_empleados(self):
        return self.empleados

    def _str_(self):
        return f"Área: {self.nombre}, Descripción: {self.descripcion}, Cantidad de Empleados: {len(self.empleados)}"  
    # Ejemplo de uso:
area1 = Area("Ventas", "Encargada de las ventas de la empresa")

area1.agregar_empleado(empleado1)
print(area1)
