import tkinter as tk
from tkinter import ttk, messagebox
from user_controller import UserController

class UserView:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title(f"👥 Gestión de Usuarios - {username}")
        self.root.geometry("1100x650")
        self.root.configure(bg="#f8f9fa")
        self.user_controller = UserController()
        
        self.center_window()
        self.create_widgets()
        self.load_users()
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
            text=f"Hola, {self.username}",
            font=("Segoe UI", 16, "bold"),
            bg="#2d3436",
            fg="white"
        ).pack(side="left", padx=(10, 0))
        
        # Botones del header
        btn_frame = tk.Frame(top_frame, bg="#2d3436")
        btn_frame.pack(side="right", padx=30, pady=20)
        
        header_buttons = [
            ("📦 Productos", "#9b59b6", self.ir_productos),
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
            text="📊 Gestión de Usuarios",
            font=("Segoe UI", 20, "bold"),
            bg="#f8f9fa",
            fg="#2d3436"
        ).pack(side="left")
        
        # Botones de acción
        btn_frame = tk.Frame(main_frame, bg="#f8f9fa")
        btn_frame.pack(fill="x", pady=(0, 20))
        
        buttons = [
            ("➕ Agregar Usuario", "#00b894", self.add_user),
            ("✏️ Modificar Usuario", "#fdcb6e", self.edit_user),
            ("🗑️ Eliminar Usuario", "#e17055", self.delete_user),
            ("🔄 Actualizar Lista", "#0984e3", self.load_users)
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
            columns=("ID", "Usuario", "Nombre", "Correo", "Registro"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        self.tree.pack(fill="both", expand=True, padx=1, pady=1)
        scrollbar.config(command=self.tree.yview)
        
        # Configurar columnas
        columns = [
            ("ID", 70),
            ("Usuario", 150),
            ("Nombre", 200),
            ("Correo", 250),
            ("Registro", 150)
        ]
        
        for col, width in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center" if col == "ID" else "w")
    
    def load_users(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        users = self.user_controller.obtener_usuarios()
        
        if not users:
            self.tree.insert("", "end", values=(
                "No hay", "usuarios", "registrados", "en el sistema", ""
            ))
        else:
            for user in users:
                fecha = user['fecha_registro'].strftime("%d/%m/%Y %H:%M") if user['fecha_registro'] else "N/A"
                
                self.tree.insert("", "end", values=(
                    user['id_usuario'],
                    user['username'],
                    user['nombre'],
                    user['correo'],
                    fecha
                ))
    
    def add_user(self):
        UserFormDialog(self.root, self, mode="add")
    
    def edit_user(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona un usuario")
            return
        
        user_id = self.tree.item(selected[0])['values'][0]
        user_data = self.user_controller.obtener_usuario(user_id)
        if user_data:
            UserFormDialog(self.root, self, mode="edit", user_data=user_data)
    
    def delete_user(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona un usuario")
            return
        
        values = self.tree.item(selected[0])['values']
        if messagebox.askyesno("Confirmar", f"¿Eliminar a '{values[2]}'?"):
            success, msg = self.user_controller.eliminar_usuario(values[0])
            messagebox.showinfo("Resultado", msg) if success else messagebox.showerror("Error", msg)
            self.load_users()
    
    def logout(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Estás seguro de que quieres cerrar sesión?"):
            self.user_controller.close()
            self.root.destroy()
            
            from login_view import LoginView
            new_root = tk.Tk()
            LoginView(new_root)
            new_root.mainloop()
    
    def ir_productos(self):
        self.user_controller.close()
        self.root.destroy()
        
        from products_view import ProductsView
        new_root = tk.Tk()
        ProductsView(new_root, self.username)
        new_root.mainloop()
    
    def on_closing(self):
        self.user_controller.close()
        self.root.destroy()


class UserFormDialog:
    def __init__(self, parent, user_view, mode="add", user_data=None):
        self.parent = parent
        self.user_view = user_view
        self.mode = mode
        self.user_data = user_data
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("➕ Agregar Usuario" if mode == "add" else "✏️ Modificar Usuario")
        self.dialog.geometry("450x550")
        self.dialog.resizable(False, False)
        self.dialog.configure(bg="#f8f9fa")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        self.center_window()
        self.create_widgets()
        
        if mode == "edit" and user_data:
            self.fill_form()
    
    def center_window(self):
        self.dialog.update_idletasks()
        w, h = self.dialog.winfo_width(), self.dialog.winfo_height()
        x = (self.dialog.winfo_screenwidth() // 2) - (w // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (h // 2)
        self.dialog.geometry(f'{w}x{h}+{x}+{y}')
    
    def create_widgets(self):
        main_frame = tk.Frame(self.dialog, bg="#f8f9fa")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        title = "➕ Agregar Usuario" if self.mode == "add" else "✏️ Modificar Usuario"
        tk.Label(
            main_frame,
            text=title,
            font=("Segoe UI", 18, "bold"),
            bg="#f8f9fa",
            fg="#2d3436"
        ).pack(pady=(0, 25))
        
        fields = [
            ("👤 Usuario:", "username"),
            ("📛 Nombre completo:", "nombre"),
            ("📧 Correo electrónico:", "correo"),
            ("🔒 Contraseña:", "password")
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
            
            # Entry CORREGIDO - fondo blanco para ver el texto
            entry = tk.Entry(
                main_frame,
                font=("Segoe UI", 11),
                bg="white",  # Cambiado a blanco
                fg="#2d3436",
                relief="flat",
                highlightthickness=1,
                highlightbackground="#636e72",
                highlightcolor="#74b9ff",
                insertbackground="#2d3436"
            )
            
            if field_name == "password":
                entry.config(show="•")
            
            entry.pack(fill="x", pady=(0, 15), ipady=8)
            self.entries[field_name] = entry
        
        if self.mode == "edit":
            tk.Label(
                main_frame,
                text="💡 Deja vacía la contraseña para no cambiarla",
                font=("Segoe UI", 9, "italic"),
                bg="#f8f9fa",
                fg="#7f8c8d"
            ).pack(pady=(0, 15))
        
        btn_frame = tk.Frame(main_frame, bg="#f8f9fa")
        btn_frame.pack(fill="x", pady=(10, 0))
        
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
    
    def fill_form(self):
        self.entries['username'].insert(0, self.user_data['username'])
        self.entries['nombre'].insert(0, self.user_data['nombre'])
        self.entries['correo'].insert(0, self.user_data['correo'])
    
    def save(self):
        username = self.entries['username'].get().strip()
        nombre = self.entries['nombre'].get().strip()
        correo = self.entries['correo'].get().strip()
        password = self.entries['password'].get().strip()
        
        if self.mode == "add":
            success, msg = self.user_view.user_controller.crear_usuario(
                username, nombre, correo, password
            )
        else:
            success, msg = self.user_view.user_controller.modificar_usuario(
                self.user_data['id_usuario'], username, nombre, correo, 
                password if password else None
            )
        
        if success:
            messagebox.showinfo("Éxito ✅", msg)
            self.user_view.load_users()
            self.dialog.destroy()
        else:
            messagebox.showerror("Error ❌", msg)