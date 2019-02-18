import csv

class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
    def leer_Archivo(self): #Lee el archivo y devuelve una lista con las filas
        with open(str(self.nombre), newline='') as File:
            lineas = File.read().splitlines()
        return lineas
    def escribir_Archivo(self,lista):
            doc = open(str(self.nombre), "w")
            doc_csv = csv.writer(doc)
            doc_csv.writerows(lista)
class Trabajador(Archivo):
    def __init__(self,nombre):
        super().__init__(nombre)

    def masAntiguo(self):
         lineas=super().leer_Archivo()
         lineas.pop(0)
         antiguedad = []
         for l in lineas:
             linea = l.split(',')
             antiguedad.append([linea[1], int(linea[2])])
         antiguedad = sorted(antiguedad, key=lambda t: t[1], reverse=True)
         print("El trabajador mas antiguo es: ", antiguedad[0])


    def bonoAntiguedad(self):
        lineas = super().leer_Archivo()
        lineas.pop(0)
        listAntiguedad = []
        smn = 2060
        for l in lineas:
            linea = l.split(',')
            antiguedad=int(linea[2])
            if antiguedad < 2:
                bono = 0
            if antiguedad >= 2 and antiguedad <= 4:
                bono = 0.05 * 3 * smn
            if antiguedad >= 5 and antiguedad <= 7:
                bono = 0.11 * 3 * smn
            if antiguedad >= 8 and antiguedad <= 10:
                bono = 0.18 * 3 * smn
            if antiguedad >= 11 and antiguedad <= 14:
                bono = 0.26 * 3 * smn
            if antiguedad >= 15 and antiguedad <= 19:
                bono = 0.34 * 3 * smn
            if antiguedad >= 20 and antiguedad <= 24:
                bono = 0.42 * 3 * smn
            if antiguedad >= 25:
                bono = 0.50 * 3 * smn

            bono = float("{0:.3f}".format(bono))

            listAntiguedad.append([linea[1], int(linea[2]), linea[3],linea [4],str(bono)])
        print(listAntiguedad)
        return (listAntiguedad)


    def promedioDev(self):
        lineas = self.bonoAntiguedad() # devuelve una lista de listas [[,,],[,,],[,,]]
        suma = 0
        div = 0
        for l in lineas:
            linea = l
            if linea[3] == "DEV":
                suma = suma + float(linea[4]) + 5600
                div += 1
        promedio = suma / div
        print("El promedio de DEVs es: ", promedio)

    def totalPagado(self):
        lineas = self.bonoAntiguedad()  # devuelve una lista de listas [[,,],[,,],[,,]]
        total = 0
        for l in lineas:
            linea = l
            if linea[3] == "DEV":
                total = total + float(linea[4]) + 5600 # sueldo basico DEV=5600
            if linea[3] == "QA":
                total = total + float(linea[4]) + 3800
            if linea[3] == "DBA":
                total = total + float(linea[4]) + 6000
        print("El monto total que se paga a los trabajadores es:", total, "Bs")



t = Trabajador("bonos.csv")
t.masAntiguo()
t.bonoAntiguedad()
t.promedioDev()
t.totalPagado()

