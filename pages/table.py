import pandas as pd
import streamlit as st
from pandas import DataFrame

from src.button.main import Button
from src.component import Component
from src.header.main import Header
from src.link.main import Link
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
        header = Header()
        header.render("Table Example")

        button = Button("Fill table", lambda: self._get_data())
        button.render()

        table = Table()
        table.render(self.data)

        Link.go_home()

    def _get_data(self) -> None:
        self.data = self.repository.data()


if __name__ == "__main__":
    dummy_repository = DummyRepository()
    page = Page(dummy_repository)
    page.render()
