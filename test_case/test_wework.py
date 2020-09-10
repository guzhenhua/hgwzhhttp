from api.wework import WeWork


class TestWeWork():
    def test_wework(self):
        print(WeWork().get_token())