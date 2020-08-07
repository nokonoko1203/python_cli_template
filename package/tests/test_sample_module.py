import unittest

from package.sample_module import sample_function

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
        """/modules/sample_module/sample_functionのテスト
        """
        self.assertEqual("Hello sample function!!!", sample_function())


if __name__ == '__main__':
    unittest.main()
