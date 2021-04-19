import unittest

from package import utils


class TestSampleModules(unittest.TestCase):
    def test_sample_function(self):
        """package/utils/sample_modules/sample_function()のテスト
        """
        print('+ sample_functionをテストします')
        self.assertEqual("Hello sample function!!!", utils.sample_function())


if __name__ == '__main__':
    unittest.main()
