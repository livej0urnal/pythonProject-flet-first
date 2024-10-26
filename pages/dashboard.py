import flet as ft
from flet_route import Params, Basket
from utils.style import *
from dotenv import set_key, load_dotenv
from pathlib import Path
import os


class DashboardPage:
    load_dotenv()
    AUTH_USER = False
    check_token = ''
    check_channel = ''
    env_file_path = Path('.') / '.env'
    token_bot = os.getenv('TOKEN_BOT')
    channel_link = os.getenv('CHANNEL')

    def view(self, page: ft.Page, params: Params, basket: Basket):
        self.AUTH_USER = page.session.get('auth_user')
        page.title = 'Dashboard Page'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 900
        page.window.min_height = 400
        page.fonts = {"gotham": "fonts/font.ttf"}
        print(self.token_bot)
        #save data function
        def save_settings(e):
            token = token_input.content.value
            channel = channel_input.content.value
            set_key(dotenv_path=self.env_file_path, key_to_set='TOKEN_BOT', value_to_set=token)
            set_key(dotenv_path=self.env_file_path, key_to_set='CHANNEL', value_to_set=channel)
            token_input.disabled = True
            channel_input.disabled = True
            page.session.set('TOKEN', token)
            page.session.set('CHANNEL', channel)
            self.token_bot = page.session.get('TOKEN_BOT')
            self.channel_link = page.session.get('CHANNEL')
            send_btn.text = 'Save success'
            send_btn.disabled = True
            send_btn.update()
            token_input.update()
            channel_input.update()
            page.update()

        # function for create inputs
        def input_form(label):
            return ft.TextField(label=f'{label}',bgcolor=secondaryBgColor,border=ft.InputBorder.NONE,filled=True,color=secondaryFontColor)

        # style disable input
        def input_disabled(value):
            return ft.TextField(value=f'{value}', bgcolor=secondaryBgColor, border=ft.InputBorder.NONE, filled=True, disabled=True,
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
                    ft.TextButton('Home', icon='space_dashboard_rounded', style=style_menu,
                                  on_click=lambda e: page.go('/dashboard')),
                    ft.TextButton('Post', icon='post_add', style=style_menu,
                                  on_click=lambda e: page.go('/post')),
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

        # token input
        token_input = ft.Container(
            content=input_form('Token'),
            border_radius=15
        )

        # channel input
        channel_input = ft.Container(
            content=input_form('Channel ID'),
            border_radius=15
        )

        # save data
        send_btn = ft.ElevatedButton('Save', bgcolor=hoverBgColor, color=defaultFontColor, icon='settings', on_click=lambda e: save_settings(e))

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
                        # body right
                        ft.Container(
                            expand=4,
                            padding=ft.padding.symmetric(15, 10),
                            content=ft.Column([header, token_input, channel_input, send_btn]),
                        )
                    ]
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )
