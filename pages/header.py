import streamlit as st

from examples.component import Component
from examples.header.main import Header
from examples.link.main import Link


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Header example")

    def render(self) -> None:
        header = Header()
        header.render("Header Example")

        st.divider()

        header.render("Another Header Example")

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
