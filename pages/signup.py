import flet as ft
from flet_core.colors import with_opacity
from flet_route import Params, Basket
from utils.style import *
from utils.Validation import Validation


class SignupPage:
    validation = Validation()

    # form elements signup
    email_input = ft.Container(
        content=ft.TextField(label='Email',
                             bgcolor=secondaryBgColor,
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color=secondaryFontColor),
        border_radius=15,
        padding=5
    )

    login_input = ft.Container(
        content=ft.TextField(label='Login',
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

    confirm_password_input = ft.Container(
        content=ft.TextField(label='Repeat Password',
                             password=True, can_reveal_password=True,
                             bgcolor=secondaryBgColor,
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color=secondaryFontColor),
        border_radius=15,
        padding=5
    )

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Signup Page'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 400,
        page.fonts = {"gotham": "fonts/font.ttf"}
        login_link = ft.Container(ft.Text('Back to Login', color=defaultFontColor, font_family="gotham"),
                                  on_click=lambda e: page.go("/"), padding=10)
        def signup(e):
            email_value = self.email_input.content.value
            login_value = self.login_input.content.value
            password_value = self.password_input.content.value
            confpassword_value = self.confirm_password_input.content.value

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
                                    ft.Text('Signup Form',
                                            color=defaultFontColor,
                                            size=25,
                                            weight=ft.FontWeight.NORMAL,
                                            font_family='gotham'),
                                    self.email_input,
                                    self.login_input,
                                    self.password_input,
                                    self.confirm_password_input,
                                    ft.Container(
                                        ft.Text('Signup', color=defaultFontColor, font_family="gotham"),
                                        alignment=ft.alignment.center, height=40, bgcolor=hoverBgColor, padding=10,
                                        on_click=lambda e: signup(e)
                                    ),
                                    login_link,

                                ]
                            )
                        ),
                        ft.Container(
                            expand=3,
                            image_src='images/bg_signup.jpg',
                            image_fit=ft.ImageFit.COVER,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(name=ft.icons.VERIFIED_USER_OUTLINED,
                                            color=loginFontColor,
                                            size=140, ),
                                    ft.Text('Signup',
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



