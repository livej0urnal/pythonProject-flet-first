import flet as ft
from flet_route import Routing, path

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            path(url='/', clear=True, view=LoginPage().view),
            path(url='/signup', clear=False, view=SignupPage().view),
        ]

        Routing(
            page=self.page,
            app_routes=self.app_routes,
        )
        self.page.go(self.page.route)