import unittest
import teast_12_3

# Описание объекта TestSuite
suite = unittest.TestSuite()

# Добавление тестов в TestSuit
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(teast_12_3.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(teast_12_3.TournamentTest))

# Создание объекта TextTestRunner
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)

# Запуск TestSuite
result = runner.run(suite)
