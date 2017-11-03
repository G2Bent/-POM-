import os,HTMLTestRunner,unittest,time
import sys
def create_suite():
    TestSuite = unittest.TestSuite()#测试集
    test_dir = os.getcwd()+'\\TestCase\\'
    # print(test_dir)

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='test.py',
        top_level_dir=None
    )

    # print (discover)

    for test_case  in discover:
        TestSuite.addTests(test_case)
    return TestSuite

def report():
    if len(sys.argv) > 1:
        report_name = os.getcwd() + '\\report\\' + sys.argv[1] + '_result.html'
    else:
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        report_name = os.getcwd()+'\\report\\result.html'
    return report_name

fp = open(report(),'wb')
Runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='测试用例执行情况'
        )

if __name__ == '__main__':
    TestSuite = create_suite()
    Runner.run(TestSuite)
    fp.close()