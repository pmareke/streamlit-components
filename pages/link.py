import streamlit as st

from src.component import Component
from src.header.main import Header
from src.link.main import Link


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Link example")

    def render(self) -> None:
        header = Header()
        header.render("Link Example")

        Link.render(
            "https://github.com/pmareke/streamlit-components",
            "Streamlit Components repo",
        )
        Link.render("www.google.com", "Google")

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
