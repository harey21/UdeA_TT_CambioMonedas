from tkinter import *
import Util

v = Tk()
v.title("Cambio de Monedas")
v.geometry("400x300")

iconos = ["./iconos/graficas.png", "./iconos/datos.png"]
textos=["Grafica Cambio vs Fecha", "Estadisticas"]

botones = Util.agregarBarra(v, iconos, textos)

#Agregar panel para seleccionar monedas y rango de fechas
panel = Frame(v)
panel.pack(side=TOP, fill=X)

Util.agregarEtiqueta(panel, "Moneda:", 0, 0)
cmbMoneda = Util.agregarLista(panel, [], 0, 1)
Util.agregarEtiqueta(panel, "Desde:", 0, 2)
cldDesde = Util.agregarCalendario(panel, 0, 3)
Util.agregarEtiqueta(panel, "Hasta:", 0, 4)
cldHasta = Util.agregarCalendario(panel, 0, 5)
