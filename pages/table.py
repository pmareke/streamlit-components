import streamlit as st

from src.component import Component
from src.header.main import Header
from src.link.main import Link


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Table example")

    def render(self) -> None:
        header = Header()
        header.render("Table Example")

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
