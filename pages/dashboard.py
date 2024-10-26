import flet as ft
from flet_route import Params, Basket
from utils.style import *


class DashboardPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Dashboard Page'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 900
        page.window.min_height = 400
        page.fonts = {"gotham": "fonts/font.ttf"}

        #function for create inputs
        def input_form(label):
            return ft.TextField(label=f'{label}',
                                bgcolor=secondaryBgColor,
                                border=ft.InputBorder.NONE,
                                filled=True,
                                color=secondaryFontColor)

        return ft.View(
            '/dashboard',
            controls=[
                ft.Text('Hello, Dashboard!'),
            ]
        )
