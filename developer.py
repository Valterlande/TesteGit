import flet as ft


def main(page: ft.Page):
    
    lbl = ft.Text(value='Olá Flet', size=40,color=ft.colors.DEEP_ORANGE_800)


    page.add(lbl)



ft.app(target=main)
