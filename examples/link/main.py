import streamlit as st
from src.domain.component import Component


class Link(Component):
    @staticmethod
    def render(url: str, label: str) -> None:
        st.html(f"""
                    <a href='{url}' target='_self'>
                        <h2>{label}</h1>
                    </a>
                """)


if __name__ == "__main__":
    link = Link()
    link.render("any-url", "any-label")
