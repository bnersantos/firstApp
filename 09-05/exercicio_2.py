import flet as ft
from flet import *
from flet import AppBar, Text, View
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
        if input_titulo == '' or input_autor == '' or input_descricao == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
            return
        else:
            obj_livro = Livros(
                titulo=input_titulo.value,
                autor=input_autor.value,
                descricao=input_descricao.value,
            )
            obj_livro.save()
            input_titulo.value = ''
            input_autor.value = ''
            input_descricao.value = ''
            page.overlay.append(msg_sucess)
            msg_sucess.open = True
            page.update()

    def carregar_dados(e):
        lv_livro.controls.clear()
        livro = select(Livros)
        livros = db_session.execute(livro).scalars().all()
        for l in livros:
            lv_livro.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(l.titulo),
                    subtitle=ft.Text(l.autor),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text=l.descricao),
                        ]
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
                    input_titulo,
                    input_autor,
                    input_descricao,
                    ft.ElevatedButton(
                        text="Salvar",
                        on_click=lambda _: salvar_dados(e),
                    ),
                    ft.ElevatedButton(
                        text="Carregar",
                        on_click=lambda _: page.go("/segunda"),
                    )
                ],
            )
        )
        if page.route == "/segunda":
            carregar_dados(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_livro,
                    ],
                )
            )
        page.update()

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
        content=Text("Não deixec campo vazio!"),
        bgcolor=Colors.RED,
    )
    input_titulo = ft.TextField(label="Título: ")
    input_autor = ft.TextField(label="Autor: ")
    input_descricao = ft.TextField(label="Descrição: ")
    lv_livro = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1,
    )

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)


# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
