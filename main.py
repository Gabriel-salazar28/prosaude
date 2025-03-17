import flet as ft
from flet import Page, Window, WindowDragArea, colors

def format_date(field):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, field.value)) if field.value else ''
    
    # Formata a data enquanto digita
    if len(text) > 0:
        if len(text) <= 2:
            field.value = text
        elif len(text) <= 4:
            field.value = f"{text[:2]}/{text[2:]}"
        elif len(text) <= 8:
            field.value = f"{text[:2]}/{text[2:4]}/{text[4:]}"
        else:
            field.value = f"{text[:2]}/{text[2:4]}/{text[4:8]}"
        
        field.update()

def validate_form(e, page, campos):
    # Validação dos campos
    is_valid = True
    mensagens_erro = []

    # Verifica campos de texto
    for campo in campos['text_fields']:
        if not campo.value:
            campo.error_text = "Campo obrigatório"
            campo.border_color = "red"
            is_valid = False
        else:
            campo.error_text = None
            campo.border_color = None

    # Verifica radio groups
    for radio_group in campos['radio_groups']:
        if not radio_group.value:
            for radio in radio_group.content.controls:
                radio.label_style = ft.TextStyle(color="red")
            is_valid = False
        else:
            for radio in radio_group.content.controls:
                radio.label_style = None

    # Verifica se pelo menos um checkbox foi marcado em cada grupo
    for grupo in campos['checkbox_groups']:
        if not any(checkbox.value for checkbox in grupo):
            for checkbox in grupo:
                checkbox.label_style = ft.TextStyle(color="red")
            is_valid = False
        else:
            for checkbox in grupo:
                checkbox.label_style = None

    # Verifica o checkbox de consentimento
    if not campos['consentimento'].value:
        campos['consentimento'].label_style = ft.TextStyle(color="red")
        is_valid = False
    else:
        campos['consentimento'].label_style = None

    page.update()

    if not is_valid:
        page.show_snack_bar(
            ft.SnackBar(
                content=ft.Text("Por favor, preencha todos os campos obrigatórios"),
                bgcolor=ft.colors.RED_400
            )
        )
    return is_valid

