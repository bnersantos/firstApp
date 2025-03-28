import flet as ft
from flet.core.textfield import TextField


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667
    # Definição de fuções
    def exibir_soma(e):
        soma = int(input_number1.value) + int(input_number2.value)
        txt_resultado.value = soma
        page.update()
    def exibir_sub(e):
        sub = int(input_number1.value) - int(input_number2.value)
        txt_resultado.value = sub
        page.update()
    def exibir_multi(e):
        multi = int(input_number1.value) * int(input_number2.value)
        txt_resultado.value = multi
        page.update()
    def exibir_div(e):
        div = int(input_number1.value) / int(input_number2.value)
        txt_resultado.value = div
        page.update()
    def limpar(e):
        txt_resultado.value = ""
        input_number1.value = ""
        input_number2.value = ""
        page.update()
    # Criação de componentes
    input_number1 = ft.TextField(label="Número: ",
                            color="lightgreen",
                            hint_text="Digite seu primeiro número",
                            )
    input_number2 = ft.TextField(label="Número: ",
                            color="lightblue",
                            hint_text="Digite seu segundo número",)


    btn_somar = ft.FilledButton(text="Somar",
                            width=page.window.width,
                            on_click=exibir_soma,
                            )

    btn_sub = ft.FilledButton(text="Subtrair",
                            width=page.window.width,
                            on_click=exibir_sub,)

    btn_multi = ft.FilledButton(text="Multiplicar",
                            width=page.window.width,
                            on_click=exibir_multi,)

    btn_div = ft.FilledButton(text="Dividir",
                            width=page.window.width,
                            on_click=exibir_div,)

    btn_limpar = ft.FilledButton(text="Limpar",
                            width=page.window.width,
                            on_click=limpar,)

    txt_resultado = ft.Text(value="")
    # Construir o layout
    page.add(
        ft.Column(
            [
                input_number1,
                input_number2,
                btn_somar,
                btn_sub,
                btn_multi,
                btn_div,
                btn_limpar,
                txt_resultado,
            ]
        )
    )

ft.app(main)
