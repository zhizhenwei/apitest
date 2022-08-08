# @Time    : 2021/10/20 09:21
# @Author  : Evan.zhi
# @File    : conftest.py
# @Software: PyCharm


import pytest,warnings
from loguru import logger


#class级别fixture
@pytest.fixture(scope='class')
def setup_teardown_class():
    warnings.filterwarnings("ignore")
    logger.info(f'-----------------开始执行用例----------------')
    yield
    logger.info(f'-----------------用例执行结束----------------')