def main(page: Page):
    # Configuração da janela
    page.window_width = 1920
    page.window_height = 1080
    page.window_resizable = False
    page.window_maximized = True
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.window_frameless = True
    
    # Configuração do tema
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#6495ED"  # Definindo a cor de fundo na página
    
    # Criar todas as referências necessárias
    # Campos de texto
    nome_field = ft.TextField(label="Nome completo*", width=300)
    data_nasc_field = ft.TextField(
        label="Data de Nascimento*",
        width=150,
        bgcolor="white",
        hint_text="DD/MM/AAAA",
        max_length=10,
        on_change=lambda e: format_date(e.control)
    )
    altura_field = ft.TextField(label="Altura*", width=100, bgcolor="white", suffix_text="cm")
    peso_field = ft.TextField(label="Peso*", width=100, bgcolor="white", suffix_text="kg")
    email_field = ft.TextField(label="E-mail*", width=300, bgcolor="white")

    # Radio Groups
    sexo_group = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="M", label="Masculino"),
            ft.Radio(value="F", label="Feminino"),
            ft.Radio(value="O", label="Outro"),
        ])
    )
    
    atividade_fisica_group = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="nunca", label="Nunca"),
            ft.Radio(value="1-2", label="1 a 2 vezes por semana"),
            ft.Radio(value="3-5", label="3 a 5 vezes por semana"),
            ft.Radio(value="diario", label="Todos os dias"),
        ])
    )

    alcool_group = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="nunca", label="Nunca"),
            ft.Radio(value="ocasionalmente", label="Ocasionalmente"),
            ft.Radio(value="frequentemente", label="Frequentemente"),
        ])
    )

    fumo_group = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="sim", label="Sim"),
            ft.Radio(value="nao", label="Não"),
        ]),
    )

    estresse_group = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="baixo", label="Baixo"),
            ft.Radio(value="moderado", label="Moderado"),
            ft.Radio(value="alto", label="Alto"),
        ]),
    )

    sono_group = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="boa", label="Boa, durmo bem todas as noites"),
            ft.Radio(value="regular", label="Regular, às vezes tenho dificuldade para dormir"),
            ft.Radio(value="ruim", label="Ruim, tenho insônia ou acordo cansado"),
        ]),
    )

    # Checkboxes para condições de saúde
    diabetes_check = ft.Checkbox(label="Diabetes", value=False)
    hipertensao_check = ft.Checkbox(label="Hipertensão (pressão alta)", value=False)
    cardiacos_check = ft.Checkbox(label="Problemas cardíacos", value=False)
    respiratorias_check = ft.Checkbox(label="Doenças respiratórias", value=False)
    autoimunes_check = ft.Checkbox(label="Doenças autoimunes", value=False)
    alergias_check = ft.Checkbox(label="Alergias", value=False)
    coluna_check = ft.Checkbox(label="Problemas de coluna ou articulações", value=False)
    nenhuma_condicao_check = ft.Checkbox(label="Nenhuma das opções", value=False)

    # Checkboxes para queixas de saúde
    dor_cabeca_check = ft.Checkbox(label="Dores de cabeça", value=False)
    digestivos_check = ft.Checkbox(label="Problemas digestivos", value=False)
    dores_musculares_check = ft.Checkbox(label="Dores musculares ou articulares", value=False)
    ansiedade_check = ft.Checkbox(label="Ansiedade ou sintomas depressivos", value=False)
    nenhuma_queixa_check = ft.Checkbox(label="Nenhuma das opções", value=False)

    # Checkbox de consentimento
    consentimento_check = ft.Checkbox(label="Sim, concordo", value=False)

    def route_change(route):
        page.views.clear()
        
        if page.route == "/resultados":
            # Página de resultados
            page.views.append(
                ft.View(
                    route="/resultados",
                    bgcolor="#6495ED",
                    controls=[
                        ft.Container(
                            expand=True,
                            bgcolor="#6495ED"
                        )
                    ]
                )
            )
        else:
            # Página inicial com o formulário
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
        ft.Container(
            expand=True,
            bgcolor="#6495ED",
            padding=0,
            margin=0,
            content=ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src="cerebro.png",
                            width=300,
                            height=300,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=20)
                    ),
                    ft.Container(
                        content=ft.Text(
                            "ProSaúde",
                            size=50,
                            font_family="Times New Roman",
                            text_align=ft.TextAlign.CENTER,
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD
                        ),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=20)
                    ),
                    
                    # Container principal com borda arredondada
                    ft.Container(
                        width=800,
                        bgcolor="white",
                        border_radius=10,
                        padding=20,
                        margin=ft.margin.only(top=20, bottom=20),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.START,
                            controls=[
                                # Formulário (agora com largura menor)
                                ft.Container(
                                    width=600,
                                    content=ft.Column([
                                        # Todo o conteúdo do formulário anterior aqui
                                        # Apenas atualizando algumas cores já que o fundo agora é branco
                                        ft.Text("1. DADOS PESSOAIS", size=20, weight=ft.FontWeight.BOLD, color="#6495ED"),
                                        nome_field,
                                        ft.Row([
                                            data_nasc_field,
                                            ft.Text("Sexo:*", color="black", weight=ft.FontWeight.BOLD),
                                            sexo_group,
                                        ]),
                                        ft.Row([
                                            altura_field,
                                            peso_field,
                                        ]),
                                        email_field,
                                        
                                        ft.Divider(),
                                        
                                        # Seção 2 - Condições de Saúde
                                        ft.Text("2. CONDIÇÕES DE SAÚDE", size=20, weight=ft.FontWeight.BOLD, color="#6495ED"),
                                        ft.Text("Você possui ou já teve alguma das seguintes condições?*", color="black"),
                                        ft.Column([
                                            diabetes_check,
                                            hipertensao_check,
                                            cardiacos_check,
                                            respiratorias_check,
                                            autoimunes_check,
                                            alergias_check,
                                            coluna_check,
                                            nenhuma_condicao_check,
                                        ]),
                                        
                                        ft.Divider(),
                                        
                                        # Seção 3 - Estilo de Vida
                                        ft.Text("3. ESTILO DE VIDA", size=20, weight=ft.FontWeight.BOLD, color="#6495ED"),
                                        ft.Text("Com que frequência você pratica atividades físicas?*", color="black"),
                                        atividade_fisica_group,
                                        
                                        ft.Text("Você segue alguma dieta específica?", color="black"),
                                        ft.Row([
                                            ft.RadioGroup(
                                                content=ft.Row([
                                                    ft.Radio(value="sim", label="Sim"),
                                                    ft.Radio(value="nao", label="Não"),
                                                ]),
                                            ),
                                            ft.TextField(label="Qual?", width=200, bgcolor="white"),
                                        ]),
                                        
                                        ft.Text("Com que frequência você consome bebidas alcoólicas?*", color="black"),
                                        alcool_group,
                                        
                                        ft.Text("Você fuma?*", color="black"),
                                        fumo_group,
                                        
                                        ft.Divider(),
                                        
                                        # Seção 4 - Saúde Mental
                                        ft.Text("4. SAÚDE MENTAL E QUALIDADE DE VIDA", size=20, weight=ft.FontWeight.BOLD, color="#6495ED"),
                                        ft.Text("Nos últimos meses, como você avaliaria seu nível de estresse?*", color="black"),
                                        estresse_group,
                                        
                                        ft.Text("Como está a qualidade do seu sono?*", color="black"),
                                        sono_group,
                                        
                                        ft.Text("Você tem alguma queixa de saúde frequente?*", color="black"),
                                        ft.Column([
                                            dor_cabeca_check,
                                            digestivos_check,
                                            dores_musculares_check,
                                            ansiedade_check,
                                            nenhuma_queixa_check,
                                        ]),
                                        
                                        ft.Divider(),
                                        
                                        # Seção 6 - Consentimento
                                        ft.Text("6. CONSENTIMENTO", size=20, weight=ft.FontWeight.BOLD, color="#6495ED"),
                                        ft.Text(
                                            "Declaro que as informações fornecidas são verdadeiras e autorizo o uso dos meus dados para receber recomendações de saúde e bem-estar.*",
                                            color="black",
                                        ),
                                        consentimento_check,
                                        
                                        # Adicione asterisco aos campos obrigatórios
                                        ft.Text("* Campos obrigatórios", size=12, color="red", italic=True),
                                        
                                        # Botão de Envio
                                        ft.ElevatedButton(
                                            text="Analisar",
                                            width=150,
                                            bgcolor=ft.colors.BLUE_700,
                                            color=ft.colors.WHITE,
                                            on_click=validate_form
                                        ),
                                    ]),
                                    padding=20,
                                ),
                            ]
                        ),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.colors.BLACK12,
                            offset=ft.Offset(2, 2),
                        ),
                    ),
                ]
            )
                        )
                    ]
                )
            )
        
        page.update()

    def validate_form(e):
        is_valid = True

        # Validar campos de texto
        text_fields = [nome_field, data_nasc_field, altura_field, peso_field, email_field]
        for field in text_fields:
            if not field.value:
                field.error_text = "Campo obrigatório"
                field.border_color = "red"
                is_valid = False
            else:
                field.error_text = None
                field.border_color = None

        # Validar radio groups
        radio_groups = [sexo_group, atividade_fisica_group, alcool_group, fumo_group, estresse_group, sono_group]
        for group in radio_groups:
            if not group.value:
                for radio in group.content.controls:
                    radio.label_style = ft.TextStyle(color="red")
                is_valid = False
            else:
                for radio in group.content.controls:
                    radio.label_style = None

        # Validar grupos de checkbox (pelo menos um selecionado em cada grupo)
        condicoes_saude = [diabetes_check, hipertensao_check, cardiacos_check, respiratorias_check,
                          autoimunes_check, alergias_check, coluna_check, nenhuma_condicao_check]
        queixas_saude = [dor_cabeca_check, digestivos_check, dores_musculares_check,
                        ansiedade_check, nenhuma_queixa_check]

        for grupo in [condicoes_saude, queixas_saude]:
            if not any(check.value for check in grupo):
                for check in grupo:
                    check.label_style = ft.TextStyle(color="red")
                is_valid = False
            else:
                for check in grupo:
                    check.label_style = None

        # Validar consentimento
        if not consentimento_check.value:
            consentimento_check.label_style = ft.TextStyle(color="red")
            is_valid = False
        else:
            consentimento_check.label_style = None

        page.update()

        if not is_valid:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Por favor, preencha todos os campos obrigatórios"),
                    bgcolor=ft.colors.RED_400
                )
            )
        else:
            # Salvar dados em arquivo texto
            dados = {
                "Nome": nome_field.value,
                "Data de Nascimento": data_nasc_field.value,
                "Sexo": sexo_group.value,
                "Altura": altura_field.value,
                "Peso": peso_field.value,
                "Email": email_field.value,
                "Atividade Física": atividade_fisica_group.value,
                "Consumo de Álcool": alcool_group.value,
                "Fumante": fumo_group.value,
                "Nível de Estresse": estresse_group.value,
                "Qualidade do Sono": sono_group.value,
                "Condições de Saúde": [
                    check.label for check in [diabetes_check, hipertensao_check, cardiacos_check, 
                    respiratorias_check, autoimunes_check, alergias_check, coluna_check] 
                    if check.value
                ],
                "Queixas de Saúde": [
                    check.label for check in [dor_cabeca_check, digestivos_check, 
                    dores_musculares_check, ansiedade_check] 
                    if check.value
                ]
            }
            
            try:
                with open("dados_usuario.txt", "w", encoding="utf-8") as arquivo:
                    for chave, valor in dados.items():
                        if isinstance(valor, list):
                            arquivo.write(f"{chave}: {', '.join(valor)}\n")
                        else:
                            arquivo.write(f"{chave}: {valor}\n")
                            
                page.go('/resultados')  # Redireciona para a nova página
                
            except Exception as e:
                page.show_snack_bar(
                    ft.SnackBar(
                        content=ft.Text("Erro ao salvar os dados. Tente novamente."),
                        bgcolor=ft.colors.RED_400
                    )
                )
        
        return is_valid

    page.on_route_change = route_change
    page.go('/')  # Define a rota inicial

if __name__ == "__main__":
    ft.app(target=main) 