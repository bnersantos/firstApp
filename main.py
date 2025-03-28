import flet as ft
from flet.core.textfield import TextField


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667
    # Definição de fuções
    def exibir_nome(e):
        txt_resultado.value = input_nome.value
        page.update()
    # Criação de componentes
    input_nome = ft.TextField(label="Nome: ",
                            color="lightgreen",
                            hint_text="Digite seu nome",
                            )
    btn_enviar = ft.FilledButton(text="Enviar",
                            width=page.window.width,
                            on_click=exibir_nome,
                            )
    txt_resultado = ft.Text(value="")
    # Construir o layout
    page.add(
        ft.Column(
            [
                input_nome,
                btn_enviar,
                txt_resultado,
            ]
        )
    )

ft.app(main)