import flet as ft

def main(page: ft.Page):
    page.title = "App con navegación."
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(
        "Inicio de Sesión.",
        size=30,
        color=ft.Colors.BLUE_900,
        weight="bold"
    )

    nombre = ft.TextField(
    label="Nombre completo.",
    prefix_icon=ft.Icons.PERSON
)
    contrasena = ft.TextField(
    label="Contraseña.",
    password=True,
    can_reveal_password=True,
    prefix_icon=ft.Icons.LOCK
)

    resumen = ft.Text("", color=ft.Colors.BLUE_900)

    def iniciar_sesion(e):
        nombre.error_text = None
        contrasena.error_text = None
        error = False

        if not nombre.value or nombre.value == "":
            nombre.error_text = "Campo obligatorio."
            error = True
        if not contrasena.value or contrasena.value == "":
            contrasena.error_text = "Campo obligatorio."
            error = True
        if not error:
            resumen.value = f"Bienvenido {nombre.value}."
            nav.selected_index = 0
            contenido.content = pantalla_inicio
        else:
            resumen.value = ""
        page.update()

    boton_login = ft.FilledButton(
        content=ft.Text("Iniciar sesión."),
        icon=ft.Icons.LOGIN,
        on_click=iniciar_sesion
    )

    olvido_pass = ft.TextButton(
    content=ft.Text("¿Olvidaste tu contraseña?"),
    on_click=lambda e: None
)

    pantalla_login = ft.Column(
        [
            titulo,
            nombre,
            contrasena,
            boton_login,
            olvido_pass,
            resumen
        ],
        width=400,
        spacing=15
    )

    pantalla_inicio = ft.Column(
    [
        ft.Text("Pantalla de Inicio", size=30, weight="bold"),
        ft.Text("Bienvenido a mi app."),
        ft.Image(
            src="image.png",
            width=500,
            height=500,
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
)

    contenido = ft.Container(content=pantalla_inicio)

    def cambiar_pantalla(e):
        if nav.selected_index == 0:
            contenido.content = pantalla_inicio
        else:
            contenido.content = pantalla_login
        page.update()

    nav = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.LOGIN, label="Login"),
        ],
        on_change=cambiar_pantalla
    )

    page.add(contenido)
    page.navigation_bar = nav

ft.run(main)