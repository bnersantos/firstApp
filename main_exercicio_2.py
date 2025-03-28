import flet as ft
from flet.core.textfield import TextField


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    txt_resultado = ft.Text(value="")

    # Definição de fuções
    def par_impar(e):
        if int(input_number.value) != 0:
            if int(input_number.value) % 2 == 0:
                txt_resultado.value = "Número par!"
            else:
                txt_resultado.value = "Ímpar!"
        else:
            txt_resultado.value = 'Zero é neutro, escolha outro número'
        page.update()

    # Criação de componentes
    input_number = ft.TextField(
        label="Número: ",
        color="lightgreen",
    )
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=par_impar,
    )

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_number,
                btn_enviar,
                txt_resultado,
            ]
        )
    )


ft.app(main)
