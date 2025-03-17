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
                    # Aqui serão adicionados os componentes futuros
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.app(target=main) 