import streamlit as st

from src.component import Component
from src.header.main import Header
from src.link.main import Link


class App(Component):
    def render(self) -> None:
        st.set_page_config("Examples")

        header = Header()
        header.render("Streamlit Components")

        st.divider()

        Link.render("/header", "Header")
        Link.render("/title", "Title")
        Link.render("/button", "Button")
        Link.render("/link", "Link")
        Link.render("/form", "Form")
        Link.render("/tab", "Tab")


if __name__ == "__main__":
    app = App()
    app.render()
