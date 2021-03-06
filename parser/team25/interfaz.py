from tkinter import * 
from tkinter import ttk
from tkinter import messagebox as msg , scrolledtext
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from gramaticasql import analizarEntrada # metodo para ejecutar el parser
import tkinter.font as tkFont
import os 

class InterfazCompi:
    def __init__(self, window):
        self.ventana = window
        self.ventana.title("COMPILADORES 2")
        self.ventana.geometry('1500x1800') # ancho * altura
        self.ventana.config(background='black')
        
        myfont = tkFont.Font(family="Arial" , size = 14 , slant = "italic")
        
        frame = LabelFrame(self.ventana, text = '')
        frame.grid(row=0,column=0,columnspan=100,pady=15 , padx = 15) # MARGEN superior
        frame.config(background='black')
        
        #___________________________________________ SECCION DE BOTONES
        menuPrincipal = Menu(self.ventana)
        self.ventana.config(menu = menuPrincipal )
        
        # creacion previa de los subMenus
        filemenu = Menu(menuPrincipal)
        reporteMenu = Menu(menuPrincipal)
        filemenu.add_command(label="Abrir" , command = self.openFIILE)
        reporteMenu.add_command(label="View" , command = self.viewImage)
        
        # los agrega a la pantalla principal
        menuPrincipal.add_cascade(label="Archivos", menu=filemenu)
        menuPrincipal.add_cascade(label="Reportes", menu=reporteMenu)
        

        
        self.ejecutar = Button(frame,justify = 'center', width= 45,bd = 8, fg='black', bg= 'OliveDrab1', text ="EJECUTAR", command = self.analizar , relief = 'ridge' ,  pady = 10 , padx = 0 , activeforeground  = 'black' , activebackground  ='orange')
        self.ejecutar.grid(row=0,column=0)
        


        
         

    
        #_____________________________________________ TEXT AREA
        Label(frame , text ='ENTRADA:' , font = myfont ,  background='black' ,fg = 'white').grid(row=60,column=0 , pady = 20 )
        self.entradaTextArea = Text(frame, height=25, width=180 )
        self.entradaTextArea = scrolledtext.ScrolledText(frame ,height=25 ,width=180 , bg='linen' )
        self.entradaTextArea.grid(row=80,column=0)
        self.entradaTextArea.focus()
        
        
        Label(frame,text='CONSOLA: ' ,  font = myfont , background='black' ,fg = 'white').grid(row=100,column=0 , pady = 20)
        self.salidaTextArea = Text(frame, height=20, width=180 )
        self.salidaTextArea = scrolledtext.ScrolledText(frame ,height=20 ,width=180 , background='black' , fg = 'SpringGreen' )
        self.salidaTextArea.grid(row=120,column=0)


    def openFIILE(self):
        direccionArchivo = askopenfilename()
        file = open(direccionArchivo,"r")
        cadena_del_archivo = file.read()
        file.close()
        self.entradaTextArea.insert(INSERT,cadena_del_archivo)

         
        
    def analizar(self):
        print('analizando una entrada')
        result = msg.askyesno("EJECUTANDO", "¿Quiere ejecutar esta entrada?")
        if result==True:
            try:
                index = "0.0"
                print('ENTRADA:', self.entradaTextArea.get(index,END))
                analizarEntrada(self.entradaTextArea.get(index,END))
            except:
                print("NO SE PUDO EJECUTAR :v")

   
            
    
    def viewImage(self):
        ventana = Tk()
        try:
            ventana.title("imagenes")
            ventana.geometry("700x700")
            imagen = PhotoImage(file="graphviz.png")
            fondo = Label(ventana , image = imagen ).place(x = 0 , y = 0)
            ventana.mainloop() 
        except:
            print('NO SE ENCONTRO LA IMAGEN')            

if __name__ == '__main__':
    window = Tk()
    app = InterfazCompi(window)
    window.mainloop()