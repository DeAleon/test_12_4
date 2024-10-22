import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

class TestRunner(unittest.TestCase):



    def test_walk(self):
        try:
            tw = Runner('Test1', speed=-2)
            for walk in range(10):
                tw.walk()

            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            tr = Runner(2)
            for run in range(10):
                tr.run()
            self.assertEqual(tr.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)





if __name__ == '__main__':
    unittest.main()

