import streamlit as st

from src.component import Component
from src.header.main import Header
from src.link.main import Link


class App(Component):
    def render(self) -> None:
        st.set_page_config("Examples")

        header = Header("Streamlit Components")
        header.render()

        st.divider()

        header_page_link = Link("/header", "Header")
        header_page_link.render()

        divider_page_link = Link("/divider", "Divider")
        divider_page_link.render()

        title_page_link = Link("/title", "Title")
        title_page_link.render()

        button_page_link = Link("/button", "Button")
        button_page_link.render()

        link_page_link = Link("/link", "Link")
        link_page_link.render()

        form_page_link = Link("/form", "Form")
        form_page_link.render()

        tab_page_link = Link("/tab", "Tab")
        tab_page_link.render()

        table_page_link = Link("/table", "Table")
        table_page_link.render()

        code_page_link = Link("/code", "Code")
        code_page_link.render()


if __name__ == "__main__":
    app = App()
    app.render()
