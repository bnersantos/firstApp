from msilib.schema import ListView
import flet as ft
from flet import AppBar, Text, View
from flet.auth import user
from flet.core.colors import Colors


class User():
    def __init__(self, nome, profissao, salario):
        self.nome = nome
        self.profissao = profissao
        self.salario = salario


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []

    def salvar_dados(e):
        if input_nome == '' or input_profissao == '' or input_salario == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
            return
        else:
            obj_user = User(
                nome=input_nome.value,
                profissao=input_profissao.value,
                salario=input_salario.value,
            )
            lista.append(obj_user)
            input_nome.value = ''
            input_profissao.value = ''
            input_salario.value = ''
            page.overlay.append(msg_sucess)
            msg_sucess = True
            page.update()


        lista.append(obj_user)
        input_nome.value = ""
        input_salario.value = ""
        input_profissao.value = ""
        page.overlay.append(msg_sucess)
        msg_sucess.open = True
        page.update()

    def carregar_dados(e):
        lv_funcionario.controls.clear()
        for user in lista:
            lv_funcionario.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(user.nome),
                    subtitle=ft.Text(user.profissao),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text=user.salario),
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
                    input_nome,
                    input_profissao,
                    input_salario,
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
                        lv_funcionario,
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
        content=Text(),
        bgcolor=Colors.GREEN,
    )
    msg_error = ft.SnackBar(
        content=Text(),
        bgcolor=Colors.RED,
    )
    input_nome = ft.TextField(label="Nome: ")
    input_profissao = ft.TextField(label="Profissao: ")
    input_salario = ft.TextField(label="Salario: ")
    lv_funcionario = ft.ListView(
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
