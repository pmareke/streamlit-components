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

        class DividerPage(Component):
            def render(self) -> None:
                button = Button(
                    "Click me!!!", callback=lambda: st.write("Button clicked!!!")
                )
                button.render()
                Divider.render()
                button = Button(
                    "Click me too!!!", callback=lambda: st.write("Button clicked!!!")
                )
                button.render()

        divider_page = DividerPage()
        tab.add("Button", divider_page)
        lines = [
            'button = Button("Click me!!!", callback=lambda: st.write("Button clicked!!!"))',
            "Divider.render()",
            'button = Button("Click me too!!!", callback=lambda: st.write("Button clicked!!!"))',
        ]
        content = "\n".join(lines)
        code = Code(language="python", content=content)
        tab.add("Source code", code)
        tab.render()

        Divider.render()

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
