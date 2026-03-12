import flet as ft

def main(page: ft.Page):
    page.title = "Bienvenido al inicio de sesión."
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 

    titulo = ft.Text(
        value="Inicio de Sesión.", 
        size=30, 
        color=ft.Colors.BLUE_900,
        weight="bold", 
        text_align=ft.TextAlign.CENTER
    )

    nombre = ft.TextField(label="Nombre completo", hint_text="Ingrese el nombre completo")
    contrasena = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, hint_text="Ingrese su contraseña")

    resumen = ft.Text(value="", size=16, color=ft.Colors.BLUE_900)

    def iniciar_sesion(e):
        nombre.error_text = None
        contrasena.error_text = None
        hay_error = False

        if not nombre.value:
            nombre.error_text = "Campo obligatorio"
            hay_error = True
        
        if not contrasena.value:
            contrasena.error_text = "Campo obligatorio"
            hay_error = True

        if not hay_error:
            resumen.value = f"Bienvenido, {nombre.value}. Iniciando sesión..."
            resumen.color = ft.Colors.BLUE_700
        else:
            resumen.value = ""
            
        page.update()

    boton_login = ft.ElevatedButton(
        text="Iniciar Sesión", 
        on_click=iniciar_sesion,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_200, 
            color=ft.Colors.BLUE_900    
        )
    )

    olvido_pass = ft.TextButton(
        text="¿Olvidaste tu contraseña?",
        on_click=lambda _: None 
    )

    page.add(
        ft.Column(
            controls=[
                ft.Row([titulo], alignment=ft.MainAxisAlignment.CENTER),
                nombre,
                contrasena,
                ft.Row([boton_login], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([olvido_pass], alignment=ft.MainAxisAlignment.CENTER), 
                ft.Divider(),
                resumen
            ],
            spacing=20,
            width=500
        )
    )
ft.app(target=main)
