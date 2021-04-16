import unittest

from sample_package import modules


class TestSampleModules(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('*** 全体前処理 ***')

    @classmethod
    def tearDownClass(cls):
        print('*** 全体後処理 ***')

    def setUp(self):
        print('+ テスト前処理')

    def tearDown(self):
        print('+ テスト後処理')

    def test_sample_function(self):
        """sample_package/utils/sample_modules/sample_function()のテスト
        """
        print('+ sample_functionをテストします')
        self.assertEqual("Hello sample function!!!", modules.sample_function())


if __name__ == '__main__':
    unittest.main()
