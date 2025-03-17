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
    
    # Área principal
    page.add(
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
                            width=200,
                            height=200,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=20)
                    ),
                    ft.Container(
                        content=ft.Text(
                            "ProSaúde",
                            size=43,
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
                                        ft.TextField(label="Nome completo", width=300),
                                        ft.Row([
                                            ft.TextField(
                                                label="Data de Nascimento",
                                                width=150,
                                                bgcolor="white",
                                                hint_text="DD/MM/AAAA",  # Texto de exemplo
                                                max_length=10,  # Limita a 10 caracteres (DD/MM/AAAA)
                                                on_change=lambda e: format_date(e.control),  # Formata enquanto digita
                                            ),
                                            ft.Text("Sexo:", color="black", weight=ft.FontWeight.BOLD),
                                            ft.RadioGroup(
                                                content=ft.Row([
                                                    ft.Radio(value="M", label="Masculino"),
                                                    ft.Radio(value="F", label="Feminino"),
                                                    ft.Radio(value="O", label="Outro"),
                                                ]),
                                            ),
                                        ]),
                                        ft.Row([
                                            ft.TextField(label="Altura", width=100, bgcolor="white", suffix_text="cm"),
                                            ft.TextField(label="Peso", width=100, bgcolor="white", suffix_text="kg"),
                                        ]),
                                        ft.TextField(label="E-mail", width=300, bgcolor="white"),
                                        
                                        ft.Divider(),
                                        
                                        # Seção 2 - Condições de Saúde
                                        ft.Text("2. CONDIÇÕES DE SAÚDE", size=20, weight=ft.FontWeight.BOLD, color="#6495ED"),
                                        ft.Text("Você possui ou já teve alguma das seguintes condições?", color="black"),
                                        ft.Column([
                                            ft.Checkbox(label="Diabetes", value=False),
                                            ft.Checkbox(label="Hipertensão (pressão alta)", value=False),
                                            ft.Checkbox(label="Problemas cardíacos", value=False),
                                            ft.Checkbox(label="Doenças respiratórias", value=False),
                                            ft.Checkbox(label="Doenças autoimunes", value=False),
                                            ft.Checkbox(label="Alergias", value=False),
                                            ft.Checkbox(label="Problemas de coluna ou articulações", value=False),
                                            ft.Checkbox(label="Nenhuma das opções", value=False),
                                        ]),
                                        
                                        ft.Divider(),
                                        
                                        # Seção 3 - Estilo de Vida
                                        ft.Text("3. ESTILO DE VIDA", size=20, weight=ft.FontWeight.BOLD, color="#6495ED"),
                                        ft.Text("Com que frequência você pratica atividades físicas?", color="black"),
                                        ft.RadioGroup(
                                            content=ft.Column([
                                                ft.Radio(value="nunca", label="Nunca"),
                                                ft.Radio(value="1-2", label="1 a 2 vezes por semana"),
                                                ft.Radio(value="3-5", label="3 a 5 vezes por semana"),
                                                ft.Radio(value="diario", label="Todos os dias"),
                                            ]),
                                        ),
                                        
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
                                        
                                        ft.Text("Com que frequência você consome bebidas alcoólicas?", color="black"),
                                        ft.RadioGroup(
                                            content=ft.Column([
                                                ft.Radio(value="nunca", label="Nunca"),
                                                ft.Radio(value="ocasionalmente", label="Ocasionalmente"),
                                                ft.Radio(value="frequentemente", label="Frequentemente"),
                                            ]),
                                        ),
                                        
                                        ft.Text("Você fuma?", color="black"),
                                        ft.RadioGroup(
                                            content=ft.Row([
                                                ft.Radio(value="sim", label="Sim"),
                                                ft.Radio(value="nao", label="Não"),
                                            ]),
                                        ),
                                        
                                        ft.Divider(),
                                        
                                        # Seção 4 - Saúde Mental
                                        ft.Text("4. SAÚDE MENTAL E QUALIDADE DE VIDA", size=20, weight=ft.FontWeight.BOLD, color="#6495ED"),
                                        ft.Text("Nos últimos meses, como você avaliaria seu nível de estresse?", color="black"),
                                        ft.RadioGroup(
                                            content=ft.Column([
                                                ft.Radio(value="baixo", label="Baixo"),
                                                ft.Radio(value="moderado", label="Moderado"),
                                                ft.Radio(value="alto", label="Alto"),
                                            ]),
                                        ),
                                        
                                        ft.Text("Como está a qualidade do seu sono?", color="black"),
                                        ft.RadioGroup(
                                            content=ft.Column([
                                                ft.Radio(value="boa", label="Boa, durmo bem todas as noites"),
                                                ft.Radio(value="regular", label="Regular, às vezes tenho dificuldade para dormir"),
                                                ft.Radio(value="ruim", label="Ruim, tenho insônia ou acordo cansado"),
                                            ]),
                                        ),
                                        
                                        ft.Text("Você tem alguma queixa de saúde frequente?", color="black"),
                                        ft.Column([
                                            ft.Checkbox(label="Dores de cabeça", value=False),
                                            ft.Checkbox(label="Problemas digestivos", value=False),
                                            ft.Checkbox(label="Dores musculares ou articulares", value=False),
                                            ft.Checkbox(label="Ansiedade ou sintomas depressivos", value=False),
                                            ft.Checkbox(label="Nenhuma das opções", value=False),
                                        ]),
                                        
                                        ft.Divider(),
                                        
                                        # Seção 6 - Consentimento
                                        ft.Text("6. CONSENTIMENTO", size=20, weight=ft.FontWeight.BOLD, color="#6495ED"),
                                        ft.Text(
                                            "Declaro que as informações fornecidas são verdadeiras e autorizo o uso dos meus dados para receber recomendações de saúde e bem-estar.",
                                            color="black",
                                        ),
                                        ft.Checkbox(label="Sim, concordo", value=False),
                                        
                                        # Botão de Envio
                                        ft.ElevatedButton(
                                            text="Analisar",
                                            width=150,
                                            bgcolor=ft.colors.BLUE_700,
                                            color=ft.colors.WHITE,
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
    )

if __name__ == "__main__":
    ft.app(target=main) 