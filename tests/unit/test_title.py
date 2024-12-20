from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestTitleComponent:
    def test_title(self) -> None:
        app = AppTest.from_file("src/title/main.py")

        at = app.run()

        expect(at.title[0].value).to(equal("any-title"))
