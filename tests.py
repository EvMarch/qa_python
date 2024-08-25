from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # Тестирование добавления книги с длинным названием
    def test_add_new_book_with_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('A' * 41)
        assert collector.get_books_genre() == {}


# Тестирование установки жанра книги
    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

# Тестирование установки жанра книги с неверным жанром
    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Толковый словарь')
        collector.set_book_genre('Толковый словарь', 'Словарь')
        assert collector.get_book_genre('Толковый словарь') == ''


# Тестирование получения книг по жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Кэрри')
        collector.set_book_genre('Кэрри', 'Ужасы')
        collector.add_new_book('Сумерки')
        collector.set_book_genre('Сумерки', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Кэрри']

# Тестирование получения книг для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Чебурашка')
        collector.set_book_genre('Чебурашка', 'Мультфильмы')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_books_for_children() == ['Чебурашка']

# Тестирование добавления книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Анекдоты')
        collector.set_book_genre('Анекдоты', 'Комедии')
        collector.add_book_in_favorites('Анекдоты')
        assert collector.get_list_of_favorites_books() == ['Анекдоты']

# Тестирование удаления книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Фантастика')
        collector.add_book_in_favorites('Пикник на обочине')
        collector.delete_book_from_favorites('Пикник на обочине')
        assert collector.get_list_of_favorites_books() == []

# Параметризация тестов для установки жанра
    @pytest.mark.parametrize("book_name, genre, expected_genre", [
        ("10 негритят", "Детективы", "Детективы"),
        ("Солярис", "Фантастика", "Фантастика")
    ])
    def test_set_book_genre_parametrized(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    # Параметризация тестов для добавления и удаления книг в/из избранного
    @pytest.mark.parametrize("book_name", [
        "1984",
        "Трудно быть богом"
    ])
    def test_add_and_remove_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "Фантастика")
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    # Тестирование книги с пустым жанром
    def test_book_with_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        assert collector.get_book_genre('Колобок') == ''