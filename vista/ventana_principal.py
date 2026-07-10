import customtkinter as ctk

# Configuración global de la apariencia
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class VentanaPrincipal(ctk.CTk):

    def __init__(self):
        super().__init__()


        #self.gestor_excel = GestorExcel()
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

        
 

    def crear_frame_base(self):

        self.frame_base = ctk.CTkFrame(self)

        self.frame_base.grid(
        row=1,
        column=0,
        padx=20,
        pady=10,
        sticky="nsew"
        )

    def crear_frame_lector(self):
        self.frame_lector = ctk.CTkFrame(self)

        self.frame_lector.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )
        


    def crear_frame_estadisticas(self):
        self.frame_estadisticas = ctk.CTkFrame(self)

        self.frame_estadisticas.grid(
            row=3,
            column=0,
            padx=20,
            pady=(10,20),
            sticky="nsew"
        )
        

    

    

   

   

    

    