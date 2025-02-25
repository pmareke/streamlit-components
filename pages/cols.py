import streamlit as st

from src.code.main import Code
from src.cols.main import Cols
from src.component import Component
from src.divider.main import Divider
from src.header.main import Header
from src.link.main import Link
from src.tab.main import Tab
from src.title.main import Title


class ColsPage(Component):
    def __init__(self) -> None:
        st.set_page_config("Cols example")

    def render(self) -> None:
        header = Header("Cols Example")
        header.render()

        divider = Divider()
        tab = Tab()
        cols = Cols()
        title = Title("Title 1")
        cols.add(title)
        another_title = Title("Title 2")
        cols.add(another_title)
        extra_title = Title("Title 3")
        cols.add(extra_title)

        tab.add("Cols", cols)
        lines = [
            "cols = Cols()",
            "\n",
            'title = Title("Title 1")',
            "cols.add(title)",
            "\n",
            'another_title = Title("Title 2")',
            "cols.add(another_title)",
            "\n",
            'extra_title = Title("Title 3")',
            "cols.add(extra_title)",
            "\n",
            "cols.add(extra_title)",
        ]
        content = "\n".join(lines)
        code = Code(
            language="python",
            content=content,
        )
        tab.add("Source code", code)
        tab.render()

        divider.render()

        Link.go_home()


if __name__ == "__main__":
    page = ColsPage()
    page.render()
