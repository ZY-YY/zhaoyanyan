#TestRunner执行所有入口的文件
import unittest

test_dir="./"  #当前路径
suite=unittest.TestLoader().discover(test_dir,pattern='test*.py')
#通过TestLoader()来进行批量测试用例的进行,discover可以找到符合后面的要求的所有文件（以test开头*就是后面什么都可以，后缀是.py的所有文件）


#对于每一个.py文件都hi有一个因长的属性名字就是__name__
if __name__=='__main__': #这句话的含义就是当.py模块在执行的时候要用unittest.TestTestRunner的这个对象来运行代码
    #加上这句话就能在控制台CMD执行
    #执行用例
    runner=unittest.TextTestRunner()
    runner.run(suite)# runner.run 这个方法就可以来执行一个测试用例的集合 suite是集合名字
