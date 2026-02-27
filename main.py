import flet as ft
def main(page: ft.Page):
    def add_clicked(e):
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ''
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Добавь задачу", width=1080, text_align=ft.TextAlign.CENTER)
    page.add(ft.Row([new_task,  ft.ElevatedButton('Добавить', on_click=add_clicked)]))

ft.app(target=main)