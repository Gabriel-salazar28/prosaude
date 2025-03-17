import flet as ft
from flet import Page, Window, WindowDragArea, colors

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
                    # Aqui serão adicionados os componentes futuros
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.app(target=main) 