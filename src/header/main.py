import streamlit as st

from src.component import Component


class Header(Component):
    def __init__(self, message: str) -> None:
        self.message = message

    def render(self) -> None:
        st.header(self.message)


if __name__ == "__main__":
    header = Header("any-header")
    header.render()
