import streamlit as st

from src.button.main import Button
from src.component import Component
from src.header.main import Header
from src.link.main import Link
from src.tab.main import Tab


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Tab example")

    def render(self) -> None:
        header = Header()
        header.render("Tab Example")

        tab = Tab()
        button1 = Button(
            "Click button 1 !!!", callback=lambda: st.write("Button 1 clicked!!!")
        )
        tab.add("Button 1", button1)
        button2 = Button(
            "Click button 2 !!!", callback=lambda: st.write("Button 2 clicked!!!")
        )
        tab.add("Button 2", button2)
        tab.render()

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
