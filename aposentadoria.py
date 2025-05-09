import flet as ft
from flet import *
from flet.core.dropdown import Option


def main(page: ft.Page):
    page.title = "Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667



    def calculo_aposentadoria(e):
        try:
            idade = abs(int(input_idade.value))
            categoria = input_categoria.value
            contribuicao = abs(int(input_contribuicao.value))
            salario = float(input_salario.value)
            genero = input_genero.value

            if idade >= 16:
                if categoria == "Por idade" or "Por tempo":
                    if categoria == "idade":
                        # Por idade
                        if genero == "Masc" or "Fem":
                            if genero == "Masc":
                                if idade >= 65 and contribuicao >= 15:
                                    valor_aposentado = 0.6 * salario + ((contribuicao - 15) * 0.02 * salario)
                                    text_result.value = ("Você pode se aposentar!\n"
                                                            f"R$: {valor_aposentado:.2f}")
                                else:
                                    text_result.value = "Você ainda não pode se aposentar!"
                            elif genero == "Fem":
                                if idade >= 62 and contribuicao >= 15:
                                    valor_aposentado = 0.6 * salario + ((contribuicao - 15) * 0.02 * salario)
                                    text_result.value = ("Você pode se aposentar!\n"
                                                            f"R$: {valor_aposentado:.2f}")
                                else:
                                    text_result.value = "Você ainda não pode se aposentar!"
                            else:
                                text_result.value = "Gênero Inválido, selecione um gênero válido!"
                        else:
                            text_result.value = "Selecione um gênero!"
                    elif categoria == "tempo":
                        # Por tempo
                        if genero == "Masc" or "Fem":
                            if genero == "Masc":
                                if idade >= 51 and contribuicao >= 35 and idade > contribuicao:
                                    valor_aposentado = 0.6 * salario + ((contribuicao - 15) * 0.02 * salario)
                                    text_result.value = ("Você pode se aposentar!\n"
                                                            f"R$: {valor_aposentado:.2f}\n")
                                else:
                                    text_result.value = "Você ainda naõ pode se aposentar!"
                            else:
                                if idade >= 46 and contribuicao >= 30 and idade > contribuicao:
                                    valor_aposentado = 0.6 * salario + ((contribuicao - 15) * 0.02 * salario)
                                    text_result.value = ("Você pode se aposentar!\n"
                                                            f"R$: {valor_aposentado:.2f}\n")
                        else:
                            text_result.value = "Selecione um gênero"
                    else:
                        text_result.value = "Categoria Inválida, escolha uma válida!"
                else:
                    text_result.value = "Escolha um categoria válida"
            else:
                text_result.value =  "Idade Inválida, para trabalhar de carteira assinada necessita dos 16 anos completos!"
            page.update()
            page.go("/resultado")
        except ValueError:
            text_result.value = ("Valor Inválido!")
            page.update()
            page.go("/resultado")
        except TypeError:
            text_result.value = ("Tipo Inválido!")
            page.update()
            page.go("/resultado")

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Menu"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text="Simulação de Aposentadoria", on_click=lambda _: page.go("/simulacao")),
                    ElevatedButton(text="Como é feito o Cálculo?", on_click=lambda _: page.go("/condicoes"))

                ],

            )
        )

        if page.route == "/simulacao":
            page.views.append(
                View(
                    "/simulacao",
                    [
                        AppBar(title=Text("Simulação"), bgcolor=Colors.PRIMARY_CONTAINER),
                        input_idade,
                        input_contribuicao,
                        input_salario,
                        input_genero,
                        input_categoria,
                        ElevatedButton("Simular", on_click=lambda _e: calculo_aposentadoria(e)),
                        ElevatedButton("Voltar", on_click=lambda _e: page.go("/")),
                    ],
                )
            )
        elif page.route == "/resultado":
            page.views.append(
                View(
                    "/resultado",
                    [
                        AppBar(title=Text("Resultado"), bgcolor=Colors.PRIMARY_CONTAINER),
                        text_result,
                    ]

                )
            )
        elif page.route == "/condicoes":
            page.views.append(
                View(
                    "condicoes",
                    [

                        Text("Condições de Aposentadoria", size=22, weight="bold", color="blue"),
                        Divider(),

                        Text("➡️ Para aposentar-se por idade: \n"
                             "- Homens: 65 anos e pelo menos 15 anos de contribuição.\n"
                             "- Mulheres 62 anos e pelo menos 15 anos de contribuição."),
                        Divider(),

                        Text("➡️ Para aposentar-se por tempo de contribuição: \n"
                             "- Homens: 35 anos de contribuição."
                             "- Mulheres: 30 anos de contrubuição."),
                        Divider(),

                        Text("➡️ O cáculo do benefício considera: \n"
                             "- 60% da média salarial + 2% para cada ano extra de contribuição após 15 anos."),
                        Divider(),

                        ElevatedButton(text="Voltar", on_click=lambda _: page.go("/"))
                    ]
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_views = page.views[-1]
        page.go(top_views.route)

    text_result = ft.Text("", size=18, weight="bold", color="red")
    input_idade = ft.TextField(label="Idade: ")
    input_contribuicao = ft.TextField(label="Tempo de Contribuição: ")
    input_salario = ft.TextField(label="Salário Médio: ")
    input_categoria = ft.Dropdown(
        label="Categorias",
        width=page.window.width,
        options=[Option(key="idade", text="Por Idade"), Option(key="tempo", text="Por Tempo")],
    )
    input_genero = ft.Dropdown(
        label="Gênero",
        width=page.window.width,
        options=[Option(key="Masc", text="Masculino"), Option(key="Fem", text="Femenino")],
    )
    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.go(page.route)


ft.app(main)
