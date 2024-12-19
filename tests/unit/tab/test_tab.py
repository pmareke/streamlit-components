from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestTabComponent:
    def test_tab(self) -> None:
        app = AppTest.from_file("examples/tab/main.py")

        at = app.run()

        expect(at.text[0].value).to(equal("any-text"))
        expect(at.tabs[0].label).to(equal("Dummy tab"))
