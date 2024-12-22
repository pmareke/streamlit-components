import streamlit as st

from src.code.main import Code
from src.component import Component
from src.divider.main import Divider
from src.header.main import Header
from src.link.main import Link
from src.tab.main import Tab


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Code example")

    def render(self) -> None:
        header = Header("Code Example")
        header.render()

        tab = Tab()
        code = Code(language="python", content="print('Hello, World!')")
        tab.add("Code", code)
        code = Code(
            language="python",
            content='Code(language="python", content="print(\'Hello, World!\')")',
        )
        tab.add("Source code", code)

        tab.render()

        Divider.render()

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
