import flet as ft
from router import Router

# This is block starting our
# app
def main(page: ft.Page):
    Router(page)

if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")