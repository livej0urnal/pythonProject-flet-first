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

        # function for create inputs
        def input_form(label):
            return ft.TextField(label=f'{label}',
                                bgcolor=secondaryBgColor,
                                border=ft.InputBorder.NONE,
                                filled=True,
                                color=secondaryFontColor)

        # style menu
        style_menu = ft.ButtonStyle(color={ft.ControlState.HOVERED: ft.colors.WHITE,
                                           ft.ControlState.DEFAULT: menuFontColor},
                                    icon_size=14,
                                    overlay_color=hoverBgColor,
                                    shadow_color=hoverBgColor, )

        # sidebar view
        logo = ft.Container(
            padding=ft.padding.symmetric(17, 13),
            content=ft.Row(
                controls=[
                    ft.Image(src='/images/logo.png', width=150, height=50, fit=ft.ImageFit.FILL),
                    # ft.Text('Dashboard', expand=True, color=defaultFontColor, font_family='gotham', size=16),
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        # sidebar menu
        sidebar_menu = ft.Container(
            padding=ft.padding.symmetric(0, 13),
            content=ft.Column(
                controls=[
                    ft.Text('Navigation', color=menuFontColor, font_family='gotham', size=14),
                    ft.TextButton('Home', icon='space_dashboard_rounded', style=style_menu),
                    ft.TextButton('Post', icon='post_add', style=style_menu),
                    ft.TextButton('Test', icon='verified_user', style=style_menu),
                ]
            )
        )

        # start header
        header = ft.Container(
            content=ft.Row(controls=[
                ft.Text('Dashboard', color=defaultFontColor, font_family='gotham', size=18),
                ft.Row(
                    controls=[
                        ft.CircleAvatar(
                            foreground_image_src='https://core.telegram.org/file/811140327/1/zlN4goPTupk/9ff2f2f01c4bd1b013',
                            content=ft.Text('A')
                        ),
                        ft.IconButton(
                            icon=ft.icons.NOTIFICATIONS_ROUNDED,
                            icon_size=20,
                            hover_color=hoverBgColor,
                            icon_color=defaultFontColor,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        )
        return ft.View(
            '/dashboard',
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        # left
                        ft.Container(
                            expand=1,
                            content=ft.Column(
                                controls=[
                                    logo,
                                    sidebar_menu,
                                ]
                            ),
                            bgcolor=secondaryBgColor,
                        ),
                        #body right
                        ft.Container(
                            expand=4,
                            padding=ft.padding.symmetric(15, 10),
                            content=ft.Column([header])
                        )
                    ]
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )
