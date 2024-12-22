import streamlit as st

from src.code.main import Code
from src.component import Component
from src.header.main import Header
from src.link.main import Link
from src.tab.main import Tab


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Header example")

    def render(self) -> None:
        header = Header("Header Example")
        header.render()

        tab = Tab()
        header = Header("Header Example")
        tab.add("Header", header)
        code = Code(language="python", content='Header("Header Example")')
        tab.add("Source code", code)
        tab.render()

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
