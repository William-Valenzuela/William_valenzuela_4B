import tkinter as tk
from tkinter import messagebox
from auth_controller import AuthController
from user_view import UserView

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Login - Sistema de Gestión")
        self.root.geometry("450x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e272e")
        
        self.auth_controller = AuthController()
        self.center_window()
        self.create_widgets()
    
    def center_window(self):
        self.root.update_idletasks()
        w, h = self.root.winfo_width(), self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f'{w}x{h}+{x}+{y}')
    
    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#1e272e")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Header con icono
        header_frame = tk.Frame(main_frame, bg="#1e272e")
        header_frame.pack(pady=(20, 30))
        
        # Icono
        tk.Label(
            header_frame,
            text="🚀",
            font=("Segoe UI", 40),
            bg="#1e272e",
            fg="white"
        ).pack()
        
        tk.Label(
            header_frame,
            text="Bienvenido",
            font=("Segoe UI", 24, "bold"),
            bg="#1e272e",
            fg="white"
        ).pack(pady=(10, 5))
        
        tk.Label(
            header_frame,
            text="Sistema de Gestión Integral",
            font=("Segoe UI", 11),
            bg="#1e272e",
            fg="#b2bec3"
        ).pack()
        
        # Card de login
        card_frame = tk.Frame(main_frame, bg="#2d3436", relief="flat", bd=0)
        card_frame.pack(fill="x", padx=10, pady=10)
        
        # Campos de entrada
        input_frame = tk.Frame(card_frame, bg="#2d3436")
        input_frame.pack(fill="x", padx=30, pady=30)
        
        # Campo Usuario
        tk.Label(
            input_frame,
            text="👤 Usuario",
            font=("Segoe UI", 10, "bold"),
            bg="#2d3436",
            fg="#dfe6e9",
            anchor="w"
        ).pack(fill="x", pady=(0, 5))
        
        self.username_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 12),
            bg="white",
            fg="#2d3436",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#636e72",
            highlightcolor="#74b9ff",
            insertbackground="#2d3436"
        )
        self.username_entry.pack(fill="x", pady=(0, 15), ipady=8)
        
        # Campo Contraseña
        tk.Label(
            input_frame,
            text="🔒 Contraseña",
            font=("Segoe UI", 10, "bold"),
            bg="#2d3436",
            fg="#dfe6e9",
            anchor="w"
        ).pack(fill="x", pady=(0, 5))
        
        self.password_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 12),
            bg="white",
            fg="#2d3436",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#636e72",
            highlightcolor="#74b9ff",
            insertbackground="#2d3436",
            show="•"
        )
        self.password_entry.pack(fill="x", pady=(0, 20), ipady=8)
        
        # Botón de Ingresar - CORREGIDO
        ingresar_btn = tk.Button(
            input_frame,
            text="🎯 INGRESAR",
            font=("Segoe UI", 12, "bold"),
            bg="#0984e3",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.login,
            activebackground="#74b9ff",
            activeforeground="white",
            padx=20,
            pady=12
        )
        ingresar_btn.pack(fill="x", pady=(10, 5))
        
        # Efecto hover para botón
        def on_enter_btn(e):
            ingresar_btn.config(bg="#74b9ff")
        def on_leave_btn(e):
            ingresar_btn.config(bg="#0984e3")
        ingresar_btn.bind("<Enter>", on_enter_btn)
        ingresar_btn.bind("<Leave>", on_leave_btn)
        
        # Footer informativo
        footer_frame = tk.Frame(main_frame, bg="#1e272e")
        footer_frame.pack(fill="x", pady=(20, 0))
        
        info_text = """💡 Credenciales de prueba:
admin / admin123   |   juan / juan123   |   maria / maria123"""
        
        tk.Label(
            footer_frame,
            text=info_text,
            font=("Segoe UI", 9),
            bg="#1e272e",
            fg="#b2bec3",
            justify="center"
        ).pack(pady=10)
        
        # Bindings
        self.username_entry.bind('<Return>', lambda e: self.password_entry.focus())
        self.password_entry.bind('<Return>', lambda e: self.login())
        self.username_entry.focus()
    
    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        success, message, user_data = self.auth_controller.login(username, password)
        
        if success:
            messagebox.showinfo("¡Éxito! 🎉", f"¡Bienvenido/a {user_data['nombre']}!\n\n{user_data['correo']}")
            self.auth_controller.close()
            self.root.destroy()
            
            # Nueva ventana con el nombre de usuario
            new_root = tk.Tk()
            UserView(new_root, user_data['username'])
            new_root.mainloop()
        else:
            messagebox.showerror("Error ❌", message)
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus()