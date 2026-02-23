import flet as ft

def main(page: ft.Page):
    page.title ="Contenedor flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    txt_numero = ft.TextField(value = "0", text_align = ft.TextAlign.RIGHT, width = 100)
    def restar(e):
        txt_numero.value = str(int(txt_numero.value) - 1)
        page.update()
    def sumar(e):
        txt_numero.value = str(int(txt_numero.value) + 1)
        page.update()
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=restar),
                txt_numero,
                ft.IconButton(ft.Icons.ADD, on_click=sumar),
            ],
            alignment = ft.MainAxisAlignment.CENTER,
        )
    )
ft.app(target = main)
    
#uv run main.py
#uv run flet run --web main.py
#uv run flet run --android main.py