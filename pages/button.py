import streamlit as st

from src.button.main import Button
from src.code.main import Code
from src.component import Component
from src.divider.main import Divider
from src.header.main import Header
from src.link.main import Link
from src.tab.main import Tab


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Button example")

    def render(self) -> None:
        header = Header("Button Example")
        header.render()

        tab = Tab()
        button = Button("Click me!!!", callback=lambda: st.write("Button clicked!!!"))
        tab.add("Button", button)
        code = Code(
            language="python",
            content='Button("Click me!!!", callback=lambda: st.write("Button clicked!!!"))',
        )
        tab.add("Source code", code)
        tab.render()

        Divider.render()

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
