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
        st.set_page_config("Tab example")

    def render(self) -> None:
        header = Header("Tab Example")
        header.render()

        tab = Tab()
        button1 = Button(
            "Click button 1 !!!", callback=lambda: st.write("Button 1 clicked!!!")
        )
        tab.add("Button 1", button1)
        lines = [
            "tab = Tab()",
            'button1 = Button(\n  "Click button 1 !!!",\n  callback=lambda: st.write("Button 1 clicked!!!")\n)',
            'tab.add("Button 1", button1)',
            "tab.render()",
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
