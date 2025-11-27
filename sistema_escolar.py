class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_info(self):
        return f"""
            ¡INFORMACION! 
            Nombre: {self.nombre}
            Edad: {self.edad}
            """
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def grado_est(self):
        print(f"{self.nombre} esta cursando el grado: {self.grado}")
    
    def mostrar_info(self):
        return f"""
            ¡INFORMACION! 
            Nombre: {self.nombre}
            Edad: {self.edad}
            Grado: {self.grado}     
            """

    
if __name__ == "__main__":
    persona = Persona("Daniel", 19)
    persona.mostrar_info()
    estudiante = Estudiante("Daniel", 19, 11)
    print(estudiante.mostrar_info())
