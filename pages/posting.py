import time
import flet as ft
from flet_route import Params, Basket
from utils.request import sendMessage, sendMessagePhoto
from utils.style import *
import os
from utils.Validation import Validation
from utils.Databes import Database
from dotenv import load_dotenv
from utils.function import p_link_generate
import shutil

load_dotenv()


class PostingPage:
    token_bot = os.getenv('TOKEN_BOT')
    channel_link = os.getenv('CHANNEL')
    validation = Validation()
    db = Database()
    no_preview = False
    preview = ''

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Posting Page'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 900
        page.window.min_height = 400
        page.fonts = {"gotham": "fonts/font.ttf"}

        # checkbox function
        def checkbox_change(e):
            if e.control.value:
                posting_button.visible = True
                postingDate_field.visible = True
                posting_hint.visible = True
            else:
                posting_button.visible = False
                postingDate_field.visible = False
                posting_hint.visible = False
            posting_button.update()
            postingDate_field.update()
            posting_hint.update()

        # function after click send now
        def on_submit(e):
            message_text = message_field.value
            try:
                print("Sending message:", message_text)  # Для отладки
                if self.no_preview:
                    sendMessagePhoto(self.token_bot, self.channel_link, selected_files.src, message_text)
                    selected_files.src = 'images/preview.jpg'
                    selected_files.update()
                else:
                    response = sendMessage(self.token_bot, self.channel_link, message_text)
                    print("Response from Telegram:", response)
                    if response.get('ok'):
                        print("Message sent successfully!")
                    else:
                        print("Failed to send message:", response.get('description'))
                success_message.size=12
                success_message.update()
                message_field.value = ''
                message_field.update()
                time.sleep(2)
                success_message.size = 0
                success_message.update()
            except Exception as e:
                print("Error:", e)

        # files load function
        def pick_files_result(e: ft.FilePickerResultEvent):
            if e.files:
                file_name = p_link_generate(9)
                selected_files.src = e.files[0].path
                upload_file = os.path.join(os.getcwd(), 'assets/upload')
                new_file = f'{file_name}_{os.path.basename(e.files[0].path)}'
                new_file_path = os.path.join(upload_file, new_file)
                shutil.copy(e.files[0].path, new_file_path)
                self.preview = new_file
                self.preview = True
                selected_files.update()

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
        message_button = ft.ElevatedButton('Send Now', icon='send', bgcolor=hoverBgColor, color=defaultFontColor,
                                           on_click=lambda e: on_submit(e))
        pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
        page.overlay.append(pick_files_dialog)
        upload_button = ft.ElevatedButton('Select File')
        posting_date = ft.Checkbox(label='Delay Send', label_style=ft.TextStyle(color=defaultFontColor),
                                   on_change=checkbox_change)
        postingDate_field = ft.TextField(label='Select Date', bgcolor=secondaryBgColor, border=ft.InputBorder.NONE,
                                         visible=False, filled=True, color=secondaryFontColor)
        posting_button = ft.ElevatedButton('Delay post', bgcolor=hoverBgColor, color=defaultFontColor,
                                           icon='schedule_send_rounded', visible=False)
        posting_hint = ft.Text('Select Time in HH:MM format', visible=False, color='red')
        success_message = ft.Text('Post send complete', color=hoverBgColor, size=0)

        # create Row for form
        setting_content = ft.Column(
            controls=[
                selected_files, success_message, message_field,
                ft.Row([posting_date, postingDate_field, posting_hint]),
                ft.Row([message_button, posting_button, upload_button], alignment=ft.MainAxisAlignment.CENTER)
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
