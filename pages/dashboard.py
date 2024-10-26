import flet as ft
from flet_route import Params, Basket
from utils.style import *


class DashboardPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Dashboard'
        return ft.View(
            '/dashboard',
            controls=[
                ft.Text('Hello, Dashboard!'),
            ]
        )
