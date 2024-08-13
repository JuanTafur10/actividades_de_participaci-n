class Estudiante:
    def __init__(self, id, nombre, nota):
        self.id = id
        self.nombre = nombre
        self.nota = nota

class Curso:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, id, nombre, nota):
        self.estudiantes.append(Estudiante(id, nombre, nota))
    
    def notas_a_cero(self):
        encontrado = False
        for estudiante in self.estudiantes:
            if encontrado:
                break
            if estudiante.nota > 3.0:
                encontrado = True
            else:
                estudiante.nota = 0

    def nota_mediana(self):
        notas = [estudiante.nota for estudiante in self.estudiantes]
        notas.sort()
        n = len(notas)
        if n % 2 == 0:
            return notas[n // 2 - 1]
        else:
            return notas[n // 2]

curso = Curso()
curso.agregar_estudiante(1, "Juan", 1.5)
curso.agregar_estudiante(2, "María", 4.0)
curso.agregar_estudiante(3, "Pedro", 3.4)
curso.agregar_estudiante(4, "Pedro", 4.0)
curso.agregar_estudiante(5, "Pedro", 2.5)
curso.agregar_estudiante(6, "Pedro", 3.5)

curso.notas_a_cero()

print("Nota mediana:", curso.nota_mediana())

for estudiante in curso.estudiantes:
    print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Nota: {estudiante.nota}")