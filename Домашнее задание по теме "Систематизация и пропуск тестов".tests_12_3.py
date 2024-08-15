import unittest

# Декоратор для пропуска тестов
def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            unittest.skip("Тесты в этом кейсе заморожены")(func)(self, *args, **kwargs)
        else:
            return func(self, *args, **kwargs)
    return wrapper

# Класс RunnerTest
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        # Тест 1
        pass

    @skip_if_frozen
    def test_run(self):
        # Тест 2
        pass

    @skip_if_frozen
    def test_walk(self):
        # Тест 3
        pass

# Класс TournamentTest
class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        # Тест 1
        pass

    @skip_if_frozen
    def test_second_tournament(self):
        # Тест 2
        pass

    @skip_if_frozen
    def test_third_tournament(self):
        # Тест 3
        pass

# Описание объекта TestSuite
suite = unittest.TestSuite()

# Добавление тестов в TestSuit
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

