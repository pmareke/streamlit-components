import streamlit as st

from examples.component import Component


class Header(Component):
    def render(self, message: str) -> None:
        st.header(message)


if __name__ == "__main__":
    header = Header()
    header.render("any-header")
