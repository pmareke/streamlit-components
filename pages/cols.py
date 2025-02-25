import streamlit as st

from src.cols.main import Cols
from src.component import Component
from src.header.main import Header
from src.link.main import Link
from src.title.main import Title


class ColsPage(Component):
    def __init__(self) -> None:
        st.set_page_config("Cols example")

    def render(self) -> None:
        header = Header("Cols Example")
        header.render()

        cols = Cols()
        title = Title("Title 1")
        cols.add(title)
        another_title = Title("Title 2")
        cols.add(another_title)
        extra_title = Title("Title 3")
        cols.add(extra_title)
        cols.render()

        Link.go_home()


if __name__ == "__main__":
    page = ColsPage()
    page.render()
