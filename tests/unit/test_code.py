from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestCodeComponent:
    def test_code(self) -> None:
        app = AppTest.from_file("src/code/main.py")

        at = app.run()

        source_code = (
            'Button("Click me!!!", callback=lambda: st.write("Button clicked!!!"))'
        )
        expect(at.code[0].value).to(equal(source_code))
