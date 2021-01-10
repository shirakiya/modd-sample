import unittest

from main import get_message


class TestMain(unittest.TestCase):

    def test_get_message(self):
        params = [
            0,
            1
        ]
        wants = [
            'count: 0',
            'count: 1',
        ]
        for param, want in zip(params, wants):
            god = get_message(param)
            self.assertEqual(god, want)


if __name__ == '__main__':
    unittest.main()
