import streamlit as st

from examples.component import Component


class Link(Component):
    @staticmethod
    def render(url: str, label: str) -> None:
        st.html(f"""
                    <a href='{url}' target='_self'>
                        <h2>{label}</h1>
                    </a>
                """)

    @staticmethod
    def go_home() -> None:
        st.html("""
                <style>
                    .st-emotion-cache {
                        display: inline-flex;
                        -webkit-box-align: center;
                        align-items: center;
                        -webkit-box-pack: center;
                        justify-content: center;
                        font-weight: 400;
                        padding: 0.5rem;
                        border-radius: 0.5rem;
                        min-height: 2.5rem;
                        margin: 0px;
                        line-height: 1.6;
                        color: inherit;
                        width: auto;
                        cursor: pointer;
                        user-select: none;
                        background-color: rgb(255, 255, 255);
                        border: 1px solid rgba(49, 51, 63, 0.2);
                    }
                </style>
                <a href='/' target='_self'>
                    <button kind="secondaryFormSubmit" class="st-emotion-cache">
                        🏠 Go Home
                    </button>
                </a>
            """)


if __name__ == "__main__":
    link = Link()
    link.render("any-url", "any-label")
