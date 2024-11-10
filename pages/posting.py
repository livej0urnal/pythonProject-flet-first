import time
from datetime import timezone
import flet as ft
from django.utils.datetime_safe import datetime
from flet_route import Params, Basket
from utils.request import sendMessage, sendMessagePhoto
from utils.style import *
import os
from utils.Validation import Validation
from utils.Databes import Database
from dotenv import load_dotenv
from utils.function import p_link_generate
from apscheduler.schedulers.background import BackgroundScheduler
import shutil
import datetime

load_dotenv()


class PostingPage:
    token_bot = os.getenv('TOKEN_BOT')
    channel_link = os.getenv('CHANNEL')
    validation = Validation()
    db = Database()
    no_preview = False
    preview = ''
    scheduler = BackgroundScheduler(timezone='Europe/Moscow')
    scheduler.start()

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
                    self.no_preview = False
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

        #method delay post with image
        def deffer_img(date):
            post = self.db.get_post(date)
            images = f'assets/upload/{post[2]}'
            sendMessagePhoto(self.token_bot, self.channel_link, images, post[1])

        #method delay post no image
        def deferred_post(date):
            post = self.db.get_post(date)
            sendMessagePhoto(self.token_bot, self.channel_link, post[1])

        #function delay posting
        def on_posting_deffer(e):
            if self.validation.is_valid_date(postingDate_field.value):
                postdate = postingDate_field.value
                posttime = postdate.split(":")
                post_hour = int(posttime[0])
                post_minute = int(posttime[1])
                link = p_link_generate(9)
                if self.no_preview:
                    self.db.insert_post(message_field.value, self.preview, link, postingDate_field.value)
                    self.scheduler.add_job(deffer_img, 'date', run_date=datetime.today().replace(hour=post_hour, minute=post_minute, second=0),
                                           args=[link])
                    selected_files.src = 'images/preview.jpg'
                    self.preview = ''
                    self.no_preview = False
                    selected_files.update()
                else:
                    self.db.insert_post(message_field.value, 'NULL', link, postingDate_field.value)
                    self.scheduler.add_job(deffer_img, 'date',
                                           run_date=datetime.today().replace(hour=post_hour, minute=post_minute,
                                                                             second=0),args=[link])
            else:
                error_message.size = 10
                error_message.update()
                time.sleep(2)
                error_message.size = 0
                error_message.update()

        # files load function
        def pick_files_result(e: ft.FilePickerResultEvent):
            if e.files:
                file_name = p_link_generate(9)
                selected_files.src = e.files[0].path
                upload_file = os.path.join(os.getcwd(), 'assets/uploads')
                new_file = f'{file_name}_{os.path.basename(e.files[0].path)}'
                new_file_path = os.path.join(upload_file, new_file)
                shutil.copy(e.files[0].path, new_file_path)
                self.preview = new_file
                self.no_preview = True
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
        upload_button = ft.ElevatedButton('Select File', on_click=lambda e:pick_files_dialog.pick_files(allow_multiple=False))
        posting_date = ft.Checkbox(label='Delay Send', label_style=ft.TextStyle(color=defaultFontColor),
                                   on_change=on_posting_deffer)
        postingDate_field = ft.TextField(label='Select Date', bgcolor=secondaryBgColor, border=ft.InputBorder.NONE,
                                         visible=False, filled=True, color=secondaryFontColor)
        posting_button = ft.ElevatedButton('Delay post', bgcolor=hoverBgColor, color=defaultFontColor,
                                           icon='schedule_send_rounded', visible=False, on_click= lambda e:on_posting_deffer(e))
        posting_hint = ft.Text('Select Time in HH:MM format', visible=False, color='red')
        success_message = ft.Text('Post send complete', color=hoverBgColor, size=0)
        error_message = ft.Text('Publish error', color=red, size=0)

        # create Row for form
        setting_content = ft.Column(
            controls=[
                selected_files, success_message, message_field,
                ft.Row(error_message),
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
