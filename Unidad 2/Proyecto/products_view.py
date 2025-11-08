import tkinter as tk
from tkinter import ttk, messagebox
from products_controller import ProductController

class ProductsView:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title(f"📦 Gestión de Productos - {username}")
        self.root.geometry("1200x650")
        self.root.configure(bg="#f8f9fa")
        self.product_controller = ProductController()
        
        self.center_window()
        self.create_widgets()
        self.load_products()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def center_window(self):
        self.root.update_idletasks()
        w, h = self.root.winfo_width(), self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f'{w}x{h}+{x}+{y}')
    
    def lighten_color(self, color, factor=0.2):
        """Aclara un color hexadecimal"""
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        light_rgb = tuple(min(255, int(c + (255 - c) * factor)) for c in rgb)
        return f'#{light_rgb[0]:02x}{light_rgb[1]:02x}{light_rgb[2]:02x}'
    
    def create_widgets(self):
        # Header moderno
        top_frame = tk.Frame(self.root, bg="#2d3436", height=80)
        top_frame.pack(fill="x")
        top_frame.pack_propagate(False)
        
        # Información de usuario
        user_info_frame = tk.Frame(top_frame, bg="#2d3436")
        user_info_frame.pack(side="left", padx=30, pady=20)
        
        tk.Label(
            user_info_frame,
            text="👤",
            font=("Segoe UI", 16),
            bg="#2d3436",
            fg="white"
        ).pack(side="left")
        
        tk.Label(
            user_info_frame,
            text=f"Bienvenido/a, {self.username}",
            font=("Segoe UI", 16, "bold"),
            bg="#2d3436",
            fg="white"
        ).pack(side="left", padx=(10, 0))
        
        # Botones del header
        btn_frame = tk.Frame(top_frame, bg="#2d3436")
        btn_frame.pack(side="right", padx=30, pady=20)
        
        header_buttons = [
            ("👥 Usuarios", "#00cec9", self.volver_usuarios),
            ("🚪 Cerrar Sesión", "#e74c3c", self.logout)
        ]
        
        for text, color, cmd in header_buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Segoe UI", 10, "bold"),
                bg=color,
                fg="white",
                relief="flat",
                cursor="hand2",
                command=cmd,
                padx=15,
                pady=8
            )
            btn.pack(side="left", padx=(10, 0))
            
            # Efecto hover
            def on_enter(e, button=btn, color=color):
                button.config(bg=self.lighten_color(color))
            
            def on_leave(e, button=btn, color=color):
                button.config(bg=color)
            
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
        
        # Main content
        main_frame = tk.Frame(self.root, bg="#f8f9fa")
        main_frame.pack(fill="both", expand=True, padx=25, pady=20)
        
        # Título
        title_frame = tk.Frame(main_frame, bg="#f8f9fa")
        title_frame.pack(fill="x", pady=(0, 20))
        
        tk.Label(
            title_frame,
            text="📦 Gestión de Productos",
            font=("Segoe UI", 20, "bold"),
            bg="#f8f9fa",
            fg="#2d3436"
        ).pack(side="left")
        
        # Botones de acción
        btn_frame = tk.Frame(main_frame, bg="#f8f9fa")
        btn_frame.pack(fill="x", pady=(0, 20))
        
        buttons = [
            ("➕ Agregar Producto", "#00b894", self.add_product),
            ("✏️ Actualizar Producto", "#fdcb6e", self.edit_product),
            ("🗑️ Eliminar Producto", "#e17055", self.delete_product),
            ("🔄 Actualizar Lista", "#0984e3", self.load_products)
        ]
        
        for text, color, cmd in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                bg=color,
                fg="white",
                font=("Segoe UI", 10, "bold"),
                relief="flat",
                cursor="hand2",
                command=cmd,
                padx=20,
                pady=12
            )
            btn.pack(side="left", padx=(0, 10))
            
            # Efecto hover
            def on_enter(e, button=btn, color=color):
                button.config(bg=self.lighten_color(color))
            
            def on_leave(e, button=btn, color=color):
                button.config(bg=color)
            
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
        
        # Tabla
        self.setup_table(main_frame)
    
    def setup_table(self, parent):
        table_frame = tk.Frame(parent, bg="white", relief="flat", bd=1)
        table_frame.pack(fill="both", expand=True)
        
        style = ttk.Style()
        style.theme_use("clam")
        
        # Configurar estilo moderno
        style.configure("Treeview",
                       background="white",
                       foreground="#2d3436",
                       rowheight=35,
                       fieldbackground="white",
                       font=("Segoe UI", 10),
                       borderwidth=0)
        
        style.configure("Treeview.Heading",
                       background="#2d3436",
                       foreground="white",
                       font=("Segoe UI", 11, "bold"),
                       relief="flat")
        
        style.map("Treeview",
                 background=[("selected", "#74b9ff")],
                 foreground=[("selected", "white")])
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Producto", "Marca", "Precio", "Stock", "Proveedor", "Status"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        self.tree.pack(fill="both", expand=True, padx=1, pady=1)
        scrollbar.config(command=self.tree.yview)
        
        # Configurar columnas
        columns = [
            ("ID", 50),
            ("Producto", 180),
            ("Marca", 120),
            ("Precio", 100),
            ("Stock", 80),
            ("Proveedor", 150),
            ("Status", 80)
        ]
        
        for col, width in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center" if col in ["ID", "Precio", "Stock", "Status"] else "w")
    
    def load_products(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        products = self.product_controller.obtener_productos()
        
        if not products:
            self.tree.insert("", "end", values=(
                "No hay", "productos", "registrados", "", "", "", ""
            ))
        else:
            for product in products:
                status_text = "🟢 Activo" if product['status'] == 1 else "🔴 Inactivo"
                self.tree.insert("", "end", values=(
                    product['id_producto'],
                    product['nombre_producto'],
                    product['marca'] or "N/A",
                    f"${product['precio']:,}",
                    product['stock'],
                    product['proveedor'],
                    status_text
                ))
    
    def add_product(self):
        ProductFormDialog(self.root, self, mode="add")
    
    def edit_product(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona un producto")
            return
        
        product_id = self.tree.item(selected[0])['values'][0]
        product_data = self.product_controller.obtener_producto(product_id)
        if product_data:
            ProductFormDialog(self.root, self, mode="edit", product_data=product_data)
    
    def delete_product(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona un producto")
            return
        
        values = self.tree.item(selected[0])['values']
        if messagebox.askyesno("Confirmar", f"¿Eliminar '{values[1]}'?"):
            success, msg = self.product_controller.eliminar_producto(values[0])
            messagebox.showinfo("Resultado", msg) if success else messagebox.showerror("Error", msg)
            self.load_products()
    
    def volver_usuarios(self):
        self.product_controller.close()
        self.root.destroy()
        
        from user_view import UserView
        new_root = tk.Tk()
        UserView(new_root, self.username)
        new_root.mainloop()
    
    def logout(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Estás seguro de que quieres cerrar sesión?"):
            self.product_controller.close()
            self.root.destroy()
            
            from login_view import LoginView
            new_root = tk.Tk()
            LoginView(new_root)
            new_root.mainloop()
    
    def on_closing(self):
        self.product_controller.close()
        self.root.destroy()


class ProductFormDialog:
    def __init__(self, parent, products_view, mode="add", product_data=None):
        self.parent = parent
        self.products_view = products_view
        self.mode = mode
        self.product_data = product_data
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("➕ Agregar Producto" if mode == "add" else "✏️ Actualizar Producto")
        self.dialog.geometry("500x600")
        self.dialog.resizable(False, False)
        self.dialog.configure(bg="#f8f9fa")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        self.center_window()
        self.create_widgets()
        
        if mode == "edit" and product_data:
            self.fill_form()
    
    def center_window(self):
        self.dialog.update_idletasks()
        w, h = self.dialog.winfo_width(), self.dialog.winfo_height()
        x = (self.dialog.winfo_screenwidth() // 2) - (w // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (h // 2)
        self.dialog.geometry(f'{w}x{h}+{x}+{y}')
    
    def create_widgets(self):
        # Canvas y Scrollbar
        canvas = tk.Canvas(self.dialog, bg="#f8f9fa", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.dialog, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f8f9fa")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Contenido del formulario
        main_frame = tk.Frame(scrollable_frame, bg="#f8f9fa")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        title = "➕ Agregar Producto" if self.mode == "add" else "✏️ Actualizar Producto"
        tk.Label(
            main_frame,
            text=title,
            font=("Segoe UI", 18, "bold"),
            bg="#f8f9fa",
            fg="#2d3436"
        ).pack(pady=(0, 25))
        
        fields = [
            ("📦 Nombre del Producto:", "nombre_producto"),
            ("📊 Stock:", "stock"),
            ("🏢 Proveedor:", "proveedor"),
            ("💰 Precio:", "precio"),
            ("🟢 Status (1=Activo, 0=Inactivo):", "status"),
            ("🏷️ Marca:", "marca"),
            ("📝 Descripción:", "descripcion")
        ]
        
        self.entries = {}
        
        for label_text, field_name in fields:
            tk.Label(
                main_frame,
                text=label_text,
                font=("Segoe UI", 10, "bold"),
                bg="#f8f9fa",
                fg="#2d3436",
                anchor="w"
            ).pack(fill="x", pady=(15, 5))
            
            # ENTRY CORREGIDO - Fondo blanco para ver el texto
            entry = tk.Entry(
                main_frame,
                font=("Segoe UI", 11),
                bg="white",  # CAMBIADO A BLANCO
                fg="#2d3436",
                relief="flat",
                highlightthickness=1,
                highlightbackground="#636e72",
                highlightcolor="#74b9ff",
                insertbackground="#2d3436"
            )
            entry.pack(fill="x", pady=(0, 15), ipady=8)
            self.entries[field_name] = entry
        
        btn_frame = tk.Frame(main_frame, bg="#f8f9fa")
        btn_frame.pack(fill="x", pady=(20, 0))
        
        tk.Button(
            btn_frame,
            text="💾 Guardar",
            font=("Segoe UI", 11, "bold"),
            bg="#00b894",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.save,
            padx=30,
            pady=12
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))
        
        tk.Button(
            btn_frame,
            text="❌ Cancelar",
            font=("Segoe UI", 11),
            bg="#e17055",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.dialog.destroy,
            padx=30,
            pady=12
        ).pack(side="left", expand=True, fill="x", padx=(5, 0))
        
        # Habilitar scroll con rueda del mouse
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    def fill_form(self):
        self.entries['nombre_producto'].insert(0, self.product_data['nombre_producto'])
        self.entries['stock'].insert(0, str(self.product_data['stock']))
        self.entries['proveedor'].insert(0, self.product_data['proveedor'])
        self.entries['precio'].insert(0, str(self.product_data['precio']))
        self.entries['status'].insert(0, str(self.product_data['status']))
        self.entries['marca'].insert(0, self.product_data['marca'] or "")
        self.entries['descripcion'].insert(0, self.product_data['descripcion'] or "")
    
    def save(self):
        nombre = self.entries['nombre_producto'].get().strip()
        stock = self.entries['stock'].get().strip()
        proveedor = self.entries['proveedor'].get().strip()
        precio = self.entries['precio'].get().strip()
        status = self.entries['status'].get().strip()
        marca = self.entries['marca'].get().strip()
        descripcion = self.entries['descripcion'].get().strip()
        
        if self.mode == "add":
            success, msg = self.products_view.product_controller.crear_producto(
                nombre, stock, proveedor, precio, status, marca, descripcion
            )
        else:
            success, msg = self.products_view.product_controller.modificar_producto(
                self.product_data['id_producto'], nombre, stock, proveedor, 
                precio, status, marca, descripcion
            )
        
        if success:
            messagebox.showinfo("Éxito ✅", msg)
            self.products_view.load_products()
            self.dialog.destroy()
        else:
            messagebox.showerror("Error ❌", msg)