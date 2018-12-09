
import unittest
import sys

# print(type(sys.version_info))
# print(sys.version_info)
# print(sys.version_info[3])
class MyFirstUnit(unittest.TestCase):
    mylst = [1, 2, 3]


    # @unittest.skip("just want to skip this case")
    def test_case_1(self):
        self.assertEqual("a", "a", "they are not equal.")  # assert 断言
        print("11111")

    # @unittest.skipIf(sys.version_info[3]!="not final","not a final version")
    def test_case_num(self):
        self.assertEqual("a", "a", "they are not equal.")  # assert 断言
        print("22222")

    # @unittest.skipUnless(sys.platform.startswith("Linux"),"Need to be Windows OS")
    def test_case_list(self):
        self.assertListEqual([1, 2, 3], self.mylst, "they are not equal.")
        print("333333")


def mysuite():
    suite=unittest.TestSuite()
    suite.addTest(MyFirstUnit("test_case_1"))
    # suite.addTest(MyFirstUnit("test_case_num"))
    suite.addTest(MyFirstUnit("test_case_list"))
    suite.addTest(Baiducase("test_case_1"))
    return suite


# if __name__=="__main__":##判断程序是不是单独执行 而不是被引用执行的
#     unittest.main()


if __name__ == "__main__":
    # unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(mysuite())