import customtkinter as ctk
from logica.gestor_excel import GestorExcel
from logica.comprobador import Comprobador
from tkinter import filedialog


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

    def configurar_ventana(self):
        self.title("Comprobador de Trazabilidad")

        self.geometry("900x600")

        self.minsize(900, 600)

        self.grid_columnconfigure(0, weight=1)

        for fila in range(4):
            self.grid_rowconfigure(fila, weight=1)


    def crear_widgets(self):

        self.crear_frame_superior()
        self.crear_frame_base()
        self.crear_frame_lector()
        self.crear_frame_estadisticas()
        
    #---------------------------------------------

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

        
    #---------------------------------------

    def crear_frame_base(self):

        # 1. Creo frame
        self.frame_base = ctk.CTkFrame(self)

        # 2. lo coloco XD
        self.frame_base.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )

        self.frame_base.grid_columnconfigure(0, weight=1)

        # 3. le pongo título
        titulo = ctk.CTkLabel(
            self.frame_base,
            text="Base de datos",
            font=("Arial", 20, "bold")
        )

        titulo.grid(row=0, column=0, pady=(15, 5))

        # 4. Creo la etiqueta
        self.label_base = ctk.CTkLabel(
            self.frame_base,
            text="Base cargada: Ninguna"
        )

        self.label_base.grid(
            row=1,
            column=0,
            pady=5
        )

        # 5. Creo el botón
        self.boton_cargar = ctk.CTkButton(
            self.frame_base,
            text="Seleccionar Excel",
            command=self.seleccionar_excel
        )

        self.boton_cargar.grid(
            row=2,
            column=0,
            pady=(10, 20)
        )
    #---------------------------------------------


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
  

    #-----------------------------------------    

    def crear_frame_estadisticas(self):
        self.frame_estadisticas = ctk.CTkFrame(self)

        self.frame_estadisticas.grid(
            row=3,
            column=0,
            padx=20,
            pady=(10,20),
            sticky="nsew"
        )
        

    

    

   

   

    

    