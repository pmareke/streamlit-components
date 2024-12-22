import streamlit as st

from src.component import Component


class Divider(Component):
    @staticmethod
    def render() -> None:
        st.divider()
