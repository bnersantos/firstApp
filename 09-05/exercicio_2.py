import flet as ft
from flet import *
from flet import AppBar, Text, View, ListView
from flet.core.colors import Colors
from models import Livros, db_session
from sqlalchemy import select


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções

    def salvar_dados(e):
        if input_titulo.value == "" or input_autor.value == "" or input_descricao.value == "" or  input_categoria.value == "":
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
            return
        else:
            obj_livro = Livros(
                titulo=input_titulo.value,
                autor=input_autor.value,
                categoria=input_categoria.value,
                descricao=input_descricao.value,
            )
            obj_livro.save()
            input_titulo.value = ''
            input_autor.value = ''
            input_categoria.value = ''
            input_descricao.value = ''
            page.overlay.append(msg_sucess)
            msg_sucess.open = True
            page.update()

    def exibir_detalhes(titulo, autor, descricao, categoria):
        livro.value = (f"Título: \n {titulo}; \n\nAutor: \n {autor}; \n\nCategoria: \n {categoria} \n\nDescrição: \n {descricao}")
        page.update()
        page.go('/listar_detalhes')

    def carregar_dados(e):
        lv_livro.controls.clear()
        livro = select(Livros)
        livros = db_session.execute(livro).scalars().all()
        for l in livros:
            lv_livro.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.BOOK),
                    title=ft.Text(l.titulo),
                    subtitle=ft.Text(l.autor),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.INFO,
                        items=[
                            ft.PopupMenuItem(text="Detalhes")
                        ],
                        on_select=lambda _, liv=l: exibir_detalhes(liv.titulo, liv.autor, liv.descricao, liv.categoria),

                    )
                )
            )

        page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ft.Text('Cadastro de livros: \n'),
                    input_titulo,
                    input_autor,
                    input_categoria,
                    input_descricao,
                    ft.ElevatedButton(
                        text="Salvar",
                        on_click=lambda _: salvar_dados(e),
                    ),
                    ft.ElevatedButton(
                        text="Exibir Lista",
                        on_click=lambda _: page.go("/listar_livros"),
                    )
                ],
            )
        )
        if page.route == "/listar_livros" or page.route == "/listar_detalhes":
            carregar_dados(e)
            page.views.append(
                View(
                    "/listar_livros",
                    [
                        AppBar(title=Text("Lista de Livros"), bgcolor=Colors.PRIMARY),
                        lv_livro,
                    ],
                )
            )
        page.update()
        if page.route == "/listar_detalhes":
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text("Detalhes"), bgcolor=Colors.ON_PRIMARY),
                        livro
                    ]
                )
            )

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Componentes
    msg_sucess = ft.SnackBar(
        content=Text("Livro cadastrado!"),
        bgcolor=Colors.GREEN,
    )

    msg_error = ft.SnackBar(
        content=Text("Não deixe o campo vazio!"),
        bgcolor=Colors.RED,
    )
    input_titulo = ft.TextField(label="Título: ")
    input_autor = ft.TextField(label="Autor: ")
    input_categoria = ft.TextField(label="Categoria: ")
    input_descricao = ft.TextField(label="Descrição: ")
    lv_livro = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1,
    )
    livro = ft.Text("")
    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
