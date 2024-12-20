import streamlit as st

from src.component import Component
from src.header.main import Header
from src.link.main import Link
from src.title.main import Title


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Title example")

    def render(self) -> None:
        header = Header()
        header.render("Title Example")

        title = Title()
        title.render("Title Example")

        st.divider()

        title.render("Another title Example")

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
