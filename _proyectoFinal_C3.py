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

