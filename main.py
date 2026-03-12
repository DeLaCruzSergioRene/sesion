import flet as ft

def main(page: ft.Page):
    page.title = "Bienvenido al incio de sesión."
    page.padding = 25
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 

    titulo = ft.Text(
        value="Inicio de Sesión.", 
        size=30, 
        color=ft.Colors.BLUE_900,
        weight="bold", 
        text_align=ft.TextAlign.CENTER
    )

    nombre = ft.TextField(label="Nombre completo", hint_text="Ingrese el nombre completo")
    correo = ft.TextField(label="Correo electrónico", hint_text="Ingrese su correo electrónico")
    edad = ft.TextField(label="Edad del usuario", hint_text="Ingrese su edad")


    resumen = ft.Text(value="", size=16, color=ft.Colors.BLUE_900)

    def mostrar_resumen(e):
        resumen.value = (
            f"Nombre: {nombre.value}\n"
            f"Correo: {correo.value}\n"
            f"Edad: {edad.value}\n"
        )
        page.update()

    boton_resumen = ft.ElevatedButton(
        content=ft.Text("Mostrar resumen"),
        on_click=mostrar_resumen,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_400,
            color=ft.Colors.WHITE
        )
    )

    page.add(
        ft.Column(
            controls=[
                ft.Row([titulo], alignment=ft.MainAxisAlignment.CENTER),
                nombre,
                correo,
                edad,
                ft.Row([boton_resumen], alignment=ft.MainAxisAlignment.CENTER),
                ft.Divider(),
                resumen
            ],
            spacing=20,
            width=500
        )
    )
ft.app(target=main)