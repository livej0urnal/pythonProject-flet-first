import flet as ft
from flet_route import Params, Basket
from utils.style import *
import os
from utils.Validation import Validation
from utils.Databes import Database


class PostingPage:
    token_bot = os.getenv('TOKEN_BOT')
    channel_link = os.getenv('CHANNEL')
    validation = Validation()
    db = Database()

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Posting Page'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 900
        page.window.min_height = 400
        page.fonts = {"gotham": "fonts/font.ttf"}

        # style menu
        style_menu = ft.ButtonStyle(color={ft.ControlState.HOVERED: ft.colors.WHITE,
                                           ft.ControlState.DEFAULT: menuFontColor},
                                    icon_size=14,
                                    overlay_color=hoverBgColor,
                                    shadow_color=hoverBgColor, )
        # active menu link
        style_menu_active = ft.ButtonStyle(color={ft.ControlState.DEFAULT: ft.colors.WHITE,
                                                  ft.ControlState.HOVERED: menuFontColor},
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
                    ft.TextButton('Post', icon='post_add', style=style_menu_active,
                                  on_click=lambda e: page.go('/posting')),
                    ft.TextButton('Test', icon='verified_user', style=style_menu),
                ]
            )
        )

        # input class
        def form_message(label):
            return ft.TextField(label=label, bgcolor=secondaryBgColor, border=ft.InputBorder.NONE,
                                multiline=True,
                                min_lines=1, max_lines=4, filled=True, color=secondaryFontColor)

        # start header
        header = ft.Container(
            content=ft.Row(controls=[
                ft.Text('Posting Page', color=defaultFontColor, font_family='gotham', size=18),
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

        # input fields
        selected_files = ft.Image(src='images/preview.jpg', width=200, height=200, fit=ft.ImageFit.FILL)
        message_field = form_message('Enter Text')
        message_button = ft.ElevatedButton('Send Now', icon='send', bgcolor=hoverBgColor, color=defaultFontColor)
        upload_button = ft.ElevatedButton('Select File')
        posting_date = ft.Checkbox(label='Delay Send', label_style=ft.TextStyle(color=defaultFontColor))
        postingDate_field = ft.TextField(label='Select Date', bgcolor=secondaryBgColor, border=ft.InputBorder.NONE,
                                         visible=False, filled=True, color=secondaryFontColor)
        posting_button = ft.ElevatedButton('Delay post', bgcolor=hoverBgColor, color='red',
                                           icon='schedule_send_rounded', visible=False)
        posting_hint = ft.Text('Select Time in HH:MM format', visible=False)

        # create Row for form
        setting_content = ft.Column(
            controls=[
                selected_files, message_field,
                ft.Row([posting_date, postingDate_field, posting_hint]),
                ft.Row([message_button, posting_button, upload_button])
            ]
        )


        return ft.View(
            '/posting',
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
                            content=ft.Column([header, setting_content]),
                        )
                    ]
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )
