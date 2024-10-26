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
        #style menu
        style_menu = ft.ButtonStyle(color={ft.ControlState.HOVERED: ft.colors.WHITE,
                                           ft.ControlState.DEFAULT: menuFontColor},
                                    icon_size=14,
                                    overlay_color=hoverBgColor,
                                    shadow_color=hoverBgColor)

        #sidebar view
        logo = ft.Container(
            padding=ft.padding.symmetric(17, 13),
            content=ft.Row(
                controls=[
                    ft.Image(src='/images/logo.png', width=150, height=50, fit=ft.ImageFit.FILL),
                    ft.Text('Dashboard', expand=True, color=defaultBgColor, font_family='gotham', size=16),
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        #sidebar menu
        sidebar_menu = ft.Container(
            padding=ft.padding.symmetric(0, 13),
            content=ft.Column(
                controls=[
                    ft.Text('Menu', color=menuFontColor, font_family='gotham', size=12),
                    ft.TextButton('Home', icon='space_dashboard_rounded',
                                  style=style_menu)
                ]
            )
        )

        return ft.View(
            '/dashboard',
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        #left
                        ft.Container(
                            expand=1,
                            content=ft.Column(
                                controls=[
                                    logo
                                ]
                            ),
                            bgcolor=secondaryBgColor,
                        )
                    ]
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )
