import flet as ft
from flet_core.colors import with_opacity
from flet_route import Params, Basket
from utils.function import hash_password
from utils.Databes import Database
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

    error_message = ft.SnackBar(
        content=ft.TextField('Authorization error! Check that your email and password are correct!', color=loginFontColor),
        bgcolor=inputBgErrorColor,
    )

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Login Page'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 400,
        page.fonts = {"gotham": "fonts/font.ttf"}
        signup_link = ft.Container(ft.Text('Create Account', color=defaultFontColor, font_family="gotham"),
                                   on_click=lambda e: page.go('/signup'), padding=10)
        #function authorization
        def authorization(e):
            db = Database()
            email = self.email_input.content.value
            password = hash_password(self.password_input.content.value)
            if db.authorization(email, password):
                page.session.set('auth_user', True)
                page.go('/dashboard')
            else:
                self.error_message.open = True
                page.overlay.append(self.error_message)
                page.update()

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
                                    self.error_message,
                                    ft.Container(
                                        ft.Text('Login', color=defaultFontColor, font_family="gotham"),
                                        alignment=ft.alignment.center, height=40, bgcolor=hoverBgColor, padding=10,
                                        on_click=lambda e: authorization(e)
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
