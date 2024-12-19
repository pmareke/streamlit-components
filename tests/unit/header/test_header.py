from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestHeaderComponent:
    def test_header(self) -> None:
        app = AppTest.from_file("examples/header/main.py")

        at = app.run()

        expect(at.header[0].value).to(equal("any-header"))
