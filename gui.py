import customtkinter
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkOptionMenu, CTkToplevel, CTkTextbox, CTkImage
from PIL import Image
import os
from classes import Articulo, Autor, RevistaCientifica
from data import data


def error_popup(message):
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imgs")
    error = customtkinter.CTkToplevel()
    error.geometry("400x200")
    error.title("ERROR")
    error.resizable(False, False)
    screen_width = error.winfo_screenwidth()
    screen_height = error.winfo_screenheight()
    x = (screen_width - 400) // 2
    y = (screen_height - 200) // 2
    error.geometry(f"+{x}+{y}")
    error_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "error.png")), size=(100, 100))
    error_label = customtkinter.CTkLabel(master=error, text="", image=error_image)
    error_label.configure(image=error_image)
    error_label.pack()
    error_text = message
    error_label = customtkinter.CTkLabel(master=error, text=error_text, wraplength=300,
                                         font=customtkinter.CTkFont(size=15))
    error_label.pack()
    CTkButton(master=error, text="REINTENTAR", command=lambda: error_button_event()).pack(expand=True, pady=10,
                                                                                          padx=20)

    def error_button_event():
        error.destroy()


def success_popup(message):
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imgs")
    success = customtkinter.CTkToplevel()
    success.geometry("400x200")
    success.title("OPERACIÓN EXITOSA")
    success.resizable(False, False)
    screen_width = success.winfo_screenwidth()
    screen_height = success.winfo_screenheight()
    x = (screen_width - 400) // 2
    y = (screen_height - 200) // 2
    success.geometry(f"+{x}+{y}")
    success_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "success.png")), size=(100, 100))
    success_label = customtkinter.CTkLabel(master=success, text="", image=success_image)
    success_label.configure(image=success_image)
    success_label.pack()
    success_text = message
    success_label = customtkinter.CTkLabel(master=success, text=success_text, wraplength=300,
                                           font=customtkinter.CTkFont(size=15))
    success_label.pack()
    CTkButton(master=success, text="OK", command=lambda: error_button_event()).pack(expand=True, pady=10,
                                                                                    padx=20)

    def error_button_event():
        success.destroy()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.withdraw()
        self.revista = data()
        self.main_window()

    def main_window(self):
        self.main_window = customtkinter.CTkToplevel()
        self.main_window.title("GESTIÓN DE ARTÍCULOS")
        self.main_window.geometry("1000x500")
        self.main_window.resizable(False, False)
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        x = (screen_width - 1000) // 2
        y = (screen_height - 500) // 2
        self.main_window.geometry(f"+{x}+{y}")

        # Sidebar
        sidebar_frame = customtkinter.CTkFrame(self.main_window, width=140, corner_radius=0)
        sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.main_window.grid_rowconfigure(0, weight=1)
        logo_label = customtkinter.CTkLabel(sidebar_frame, text="REVISTA CIENTÍFICA",
                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        new_button = customtkinter.CTkButton(sidebar_frame, text="AGREGAR ARTÍCULO", command=self.new_button_event)
        new_button.grid(row=1, column=0, padx=20, pady=10)
        pending_button = customtkinter.CTkButton(sidebar_frame, text="PENDIENTES", command=self.pending_button_event)
        pending_button.grid(row=2, column=0, padx=20, pady=10)
        rejected_button = customtkinter.CTkButton(sidebar_frame, text="RECHAZADOS", command=self.rejected_button_event)
        rejected_button.grid(row=3, column=0, padx=20, pady=10)
        marked_button = customtkinter.CTkButton(sidebar_frame, text="SEÑALADOS", command=self.marked_button_event)
        marked_button.grid(row=4, column=0, padx=20, pady=10)
        accepted_button = customtkinter.CTkButton(sidebar_frame, text="ACEPTADOS", command=self.accepted_button_event)
        accepted_button.grid(row=5, column=0, padx=20, pady=10)
        authors_button = customtkinter.CTkButton(sidebar_frame, text="AUTORES", command=self.authors_button_event)
        authors_button.grid(row=6, column=0, padx=20, pady=10)
        volumes_button = customtkinter.CTkButton(sidebar_frame, text="VOLÚMENES", command=self.volumes_button_event)
        volumes_button.grid(row=7, column=0, padx=20, pady=10)
        exit_button = customtkinter.CTkButton(sidebar_frame, text="SALIR", fg_color="#E70000", hover_color="dark red",
                                              command=self.exit_button_event)
        exit_button.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.show_articles = customtkinter.CTkScrollableFrame(master=self.main_window,
                                                              label_font=customtkinter.CTkFont(size=15, weight="bold"),
                                                              corner_radius=5, width=690, height=420)
        self.show_articles.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.show_articles.grid_columnconfigure(0, weight=1)
        self.show_articles.place(relx=0.62, rely=0.5, anchor=customtkinter.CENTER)

        self.pending_button_event()

    def clear_scrollable_frame(self):
        for widget in self.show_articles.winfo_children():
            widget.destroy()

    def load_articles(self, estado, title):
        self.clear_scrollable_frame()
        self.show_articles.configure(label_text=title)
        articles = self.get_articles_by_state(estado)
        for i, articulo in enumerate(articles):
            nombres_autores = [f"{autor.nombre} {autor.apellidos}" for autor in articulo.autores]

            titulo_label = customtkinter.CTkLabel(self.show_articles, text=articulo.titulo,
                                                  font=customtkinter.CTkFont(size=15, weight="bold"))
            titulo_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            autores_label = customtkinter.CTkLabel(self.show_articles, text=", ".join(nombres_autores),
                                                   font=customtkinter.CTkFont(size=12))
            autores_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            eliminar_button = CTkButton(self.show_articles, text="Eliminar",
                                        command=lambda a=articulo: self.eliminar_articulo(a))
            eliminar_button.grid(row=i, column=2, padx=10, pady=5)

            info_button = CTkButton(self.show_articles, text="Editar",
                                    command=lambda a=articulo: self.mostrar_info_articulo(a))
            info_button.grid(row=i, column=3, padx=10, pady=5)

    def eliminar_articulo(self, articulo):
        Articulo.articulos.remove(articulo)
        self.pending_button_event()

    def mostrar_info_articulo(self, articulo):
        estado = articulo.estado
        if estado == "Pendiente de evaluación":
            self.mostrar_info_pendiente(articulo)
        elif estado == "Rechazado":
            self.mostrar_info_rechazado(articulo)
        elif estado == "Aceptado con señalamientos":
            self.mostrar_info_sennalado(articulo)
        elif estado == "Aceptado para publicación":
            self.mostrar_info_aceptado(articulo)

    def mostrar_info_pendiente(self, articulo):
        self.info_articulo_window(articulo, "Pendiente de evaluación", 400, 750)

    def mostrar_info_rechazado(self, articulo):
        self.info_articulo_window(articulo, "Rechazado", 400, 680)

    def mostrar_info_sennalado(self, articulo):
        self.info_articulo_window(articulo, "Aceptado con señalamientos", 400, 750)

    def mostrar_info_aceptado(self, articulo):
        self.info_articulo_window(articulo, "Aceptado para publicación", 400, 750)

    def info_articulo_window(self, articulo, estado, width, height):
        info_win = CTkToplevel(self.main_window)
        info_win.title(f"Información del Artículo - {estado}")
        info_win.geometry(f"{width}x{height}")
        info_win.resizable(False, False)
        screen_width = info_win.winfo_screenwidth()
        screen_height = info_win.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        info_win.geometry(f"+{x}+{y}")

        portada_path = articulo.portada if os.path.exists(articulo.portada) else "./covers/default.jpg"
        portada_image = CTkImage(Image.open(portada_path), size=(200, 300))

        portada_label = CTkLabel(info_win, text="", image=portada_image)
        portada_label.configure(image=portada_image)
        portada_label.pack(pady=10)

        CTkLabel(info_win, text=f"Título: {articulo.titulo}", font=customtkinter.CTkFont(size=15, weight="bold")).pack(
            pady=5)
        CTkLabel(info_win,
                 text="Autores: " + ", ".join([f"{autor.nombre} {autor.apellidos}" for autor in articulo.autores]),
                 font=customtkinter.CTkFont(size=12)).pack(pady=5)
        CTkLabel(info_win, text="Palabras clave: " + ", ".join(articulo.palabras_claves),
                 font=customtkinter.CTkFont(size=12)).pack(pady=5)
        CTkLabel(info_win, text="Resumen:", font=customtkinter.CTkFont(size=12)).pack(pady=5)
        CTkLabel(info_win, text=articulo.resumen, font=customtkinter.CTkFont(size=12), wraplength=350).pack(pady=5)

        if estado == "Pendiente de evaluación":
            reject_button = CTkButton(info_win, text="Rechazar",
                                      command=lambda: self.cambiar_estado_articulo(articulo, "Rechazado", info_win))
            reject_button.pack(pady=5)

            mark_button = CTkButton(info_win, text="Agregar Señalamientos",
                                    command=lambda: self.agregar_sennalamientos(articulo, info_win))
            mark_button.pack(pady=5)

            accept_button = CTkButton(info_win, text="Aceptar", command=lambda: self.aceptar_articulo(articulo, info_win))
            accept_button.pack(pady=5)

        if estado == "Aceptado con señalamientos":
            sennalamientos_label = customtkinter.CTkLabel(info_win, text="Señalamientos:",
                                                          font=customtkinter.CTkFont(size=12))
            sennalamientos_label.pack(pady=5)
            sennalamientos_text = ", ".join(articulo.sennalamientos)
            sennalamientos_textbox = customtkinter.CTkLabel(info_win, text=sennalamientos_text,
                                                            font=customtkinter.CTkFont(size=12), wraplength=350)
            sennalamientos_textbox.pack(pady=5)

            modify_button = CTkButton(info_win, text="Modificar Artículo",
                                      command=lambda: self.modificar_articulo(articulo, info_win))
            modify_button.pack(pady=10)

    def modificar_articulo(self, articulo, info_win):
        info_win.destroy()

        modificar_win = CTkToplevel(self.main_window)
        modificar_win.title("Modificar Artículo")
        modificar_win.geometry("400x400")
        modificar_win.resizable(False, False)
        screen_width = modificar_win.winfo_screenwidth()
        screen_height = modificar_win.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 400) // 2
        modificar_win.geometry(f"+{x}+{y}")

        titulo_var = customtkinter.StringVar(value=articulo.titulo)
        palabras_claves_var = customtkinter.StringVar(value=", ".join(articulo.palabras_claves))
        resumen_var = customtkinter.StringVar(value=articulo.resumen)

        CTkLabel(modificar_win, text="Título:").pack(pady=5)
        CTkEntry(modificar_win, textvariable=titulo_var).pack(pady=5)

        CTkLabel(modificar_win, text="Palabras Claves (separadas por comas):").pack(pady=5)
        CTkEntry(modificar_win, textvariable=palabras_claves_var).pack(pady=5)

        CTkLabel(modificar_win, text="Resumen (máximo 250 caracteres):").pack(pady=5)
        resumen_textbox = CTkTextbox(modificar_win, width=350, height=100)
        resumen_textbox.insert("1.0", articulo.resumen)
        resumen_textbox.pack(pady=5)

        def guardar_cambios():
            articulo.titulo = titulo_var.get()
            articulo.palabras_claves = palabras_claves_var.get().split(", ")
            articulo.resumen = resumen_textbox.get("1.0", "end-1c").strip()
            articulo.estado = "Pendiente de evaluación"  # Actualiza el estado aquí
            success_popup("Datos del artículo modificados correctamente.")
            modificar_win.destroy()
            self.pending_button_event()  # Recarga la lista de artículos pendientes

        CTkButton(modificar_win, text="Guardar Cambios", command=guardar_cambios).pack(pady=20)

    def cambiar_estado_articulo(self, articulo, nuevo_estado, info_win=None):
        articulo.estado = nuevo_estado
        success_popup(f"Artículo {nuevo_estado.lower()} correctamente.")
        if info_win:
            info_win.destroy()
        self.pending_button_event()

    def agregar_sennalamientos(self, articulo, info_win):
        info_win.destroy()
        sennalamientos_win = CTkToplevel(self.main_window)
        sennalamientos_win.title("Agregar Señalamientos")
        sennalamientos_win.geometry("400x300")
        sennalamientos_win.resizable(False, False)
        screen_width = sennalamientos_win.winfo_screenwidth()
        screen_height = sennalamientos_win.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 300) // 2
        sennalamientos_win.geometry(f"+{x}+{y}")

        CTkLabel(sennalamientos_win, text="Ingrese los señalamientos separados por coma:",
                 font=customtkinter.CTkFont(size=12)).pack(pady=10)
        sennalamientos_textbox = CTkTextbox(sennalamientos_win, width=300, height=100)
        sennalamientos_textbox.pack(pady=10)

        def save_sennalamientos():
            sennalamientos = sennalamientos_textbox.get("1.0", "end-1c").strip().split(",")
            articulo.sennalamientos = [s.strip() for s in sennalamientos]
            articulo.estado = "Aceptado con señalamientos"
            success_popup("Señalamientos agregados correctamente.")
            sennalamientos_win.destroy()
            self.pending_button_event()

        CTkButton(sennalamientos_win, text="Guardar", command=save_sennalamientos).pack(pady=20)

    def aceptar_articulo(self, articulo, info_win):
        info_win.destroy()
        volumes_win = CTkToplevel(self.main_window)
        volumes_win.title("Asignar Volumen")
        volumes_win.geometry("400x200")
        volumes_win.resizable(False, False)
        screen_width = volumes_win.winfo_screenwidth()
        screen_height = volumes_win.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 200) // 2
        volumes_win.geometry(f"+{x}+{y}")

        CTkLabel(volumes_win, text="Seleccione un volumen para asignar el artículo:",
                 font=customtkinter.CTkFont(size=12)).pack(pady=10)

        vol_names = [vol.nombre for vol in self.revista.volumenes]
        selected_volumen = customtkinter.StringVar(value=vol_names[0] if vol_names else "")
        CTkOptionMenu(volumes_win, variable=selected_volumen, values=vol_names).pack(pady=10)

        def assign_volume():
            selected_vol = selected_volumen.get()
            for vol in self.revista.volumenes:
                if vol.nombre == selected_vol:
                    vol.articulos.append(articulo)
                    articulo.estado = "Aceptado para publicación"
                    success_popup("Artículo aceptado y asignado a volumen correctamente.")
                    volumes_win.destroy()
                    self.pending_button_event()
                    break

        CTkButton(volumes_win, text="Asignar", command=assign_volume).pack(pady=20)

    def new_button_event(self):
        self.new_article_window()

    def new_article_window(self):
        new_article_win = CTkToplevel(self)
        new_article_win.title("CREAR NUEVO ARTÍCULO")
        new_article_win.geometry("400x850")
        new_article_win.resizable(False, False)
        screen_width = new_article_win.winfo_screenwidth()
        screen_height = new_article_win.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 850) // 2
        new_article_win.geometry(f"+{x}+{y}")

        titulo_var = customtkinter.StringVar(value="")
        palabras_claves_textbox = None
        resumen_textbox = None
        tamanno_archivo_var = customtkinter.StringVar(value="")
        portada_path_var = customtkinter.StringVar(value="")

        existing_authors = Autor.get_all_authors()
        author_names = [f"{author.nombre} {author.apellidos}" for author in existing_authors]
        selected_authors_vars = [customtkinter.StringVar(value="") for _ in range(3)]

        CTkLabel(new_article_win, text="Título:").pack(pady=5)
        CTkEntry(new_article_win, textvariable=titulo_var).pack(pady=5)

        for i in range(3):
            CTkLabel(new_article_win, text=f"Autor {i + 1}:").pack(pady=5)
            CTkOptionMenu(new_article_win, variable=selected_authors_vars[i], values=author_names).pack(pady=5)

        CTkLabel(new_article_win, text="Palabras Claves (separadas por comas):").pack(pady=5)
        palabras_claves_textbox = CTkTextbox(new_article_win, width=250, height=100)
        palabras_claves_textbox.pack(pady=5)

        CTkLabel(new_article_win, text="Resumen (máximo 250 caracteres):").pack(pady=5)
        resumen_textbox = CTkTextbox(new_article_win, width=250, height=100)
        resumen_textbox.pack(pady=5)

        CTkLabel(new_article_win, text="Tamaño del Artículo (en KB):").pack(pady=5)
        CTkEntry(new_article_win, textvariable=tamanno_archivo_var).pack(pady=5)

        CTkLabel(new_article_win, text="Nombre del archivo de la portada:").pack(pady=5)
        CTkEntry(new_article_win, textvariable=portada_path_var).pack(pady=5)

        def create_article():
            titulo = titulo_var.get()
            selected_authors = [var.get() for var in selected_authors_vars if var.get()]
            selected_authors_objects = [author for author in existing_authors if
                                        f"{author.nombre} {author.apellidos}" in selected_authors]
            palabras_claves = palabras_claves_textbox.get("1.0", "end-1c").strip()
            resumen = resumen_textbox.get("1.0", "end-1c").strip()
            tamanno_archivo = tamanno_archivo_var.get()
            portada_path = f"./covers/{portada_path_var.get()}"

            if not titulo:
                error_popup("Debe ingresar un título.")
                return
            if not selected_authors:
                error_popup("Debe seleccionar al menos un autor.")
                return
            if not palabras_claves:
                error_popup("Debe ingresar palabras clave.")
                return
            if len(palabras_claves.split(",")) > 5:
                error_popup("Debe ingresar como máximo cinco palabras clave.")
                return
            if not resumen:
                error_popup("Debe ingresar un resumen.")
                return
            if len(resumen) > 250:
                error_popup("El resumen no debe exceder los 250 caracteres.")
                return

            nuevo_articulo = Articulo(titulo, selected_authors_objects, palabras_claves.split(","), resumen,
                                      int(tamanno_archivo), estado="Pendiente de evaluación", portada=portada_path)

            success_popup("Artículo creado correctamente.")
            new_article_win.destroy()
            self.pending_button_event()

        CTkButton(new_article_win, text="Crear Artículo", fg_color="#28a745", hover_color="dark green",
                  command=create_article).pack(pady=20)

    def pending_button_event(self):
        self.load_articles("Pendiente de evaluación", "PENDIENTES DE EVALUACIÓN")

    def rejected_button_event(self):
        self.load_articles("Rechazado", "ARTÍCULOS RECHAZADOS")

    def marked_button_event(self):
        self.load_articles("Aceptado con señalamientos", "ARTÍCULOS SEÑALADOS")

    def accepted_button_event(self):
        self.load_articles("Aceptado para publicación", "ARTÍCULOS ACEPTADOS")

    def authors_button_event(self):
        self.clear_scrollable_frame()
        self.show_articles.configure(label_text="AUTORES")

        autores = Autor.get_all_authors()

        current_row = 0
        for autor in autores:
            autor_label = customtkinter.CTkLabel(self.show_articles, text=f"{autor.nombre} {autor.apellidos}",
                                                 font=customtkinter.CTkFont(size=15, weight="bold"))
            autor_label.grid(row=current_row, column=0, padx=10, pady=5, sticky="w")
            current_row += 1

            articulos_del_autor = [articulo for articulo in Articulo.articulos if autor in articulo.autores]

            for articulo in articulos_del_autor:
                articulo_label = customtkinter.CTkLabel(self.show_articles, text=f"    {articulo.titulo}",
                                                        font=customtkinter.CTkFont(size=12))
                articulo_label.grid(row=current_row, column=0, padx=20, pady=5, sticky="w")

                eliminar_button = CTkButton(self.show_articles, text="Eliminar",
                                            command=lambda a=articulo: self.eliminar_articulo(a))
                eliminar_button.grid(row=current_row, column=1, padx=10, pady=5)

                info_button = CTkButton(self.show_articles, text="Saber más",
                                        command=lambda a=articulo: self.mostrar_info_articulo(a))
                info_button.grid(row=current_row, column=2, padx=10, pady=5)

                current_row += 1

    def volumes_button_event(self):
        self.clear_scrollable_frame()
        self.show_articles.configure(label_text="VOLÚMENES")

        volúmenes = self.revista.volumenes

        current_row = 0
        for volumen in volúmenes:
            nombre_volumen = volumen.nombre
            cantidad_articulos = len(volumen.articulos)
            cantidad_sin_autores_repetidos = len(set([articulo.titulo for articulo in volumen.articulos]))

            volumen_label = customtkinter.CTkLabel(self.show_articles,
                                                   text=f"{nombre_volumen} - {cantidad_articulos} artículos ({cantidad_sin_autores_repetidos} sin autores repetidos)",
                                                   font=customtkinter.CTkFont(size=15, weight="bold"))
            volumen_label.grid(row=current_row, column=0, padx=10, pady=5, sticky="w")
            current_row += 1

            for articulo in volumen.articulos:
                articulo_label = customtkinter.CTkLabel(self.show_articles, text=f"    {articulo.titulo}",
                                                        font=customtkinter.CTkFont(size=12))
                articulo_label.grid(row=current_row, column=0, padx=20, pady=5, sticky="w")

                eliminar_button = CTkButton(self.show_articles, text="Eliminar",
                                            command=lambda a=articulo: self.eliminar_articulo(a))
                eliminar_button.grid(row=current_row, column=1, padx=10, pady=5)

                info_button = CTkButton(self.show_articles, text="Saber más",
                                        command=lambda a=articulo: self.mostrar_info_articulo(a))
                info_button.grid(row=current_row, column=2, padx=10, pady=5)

                current_row += 1

    def exit_button_event(self):
        self.quit()

    def get_articles_by_state(self, estado):
        articulos = []
        for articulo in Articulo.articulos:
            if articulo.estado == estado:
                articulos.append(articulo)
        return articulos

