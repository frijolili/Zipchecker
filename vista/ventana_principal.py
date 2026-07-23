import customtkinter as ctk
from logica.gestor_excel import GestorExcel
from logica.comprobador import Comprobador
from logica.exportador import Exportador
from tkinter import filedialog
from pathlib import Path



# APARIENCIA PRINCIPAL 

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class VentanaPrincipal(ctk.CTk):

    def __init__(self):
        super().__init__()


        self.gestor_excel = GestorExcel()
        self.comprobador = None

        self.configurar_ventana()
        self.crear_widgets()

        self.gestor_excel = GestorExcel()
        self.comprobador = None
        self.exportador = Exportador()

    def configurar_ventana(self):
        self.title("Comprobador de Trazabilidad")

        self.geometry("900x600")

        self.minsize(900, 600)

        self.grid_columnconfigure(0, weight=1)

        for fila in range(4):
            self.grid_rowconfigure(fila, weight=1)


    def crear_widgets(self):

        self.crear_frame_superior()
        self.crear_frame_archivos()
        self.crear_frame_lector()
        self.crear_frame_estadisticas()
        
    #--------------------ESPACIO PARA TÍTULO-------------------

    def crear_frame_superior(self):
        self.frame_superior = ctk.CTkFrame(self)

        self.frame_superior.grid(
        row=0,
        column=0,
        padx=20,
        pady=(20,10),
        sticky="nsew"
        )
        titulo = ctk.CTkLabel(
            self.frame_superior,
            text="COMPROBADOR DE TRAZABILIDAD",
            font=("Arial",28,"bold")
        )

        titulo.pack(pady=20)

        
    #------AQUÍ PONGO EL EXCEL DE LA BASE Y EL DE ESCRIBIR------------------

    def crear_frame_archivos(self):

    # Frame principal
        self.frame_archivos = ctk.CTkFrame(self)

        self.frame_archivos.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )

        self.frame_archivos.grid_columnconfigure(0, weight=1)
        self.frame_archivos.grid_columnconfigure(1, weight=1)

        # Título
        titulo = ctk.CTkLabel(
            self.frame_archivos,
            text="Archivos",
            font=("Arial", 20, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(15, 10)
        )

    
    
    # ------------ FRAME BASE ESCOGIDA-------------

        self.frame_base = ctk.CTkFrame(self.frame_archivos)

        self.frame_base.grid(
             row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.frame_base.grid_columnconfigure(0, weight=1)

        titulo_base = ctk.CTkLabel(
            self.frame_base,
            text="Base de datos",
            font=("Arial", 16, "bold")
        )

        titulo_base.grid(row=0, column=0, pady=(10,5))

        self.label_base = ctk.CTkLabel(
            self.frame_base,
            text="Base cargada: Ninguna"
        )

        self.label_base.grid(row=1, column=0, pady=5)

        self.boton_cargar = ctk.CTkButton(
            self.frame_base,
            text="Seleccionar Excel",
            command=self.seleccionar_excel
        )

        self.boton_cargar.grid(
            row=2,
            column=0,
            pady=(10,15)
        )

    

    # ----------FRAME EXCEL RESULTADOS------------

        self.frame_resultados = ctk.CTkFrame(self.frame_archivos)

        self.frame_resultados.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.frame_resultados.grid_columnconfigure(0, weight=1)

        titulo_resultados = ctk.CTkLabel(
            self.frame_resultados,
            text="Resultados",
            font=("Arial",16,"bold")
        )

        titulo_resultados.grid(row=0, column=0, pady=(10,5))

        self.label_resultados = ctk.CTkLabel(
            self.frame_resultados,
            text="Ningún archivo seleccionado"
        )

        self.label_resultados.grid(row=1, column=0, pady=5)

        self.boton_resultados = ctk.CTkButton(
            self.frame_resultados,
            text="Abrir resultados",
            command=self.seleccionar_resultados
        )

        self.boton_resultados.grid(
            row=2,
            column=0,
            pady=(10, 15)
        )


    def seleccionar_resultados(self):

        ruta = filedialog.askopenfilename(
            title="Selecciona el Excel de resultados",   
            filetypes=[("Archivos Excel", "*.xlsx")]
        )   

        if not ruta:
            return

        self.exportador.abrir_excel(ruta)

        nombre = Path(ruta).name

        self.label_resultados.configure(
            text=f"{nombre}\n🟢 Conectado"
        )
    
        
    #-------------FRAME LECTOR----------------


    def crear_frame_lector(self):

        self.frame_lector = ctk.CTkFrame(self)

        self.frame_lector.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )

        self.frame_lector.grid_columnconfigure(0, weight=1)

        titulo = ctk.CTkLabel(
            self.frame_lector,
            text="Lector QR",
            font=("Arial", 20, "bold")
        )

        titulo.grid(row=0, column=0, pady=(15, 5))

        self.entry_codigo = ctk.CTkEntry(
            self.frame_lector,
            placeholder_text="Escanea una pieza..."
        )
       
        self.entry_codigo.bind("<Return>", self.comprobar_codigo)

        self.label_resultado = ctk.CTkLabel(
            self.frame_lector,
            text="Esperando lectura...",
            font=("Arial", 24, "bold")
        )

        self.entry_codigo.grid(
            row=1,
            column=0,
            padx=20,
            pady=(5, 20),
            sticky="ew"
        )


        self.label_resultado.grid(
            row=2,
            column=0,
            pady=(0, 20)
        )
    #-------------------------------------------


    def seleccionar_excel(self):

        ruta = filedialog.askopenfilename(
            title="Selecciona la base de datos",
            filetypes=[("Archivos Excel", "*.xlsx")]
        )

        if not ruta:
            return

        total = self.gestor_excel.cargar_excel(ruta)

        self.comprobador = Comprobador(
            self.gestor_excel.trazabilidades
        )

        self.label_base.configure(
            text=f"Base cargada: {total} registros"
        )

    #-----------------------------------------

    def comprobar_codigo(self, event):

        codigo = self.entry_codigo.get()

        resultado = self.comprobador.comprobar(codigo)

        self.label_resultado.configure(
            text=resultado
        )

        self.entry_codigo.delete(0, "end")
        self.entry_codigo.focus()
  

    #------------------ESPACIO PARA DATOS ESCANEADOS-----------------------    

    def crear_frame_estadisticas(self):
        self.frame_estadisticas = ctk.CTkFrame(self)

        self.frame_estadisticas.grid(
            row=3,
            column=0,
            padx=20,
            pady=(10,20),
            sticky="nsew"
        )
        

    

    

   

   

    

    