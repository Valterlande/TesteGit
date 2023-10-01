import flet as ft


def main(page: ft.Page):
    print('Olá mundo')

    lbl = ft.Text(value='TESTE')

    page.add(lbl)


ft.app(target=main)
