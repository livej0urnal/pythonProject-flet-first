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
        border_radius=15,
        padding=5
    )

    password_input = ft.Container(
        content=ft.TextField(label='Password',
                             password=True, can_reveal_password=True,
                             bgcolor=secondaryBgColor,
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color=secondaryFontColor),
        border_radius=15,
        padding=5
    )

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Login Page'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 400,
        page.fonts = {"gotham": "fonts/font.ttf"},
        signup_link = ft.Container(
            ft.Text('Create Account',
                    color=defaultFontColor),
            on_click=lambda e:page.go('/signup')
        )

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
                                    ft.Text('Hello User',
                                            color=defaultFontColor,
                                            size=25,
                                            weight=ft.FontWeight.NORMAL,
                                            font_family='gotham'),
                                    self.email_input,
                                    self.password_input,
                                    ft.Container(
                                        ft.Text('Login', color=defaultFontColor, font_family="gotham"),
                                        alignment=ft.alignment.center, height=40, bgcolor=hoverBgColor, padding=10
                                    ),
                                    signup_link
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
                                            size=140, ),
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
