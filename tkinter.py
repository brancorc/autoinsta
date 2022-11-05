from tkinter import *

root = Tk()

descripciones=[]

def pasar_archivo(texto):

    global descripciones

    texto=entrada.get()

    texto = [texto]

    descripciones += texto

    entrada.delete(first=0, last=999999)

    print(descripciones)

    #hacer que aca llame a una funcion que pase al siguiente archivo en google photos mediante selenium

entrada =Entry(root)

entrada.place(
        width=300,
        height=100)

entrada.bind('<Return>', pasar_archivo)

root.mainloop()
