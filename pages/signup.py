import flet as ft
from flet_route import Params, Basket


class SignupPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Signup Page'

        return ft.View(
            "/signup",
            controls=[
                ft.Text('Signup')
            ]
        )
