import streamlit as st

from examples.button.main import Button
from examples.component import Component
from examples.header.main import Header
from examples.link.main import Link


class Page(Component):
    def __init__(self) -> None:
        st.set_page_config("Button example")

    def render(self) -> None:
        header = Header()
        header.render("Button Example")

        button = Button("Click me!!!", callback=lambda: st.write("Button clicked!!!"))

        button.render()

        Link.go_home()


if __name__ == "__main__":
    page = Page()
    page.render()
