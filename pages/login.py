import flet as ft
from flet_route import Params, Basket


class LoginPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Login Page'

        return ft.View(
            "/",
            controls=[
                ft.Text('Login'),
                ft.ElevatedButton('Signup page', on_click=lambda e: page.go("/signup"))
            ]
        )
