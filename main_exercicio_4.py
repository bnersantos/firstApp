from multiprocessing.forkserver import read_signed

import flet as ft
from flet.core.textfield import TextField
import datetime


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    # Definição de fuções
    def exibir_data(e):
        data = datetime.datetime.now().date()
        date = datetime.datetime.strptime(input_data.value, "%d/%m/%Y").date()
        idade = data.year - date.year
        mes = data.month
        dia = data.day
        if mes > date.month:
            idade = idade - 1
        else:
            if dia > date.day:
                idade = idade - 1
        if idade < 18:
            txt_resultado.value = f"Você é menor de idade: {idade}."
        elif idade >= 18:
            txt_resultado.value = f"Você é maior de idade : {idade}."
        elif idade <= 0:
            txt_resultado.value = "Data Inválida!"
        page.update()

    # Criação de componentes
    input_data = ft.TextField(label="Data de Nascimento: ",
                              color="lightgreen",
                              hint_text="00/00/0000",
                              )
    btn_enviar = ft.FilledButton(text="Enviar",
                                 width=page.window.width,
                                 on_click=exibir_data,
                                 )
    txt_resultado = ft.Text(value="")
    # Construir o layout
    page.add(
        ft.Column(
            [
                input_data,
                btn_enviar,
                txt_resultado,
            ]
        )
    )


ft.app(main)
