import streamlit as st

from src.component import Component


class Title(Component):
    def __init__(self, message: str) -> None:
        self.message = message

    def render(self) -> None:
        st.title(self.message)


if __name__ == "__main__":
    title = Title("any-title")
    title.render()
