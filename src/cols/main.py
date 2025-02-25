import streamlit as st

from src.component import Component


class Cols(Component):
    def __init__(self) -> None:
        self.cols: list[Component] = []

    def add(self, component: Component) -> None:
        self.cols.append(component)

    def render(self) -> None:
        cols = st.columns(len(self.cols))

        for col in range(len(self.cols)):
            with cols[col]:
                self.cols[col].render()
