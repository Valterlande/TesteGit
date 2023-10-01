import flet as ft


def main(page: ft.Page):
    print('Olá mundo')

    lbl = ft.Text(value='TESTE')
    btn = ft.ElevatedButton(text='Aperte')

    page.add(lbl, btn)


ft.app(target=main)
