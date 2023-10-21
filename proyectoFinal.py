# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3

class Inventario:
    def __init__(self, master=None):
        # self.path = r'X:/Users/ferna/Documents/UNal/Alumnos/2023_S2/ProyInventario'
        # self.db_name = self.path + r'/Inventario.db'
        self.db_name = "Inventario.db" # esto se debe quitar
        # Dimensiones de la pantalla
        ancho=800
        alto=700
        self.actualiza = None

        # Crea ventana principal
        self.win = tk.Tk()
        self.win.minsize(int(ancho/1.25), alto//2)
        self.win.geometry(f"{ancho}x{alto}")
        icon_name = "f2.ico"
        self.win.iconbitmap(icon_name)
        self.win.title("Manejo de Proveedores")

        #Centra la pantalla
        self.centra(self.win,ancho,alto)

        # Contenedor de widgets
        self.label_frame = tk.LabelFrame(master)
        self.label_frame.configure(background="#e0e0e0",font="{Arial} 12 {bold}",labelanchor="n")
        self.tabs = ttk.Notebook(self.label_frame)
        self.tabs.configure(height=800, width=800)

        #Main frame
        self.main_frame = ttk.Frame(self.tabs)

        #Frame de datos
        self.frm1 = ttk.Frame(self.main_frame)
        self.frm1.configure(height=200, width=200)
        self.frm1.columnconfigure((0,3,4,6,7,8,9,10,11,13,14,15), weight=1)
        # self.frm1.columnconfigure((3,4,7,9,10,14), minsize=30)
        self.frm1.rowconfigure((1,2,5,11), weight=1)
        self.frm1.rowconfigure((0,4,7), weight=1, minsize=70)
        self.frm1.rowconfigure((11,), weight=1, minsize=300)

        #Etiqueta IdNit del Proveedor
        self.lblIdNit = ttk.Label(self.frm1)
        self.lblIdNit.configure(text='Id/Nit', anchor="center")
        self.lblIdNit.grid(row=0, column=1, sticky="we", pady=25, padx=5)

        #Captura IdNit del Proveedor
        self.idNit_sv = tk.StringVar()
        self.idNit = ttk.Entry(self.frm1, textvariable=self.idNit_sv)
        self.idNit.configure(takefocus=True, width=15)
        self.idNit.grid(row=0, column=2, columnspan=2, sticky="w", pady=25)
        self.idNit.bind("<Key>", self.validaIdNit)

        #Etiqueta razón social del Proveedor
        self.lblRazonSocial = ttk.Label(self.frm1)
        self.lblRazonSocial.configure(text='Razon social', anchor="center")
        self.lblRazonSocial.grid(row=0, column=5, sticky="we", pady=25, padx=5)

        #Captura razón social del Proveedor
        self.razonSocial = ttk.Entry(self.frm1, width=25)
        self.razonSocial.grid(row=0, column=6, columnspan=5, sticky="w", pady=25)

        #Etiqueta ciudad del Proveedor
        self.lblCiudad = ttk.Label(self.frm1)
        self.lblCiudad.configure(text='Ciudad', anchor="center")
        self.lblCiudad.grid(row=0, column=12, sticky="we", pady=25, padx=5)

        #Captura ciudad del Proveedor
        self.ciudad = ttk.Entry(self.frm1, width=20)
        self.ciudad.grid(row=0, column=13, columnspan=3, sticky="w", pady=25)

        #Separador
        self.separador1 = ttk.Separator(self.frm1)
        self.separador1.configure(orient="horizontal")
        self.separador1.grid(row=3, column=0, columnspan=17, sticky="we", pady=5)

        #Etiqueta Código del Producto
        self.lblCodigo = ttk.Label(self.frm1)
        self.lblCodigo.configure(text='Código', anchor="center")
        self.lblCodigo.grid(row=4, column=1, sticky="we", pady=25, padx=5)

        #Captura el código del Producto
        self.codigo = ttk.Entry(self.frm1, width=10)
        self.codigo.grid(row=4, column=2, sticky="w", columnspan=2, pady=25)

        #Etiqueta descripción del Producto
        self.lblDescripcion = ttk.Label(self.frm1)
        self.lblDescripcion.configure(text='Descripción', anchor="center")
        self.lblDescripcion.grid(row=4, column=5, sticky="we", pady=25, padx=5)

        #Captura la descripción del Producto
        self.descripcion = ttk.Entry(self.frm1, width=25)
        self.descripcion.grid(row=4, column=6, columnspan=5, sticky="w", pady=25)

        #Etiqueta unidad o medida del Producto
        self.lblUnd = ttk.Label(self.frm1)
        self.lblUnd.configure(text='Unidad', anchor="center")
        self.lblUnd.grid(row=4, column=12, sticky="we", pady=25, padx=5)

        #Captura la unidad o medida del Producto
        self.unidad = ttk.Entry(self.frm1, width=10)
        self.unidad.grid(row=4, column=13, sticky="w", pady=25)

        #Etiqueta cantidad del Producto
        self.lblCantidad = ttk.Label(self.frm1)
        self.lblCantidad.configure(text='Cantidad', anchor="center")
        self.lblCantidad.grid(row=7, column=1, sticky="we", pady=25, padx=5)

        #Captura la cantidad del Producto
        self.cantidad = ttk.Entry(self.frm1, width=10)
        self.cantidad.grid(row=7, column=2, sticky="w", pady=25)

        #Etiqueta precio del Producto
        self.lblPrecio = ttk.Label(self.frm1)
        self.lblPrecio.configure(text='Precio $', anchor="center")
        self.lblPrecio.grid(row=7, column=5, sticky="we", pady=25, padx=5)

        #Captura el precio del Producto
        self.precio = ttk.Entry(self.frm1, width=10)
        self.precio.grid(row=7, column=6, sticky="w", pady=25)

        #Etiqueta fecha de compra del Producto
        self.lblFecha = ttk.Label(self.frm1)
        self.lblFecha.configure(text='Fecha', anchor="center")
        self.lblFecha.grid(row=7, column=12, sticky="we", pady=25, padx=5)

        #Captura la fecha de compra del Producto
        self.fecha_sv = tk.StringVar(value="dd/mm/aaaa")
        self.fecha = ttk.Entry(self.frm1, width=10, textvariable=self.fecha_sv)
        self.fecha.grid(row=7, column=13, sticky="w", pady=25)
        for i in ("Button-1", "Left", "Right", "Key","BackSpace", "space"):
            self.fecha.bind(f"<{i}>", self.validaFecha)
        self.fecha.bind("<FocusOut>", self.fechaFocusOut)
        self.fecha.bind("<FocusIn>", self.fechaFocusIn)
        self.fecha_mal = False
        
        #Separador
        self.separador2 = ttk.Separator(self.frm1)
        self.separador2.configure(orient="horizontal")
        self.separador2.grid(row=10, column=0, columnspan=17, sticky="we", pady=5)


        #tablaTreeView
        self.style=ttk.Style()
        self.style.configure("estilo.Treeview", highlightthickness=0, bd=0, background="#e0e0e0", font=('Calibri Light',10))
        self.style.configure("estilo.Treeview.Heading", background='Azure', font=('Calibri Light', 10,'bold')) 
        self.style.layout("estilo.Treeview", [('estilo.Treeview.treearea', {'sticky': 'nswe'})])
        
        #Árbol para mosrtar los datos de la B.D.
        self.treeProductos = ttk.Treeview(self.frm1, style="estilo.Treeview")
        
        self.treeProductos.configure(selectmode="extended")

        # Etiquetas de las columnas para el TreeView
        self.treeProductos["columns"]=("Codigo","Descripcion","Und","Cantidad","Precio","Fecha")
        # Características de las columnas del árbol
        self.treeProductos.column ("#0",          anchor="w",stretch=True,width=3)
        self.treeProductos.column ("Codigo",      anchor="w",stretch=True,width=3)
        self.treeProductos.column ("Descripcion", anchor="w",stretch=True,width=150)
        self.treeProductos.column ("Und",         anchor="w",stretch=True,width=3)
        self.treeProductos.column ("Cantidad",    anchor="w",stretch=True,width=3)
        self.treeProductos.column ("Precio",      anchor="w",stretch=True,width=8)
        self.treeProductos.column ("Fecha",       anchor="w",stretch=True,width=3)

        # Etiquetas de columnas con los nombres que se mostrarán por cada columna
        self.treeProductos.heading("#0",          anchor="center", text='ID / Nit')
        self.treeProductos.heading("Codigo",      anchor="center", text='Código')
        self.treeProductos.heading("Descripcion", anchor="center", text='Descripción')
        self.treeProductos.heading("Und",         anchor="center", text='Unidad')
        self.treeProductos.heading("Cantidad",    anchor="center", text='Cantidad')
        self.treeProductos.heading("Precio",      anchor="center", text='Precio')
        self.treeProductos.heading("Fecha",       anchor="center", text='Fecha')

        self.treeProductos.grid(row=11, column=0, columnspan=16, sticky="news")

        #Scrollbar en el eje Y de treeProductos
        self.scrollbary=ttk.Scrollbar(self.frm1, orient='vertical', command=self.treeProductos.yview)
        self.treeProductos.configure(yscroll=self.scrollbary.set)
        self.scrollbary.grid(row=11, column=16, sticky="ns")

        #Frame 2 para contener los botones
        self.frm2 = ttk.Frame(self.main_frame)
        self.frm2.configure()
        trailingCols = 10
        self.frm2.columnconfigure(
            (
                *range(trailingCols),
                trailingCols+1,
                trailingCols+3,
                trailingCols+5,
                trailingCols+7,
                *range(trailingCols+9,2*trailingCols+8)
            ),
            weight=1
            )
        self.frm2.columnconfigure(
            (
                trailingCols,
                trailingCols+2,
                trailingCols+4,
                trailingCols+6,
                trailingCols+8,
            ),
            minsize=70,
            weight=0
            )
        self.frm2.rowconfigure((0,2), weight=1)

        #Botón para Buscar un Proveedor
        self.btnBuscar = ttk.Button(self.frm2)
        self.btnBuscar.configure(text='Buscar', command=self.buscar)
        self.btnBuscar.grid(row=1, column=trailingCols)

        #Botón para Guardar los datos
        self.btnGrabar = ttk.Button(self.frm2)
        self.btnGrabar.configure(text='Grabar', command=self.adiciona_Registro)
        self.btnGrabar.grid(row=1, column=trailingCols+2)

        #Botón para Editar los datos
        self.btnEditar = ttk.Button(self.frm2)
        self.btnEditar.configure(text='Editar', command=self.carga_Datos)
        self.btnEditar.grid(row=1, column=trailingCols+4)

        #Botón para Elimnar datos
        self.btnEliminar = ttk.Button(self.frm2)
        self.btnEliminar.configure(text='Eliminar')
        self.btnEliminar.grid(row=1, column=trailingCols+6)

        #Botón para cancelar una operación
        self.btnCancelar = ttk.Button(self.frm2)
        self.btnCancelar.configure(text='Cancelar',command = self.limpiaCampos)
        self.btnCancelar.grid(row=1, column=trailingCols+8)

        #Ubicación del Frame 2
        self.frm2.pack(side="bottom", anchor="s", expand=True, fill="both")
        self.label_frame.pack(anchor="center", side="top", expand=True, fill="both")
        
        # Título de la pestaña Ingreso de Datos
        self.frm1.pack(side="top", expand=True, fill="both")
        self.tabs.add(self.main_frame, compound="center", text='Ingreso de datos')
        self.tabs.pack(side="top", expand=True, fill="both")


        # widget Principal del sistema
        self.mainwindow = self.label_frame

    def run(self):
        """Fución de manejo de eventos del sistema"""
        self.mainwindow.mainloop()

    # Métodos utilitarios del sistema-----------------------------------------
    #Rutina de centrado de pantalla
    def centra(self,win: tk.Tk,ancho,alto):
        """ centra las ventanas en la pantalla """ 
        x = win.winfo_screenwidth() // 2 - ancho // 2
        y = win.winfo_screenheight() // 2 - alto // 2
        win.geometry(f'{ancho}x{alto}+{x}+{y}')
        # win.deiconify() # Se usa para restaurar la ventana

    # Validaciones del sistema
    def validaIdNit(self, event: tk.Event):
        ''' Valida que la longitud no sea mayor a 15 caracteres'''
        if self.idNit.selection_present(): return
        if event.char in ("","\t") or len(repr(event.char).strip("\"'\\")) > 1: return
        if len(self.idNit.get()) > 14: #14 porque se ejecuta antes de añadir el caracter
            #after idle para que quite el caracter despues de que se añada
            mssg.showerror('Atención!!','.. ¡Máximo 15 caracteres! ..')
            self.idNit.after_idle(self.idNit.delete,15, "end")

    def isFechaValida(self)-> tuple[bool,str]:
        """ Revisa si la fecha es valida\n
            retorna: 
                -una tupla con el bool como resultado de la validación\n
                -un str como la razon de porque es invalido ("" si es valido)"""
        try:
            dia, mes, año = (int(i) for i in self.fecha_sv.get().split("/"))
        except ValueError:
            return False, "Las fechas deben estar compuestas solo por números enteros positivos"
        es_biciesto = (año%4 == 0) and ((año%100 != 0) or (año%400 == 0))
        max_dia = 31
        if mes > 12 or mes < 0:
            return False, "El mes debe ser un número entero entre 12 y 0"
        elif mes == 2: max_dia =28 + (1 if es_biciesto else 0) #si es biciesto y el mes es febrero 
        #Enero, Marzo, Mayo, Julio,
        elif mes in (1,3,5,7,9,10,12): max_dia = 30
        if dia < 0:
            return False, "El día debe ser un número entero positivo"
        if dia > max_dia or dia < 0:
            mes_str = ( "Enero", "Febrero", "Marzo", "Abril", "Mayo",
                        "Junio", "Julio", "Agosto", "Septiembre",
                        "Octubre", "Noviembre", "Diciembre"
                      )[mes]
            return False, f"Día invalido para {mes_str}, el maximo es {max_dia}"
        return True, ""
    
    def fechaFocusIn(self, _):
        """Se ejecuta cuando se entra al Entry fecha"""
        self.fecha.after_idle(self.fecha.icursor,0) #pone el cusor al inicio del entry
    
    def fechaFocusOut(self, event):
        """Se ejecuta cuando se sale del Entry fecha"""
        valida = self.isFechaValida()
        if (not valida[0]) and self.fecha.get().replace("/","").isnumeric():
            self.validaFecha(event)
            mssg.showerror("Atención!!", "¡Fecha invalida!!!\n"+valida[1])
    
    def validaFecha(self, event: tk.Event):
        """ Mantiene correctamente escrita a la variable fecha"""
        #nota: esta funcion ocurre antes de que se le aplicen cambios al entry por el usuario
        
        brk = False #si es True interrumpe la entrada de valores a self.fecha
        if event.type == 1: position = self.fecha.index("insert")
        else: position = self.fecha.index("insert") #El indice donde se encuentra el cusor
        
        seleccionado = False
        #si esta selecionada parte del texto
        if self.fecha.select_present():
            seleccionado = True
            position = self.fecha.index("sel.first")
            self.fecha.after_idle(self.fecha.select_clear)
            brk = True
            self.fecha.after_idle(self.fecha.icursor, position+1)
        #modificacion del texto dentro del entry -----------------------------------
        #si esta entrando un numero
        if event.keysym.isnumeric():
            #quitar el caracter que estaba en ese espacio
            if position < 10 and not position in (2,5):
                self.fecha.delete(position, position+1)
                #si se seleccionó texto añadir manualmente el caracter
                if seleccionado: self.fecha.insert(position, event.char)
                position += 1
            #pero si esta al final del entry no permitir la entrada del caracter
            else:
                brk = True
        #si esta borrando
        elif event.keysym == "BackSpace" and position > 0:
            #si se seleccionó texto moverlo hacia adelante (se maneja mejor)
            if seleccionado: position += 1
            #reemplazar caracter a borrar con el correspondiente ('d', 'm', o 'a')
            char = "a"
            if position <= 3: char = "d"
            elif position <= 6: char = "m" 
            #si esta despues de un '/' mover el cursor hacia atras para no borrarlo
            if position in (3, 6):
                position -= 1 
            position -= 1
            self.fecha.delete(position,position+1)
            self.fecha.insert(position, char)
            #reposicionar el cursor despues de modificar el entry
            self.fecha.after_idle(self.fecha.icursor, position)
            brk = True
        elif len(event.char) >= 1 and int(event.type) != 4:
            print(event.type)
            #borra el ultimo caracter digitado
            brk = True
        #movimiento por flechas ----------------------------------------------------
        if event.keysym == "Left": position -= 1
        elif event.keysym == "Right": position += 1
        #cuando el cursor llega detras de un '/' lo mueve adelante de el
        #a no ser de que halla texto seleccionado
        if position in (2, 5) and not seleccionado:
            mover = position+(-1 if event.keysym == "Left" else 1)
            self.fecha.after_idle(self.fecha.icursor,mover)
            position = mover
        
        #mostrar validez de fecha --------------------------------------------------
        #si todos los valores de fecha son numeros (exepto los '/')
        #osea ya es una fecha
        if (self.fecha.get().replace("/","")).isnumeric():
            if self.isFechaValida()[0]:
                self.fecha.configure(foreground="black")
            else: self.fecha.configure(foreground="red")
        
        #en caso de que el largo de fecha sea mayor a 10 repararlo
        if len(self.fecha_sv.get())>10: self.fecha_sv.set(self.fecha_sv.get()[:10])
        
        #cuando un metodo que se ejecuto por bind y retorna "break" no se
        #ejecuta el resto de binds (no puede añadir caracteres al Entry)
        if brk: return "break"
    
    #Rutina de limpieza de datos
    def limpiaCampos(self):
        ''' Limpia todos los campos de captura'''
        self.actualiza = None
        self.idNit.config(state = 'normal')
        self.idNit.delete(0,'end')
        self.razonSocial.delete(0,'end')
        self.ciudad.delete(0,'end')
        self.idNit.delete(0,'end')
        self.codigo.delete(0,'end')
        self.descripcion.delete(0,'end')
        self.unidad.delete(0,'end')
        self.cantidad.delete(0,'end')
        self.precio.delete(0,'end')
        self.fecha.delete(0,'end')
    
    #Rutina para cargar los datos del árbol a los entry correspondientes
    def carga_Datos(self):
        if self.actualiza: return
        seleccion = self.treeProductos.selection()
        #solo si se esta seleccionando algo
        if seleccion:
            self.actualiza = seleccion[0]
            self.treeProductos.selection_remove(seleccion)
            self.limpiaCampos()
            #insertando valores del tree a los Entry
            #valores de Productos
            tree_items = self.treeProductos.item(seleccion[0])
            items_Productos = tree_items["values"]
            self.idNit.configure(state="normal")
            self.idNit.insert(0, tree_items["text"]) #"text" porque es el primer campo
            self.idNit.configure(state = 'readonly')
            self.codigo.insert(0,items_Productos[0])
            self.descripcion.insert(0,items_Productos[1])
            self.unidad.insert(0,items_Productos[2])
            self.cantidad.insert(0,items_Productos[3])
            self.precio.insert(0, items_Productos[4])
            self.fecha.insert(0, items_Productos[5])
            
            #valores de Proveedor
            items_proveedor = tuple(
                self.run_Query(
                    f'SELECT Razon_Social, Ciudad FROM Proveedor WHERE idNitProv = "{tree_items["text"]}";'
                    )
                )[0]
            self.razonSocial.insert(0, "" if items_proveedor[0] == None else str(items_proveedor[0]))
            self.ciudad.insert(0, "" if items_proveedor[1] == None else str(items_proveedor[1]))
    
    # Operaciones con la base de datos
    def run_Query(self, query, parametros = ()):
        ''' Función para ejecutar los Querys a la base de datos '''
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametros)
            conn.commit()
        return result

    def lee_treeProductos(self, id:str):
        ''' Limpia la Tabla tablaTreeView y Carga los datos de nuevo
        Si se provee un id solo carga las filas con ese id/Nit'''
        tabla_TreeView = self.treeProductos.get_children()
        for linea in tabla_TreeView:
            self.treeProductos.delete(linea) # Límpia la filas del TreeView
        
        #si dan una id solo mostrar los datos con esa id
        if id != "": id = f' WHERE idNit = "{id}"'
        # Seleccionando los datos de la BD
        # query = '''SELECT * from Proveedor INNER JOIN Productos WHERE idNitProv = idNit ORDER BY idNitProv'''
        query = f"SELECT * FROM Productos{id} ORDER BY idNit;" # hace lo mismo con menos
        db_rows = self.run_Query(query) # db_rows contine la vista del query
        
        # Insertando los datos de la BD en treeProductos de la pantalla
        for row in db_rows:
            # self.treeProductos.insert('',0, text = row[0], values = [row[4],row[5],row[6],row[7],row[8],row[9]])
            self.treeProductos.insert('',0, text = row[0], values = row[1:])

        
        #Lo siguiente insertaria datos a los entry de forma incorrecta
        ''' Al final del for row queda con la última tupla
            y se usan para cargar las variables de captura
        '''
        # self.idNit.insert(0,row[0])
        # self.razonSocial.insert(0,row[1])
        # self.ciudad.insert(0,row[2])
        # self.codigo.insert(0,row[4])
        # self.descripcion.insert(0,row[5])
        # self.unidad.insert(0,row[6])
        # self.cantidad.insert(0,row[7])
        # self.precio.insert(0,row[8])
        # self.fecha.insert(0,row[9])  
    
    def adiciona_Registro(self, event=None):
        '''Adiciona un producto a la BD si la validación es True'''
        invalido = ""
        #validadcion idNit
        id = self.idNit.get()
        if len(id) > 15:
            invalido += "El ID debe ser menor a 15\n"
        elif id == "":
            invalido += "El campo ID no puede estar vacio\n"
        #validadcion codigo
        codigo = self.codigo.get()
        if codigo == "":
            invalido += "El campo codigo no puede estar vacio\n"
        elif (
            self.actualiza == None and 
            tuple(self.run_Query(f"SELECT count(*) FROM Productos WHERE Codigo = \"{codigo}\""))[0][0] != 0
            ):
            invalido += f"El codigo {codigo} ya existe, los codigos deben ser unicos\n"
        #validaciones de descripcion, unidad, razon social, y ciudad son innecesarias
        #porque no tienen restricciones. Pero si estan vacias deben cambiarse a "NULL"
        desc = self.descripcion.get()
        if desc == "": desc = "NULL"
        unidad = self.unidad.get()
        if unidad == "": unidad = "NULL"
        razon = self.razonSocial.get()
        if razon == "": razon = "NULL"
        ciudad = self.ciudad.get()
        if ciudad == "": ciudad = "NULL"
        #validadcion cantidad
        cantidad = self.cantidad.get()
        if (not cantidad.isnumeric()) or float(cantidad) < 0:
            invalido += "Las cantidades deben ser números positivos\n"
        else: cantidad = float(cantidad)
        #validadcion precio
        precio = self.precio.get()
        if (not precio.isnumeric()) or float(precio) < 0:
            invalido += "Los precios deben ser números positivos\n"
        else: precio = float(precio)
        #validadcion fecha
        fecha = self.fecha.get()
        fechaValida, porque = self.isFechaValida()
        if not fechaValida:
            invalido += porque
        
        if invalido:
            mssg.showerror("¡Datos Incorrectos!!!", str(invalido))
        else:
            id_exist = self.run_Query(f'SELECT * FROM Proveedor WHERE idNitProv = "{id}";').fetchall()
            try:
                with sqlite3.connect(self.db_name) as conn:
                    cursor = conn.cursor()
                    row_Productos = (f'"{id}"', f'"{codigo}"', f'"{desc}"', f'"{unidad}"', f"{cantidad}", f"{precio}", f'"{fecha}"')
                    if self.actualiza == None:
                        row_Productos = ", ".join(row_Productos)
                        query_Productos = f"INSERT INTO Productos VALUES({row_Productos});"
                        print(query_Productos)
                        cursor.execute(query_Productos)
                    else:
                        row_Productos = (row_Productos[0], *row_Productos[2:])
                        cols = ("IdNit", "Descripcion", "Und", "Cantidad", "Precio", "Fecha")
                        row_Productos = ", ".join(f"{cols[i]} = {v}" for i,v in enumerate(row_Productos))
                        query_Productos = f"UPDATE Productos SET WHERE {row_Productos} Codigo = {codigo};"
                        print(query_Productos)
                        cursor.execute(query_Productos)
                    
                    if id_exist: #Si ya existe el idNit
                        update = [] #van los valores que se deben cambiar
                        null = lambda n:None if n == "NULL" else n
                        if id_exist[0][1] != null(razon): update.append(f'Razon_Social = "{razon}"')
                        if id_exist[0][2] != null(ciudad): update.append(f'Ciudad = "{ciudad}"')
                        if update:
                            update = ", ".join(update)
                            query_proveedor = f"UPDATE Proveedor SET {update} WHERE idNitProv = {id};"
                            print(query_proveedor)
                            cursor.execute(query_proveedor)
                    else: #si no añadir los nuevos datos a Proveedor
                        row_Proveedor = f'"{id}", "{razon}", "{ciudad}"'
                        query_proveedor = f"INSERT INTO Proveedor VALUES({row_Proveedor});"
                        print(query_proveedor)
                        cursor.execute(query_proveedor)
                    conn.commit()
            except Exception as e:
                mssg.showerror("Resultado de la acción", "Ocurrio un error al intentar adicionar el registro")
                raise e
            else:
                mssg.showinfo("Resultado de la acción", "Se añadieron los items a la base de datos correctamente")
                self.lee_treeProductos(id)

    def buscar(self) :
        id = self.idNit.get()
        idExiste = bool(tuple(self.run_Query(f'SELECT count(*) FROM Productos WHERE idNit = "{id}"'))[0][0])
        if idExiste: self.lee_treeProductos(id)
        else: mssg.showerror("Error Id", f"No existe el id: {id}")
        
            
    def editaTreeProveedores(self, event=None):
        ''' Edita una tupla del TreeView'''
        pass
        
    def eliminaRegistro(self, event=None):
        '''Elimina un Registro en la BD'''
        pass

if __name__ == "__main__":
    app = Inventario()
    app.run()