import flet as ft
from flet import *



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
                    AppBar(title=Text("Dados do Usuário"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    input_sobrenome,
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
                        Text(value= f"Bem vindo {input_nome.value}"+ f" {input_sobrenome.value}"),
                    ],
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_views = page.views[-1]
        page.go(top_views.route)


    input_nome = ft.TextField(label="Nome de Usuario: ")
    input_sobrenome = ft.TextField(label="Sobrenome: ")
    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)