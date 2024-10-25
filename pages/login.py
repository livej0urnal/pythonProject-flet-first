import flet as ft
from flet_core.colors import with_opacity
from flet_route import Params, Basket
from utils.style import *


class LoginPage:
    # add email input with styles
    email_input = ft.Container(
        content=ft.TextField(label='Email',
                             bgcolor=secondaryBgColor,
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color=secondaryFontColor),
        border_radius=15
    )

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Login Page'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 400,
        page.fonts = {"gotham": "fonts/font.ttf"}

        return ft.View(
            "/",
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=2,
                            padding=ft.padding.all(40),
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text('Hello Administrator',
                                            color=defaultFontColor,
                                            size=25,
                                            weight=ft.FontWeight.NORMAL,
                                            font_family='gotham')
                                ]
                            )
                        ),
                        ft.Container(
                            expand=3,
                            image_src='images/bg_login.jpg',
                            image_fit=ft.ImageFit.COVER,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(name=ft.icons.LOCK_PERSON_ROUNDED,
                                            color=loginFontColor,
                                            size=140,),
                                    ft.Text('Login',
                                            color=loginFontColor,
                                            size=25,
                                            weight=ft.FontWeight.BOLD)
                                ]
                            )
                        )
                    ]
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )
