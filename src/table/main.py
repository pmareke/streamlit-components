import pandas as pd
import streamlit as st
from pandas import DataFrame

from src.component import Component


class Table(Component):
    def render(self, data: DataFrame | None) -> None:
        st.table(data)


if __name__ == "__main__":
    table = Table()
    data = pd.DataFrame({"foo": ["bar"]})
    table.render(data)
