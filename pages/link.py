import streamlit as st

from src.code.main import Code
from src.component import Component
from src.divider.main import Divider
from src.header.main import Header
from src.link.main import Link
from src.tab.main import Tab


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Link example")

    def render(self) -> None:
        header = Header("Link Example")
        header.render()

        tab = Tab()
        link = Link(
            "https://github.com/pmareke/streamlit-components",
            "Streamlit Components repo",
        )
        tab.add("Link", link)
        code = Code(
            language="python",
            content='Link(\n"https://github.com/pmareke/streamlit-components",\n"Streamlit Components repo"\n)',
        )
        tab.add("Source code", code)
        tab.render()

        Divider.render()

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
