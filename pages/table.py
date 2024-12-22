import pandas as pd
import streamlit as st
from pandas import DataFrame

from src.button.main import Button
from src.code.main import Code
from src.component import Component
from src.divider.main import Divider
from src.header.main import Header
from src.link.main import Link
from src.tab.main import Tab
from src.table.main import Table


class DummyRepository:
    def data(self) -> DataFrame:
        data = {"col 1": [1, 2], "col 2": [3, 4]}
        return pd.DataFrame(data)


class Page(Component):
    def __init__(self, repository: DummyRepository) -> None:
        st.set_page_config("Table example")
        self.repository = repository
        self.data = None

    def render(self) -> None:
        header = Header("Table Example")
        header.render()

        tab = Tab()

        class TablePage(Component):
            def __init__(self, repository: DummyRepository) -> None:
                self.repository = repository
                self.data = None

            def render(self) -> None:
                button = Button("Get data", lambda: self._get_data())
                button.render()
                table = Table()
                table.render(pd.DataFrame(self.data))

            def _get_data(self) -> None:
                self.data = self.repository.data()

        table_page = TablePage(self.repository)
        tab.add("Table", table_page)
        lines = [
            "data = None",
            "",
            "def get_data(self) -> None:\n  data = self.repository.data()",
            "",
            'button = Button("Get data", lambda: get_data())',
            "button.render()",
            "table = Table()",
            "table.render(pd.DataFrame(data))",
        ]
        content = "\n".join(lines)
        code = Code(language="python", content=content)
        tab.add("Source code", code)
        tab.render()

        Divider.render()

        Link.go_home()

    def _get_data(self) -> None:
        self.data = self.repository.data()


if __name__ == "__main__":
    dummy_repository = DummyRepository()
    page = Page(dummy_repository)
    page.render()
