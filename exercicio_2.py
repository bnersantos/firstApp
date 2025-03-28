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
                    AppBar(title=Text("Tela Principal"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
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
                        Text(value= f"Livro:\n {input_titulo.value}\n" +
                                    f" {input_descricao.value}\n"+
                                    f"{input_categoria.value}\n"+
                                    f"{input_autor.value}")
                    ],
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_views = page.views[-1]
        page.go(top_views.route)


    input_titulo = ft.TextField(label="Titulo: ")
    input_descricao = ft.TextField(label="Descrição: ")
    input_categoria = ft.TextField(label="Categoria: ")
    input_autor = ft.TextField(label="Autor: ")
    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)