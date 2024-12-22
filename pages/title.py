import streamlit as st

from src.code.main import Code
from src.component import Component
from src.header.main import Header
from src.link.main import Link
from src.tab.main import Tab
from src.title.main import Title


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Title example")

    def render(self) -> None:
        header = Header("Title Example")
        header.render()

        tab = Tab()
        title = Title("Title Example")
        tab.add("Title", title)
        code = Code(language="python", content='Title("Title Example")')
        tab.add("Source code", code)
        tab.render()

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
