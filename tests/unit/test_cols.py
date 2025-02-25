from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestCols:
    def test_cols(self) -> None:
        def create_app() -> None:
            from src.cols.main import Cols
            from src.header.main import Header

            header = Header("Header")
            another_header = Header("Another Header")
            internal_app = Cols()

            internal_app.add(header)
            internal_app.add(another_header)

            internal_app.render()

        app = AppTest.from_function(create_app)

        at = app.run()

        expect(at.header[0].value).to(equal("Header"))
        expect(at.header[1].value).to(equal("Another Header"))
