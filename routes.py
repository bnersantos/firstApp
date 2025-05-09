import flet as ft
from flet import *
from flet.core.textfield import TextField

def main(page: ft.Page):
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
                View(
                    "/",
                    [
                        AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                        ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda"))
                    ],
                )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                    AppBar(title=Text("Segunda"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ],
                )
            )

        page.update()
    page.on_route_change = gerenciar_rotas
    page.go(page.route)
    def voltar(e):
        page.views.pop()
        top_views = page.views[-1]
        page.go(top_views.route)

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
ft.app(main)