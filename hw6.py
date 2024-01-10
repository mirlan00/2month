import sqlite3

connect = sqlite3.connect('books.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    year  INTEGER
) ''')


def add_book(title, author, year):
    connect = sqlite3.connect('books.db')
    cursor = connect.cursor()
    cursor.execute('''
        INSERT INTO books (title, author, year) VALUES (?, ?, ?)
    ''', (title, author, year))
    connect.commit()

def update_books(book_id, title, author, year):
    connect = sqlite3.connect('books.db')
    cursor = connect.cursor()
    cursor.execute('''
        UPDATE books SET title=?, author=?, year=? WHERE id=?
    ''', (title, author, year, book_id))
    connect.commit()

def all_books():
    connect = sqlite3.connect('books.db')
    cursor = connect.cursor()
    cursor.execute('''SELECT * FROM books''')
    books = cursor.fetchall()
    connect.close()
    return books

def delete_books(title):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute('''
        DELETE FROM books
        WHERE title=?
    ''', (title,))
    connect.commit()
    connect.close()


class Books():
    def init(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")

def main():
    while True:
            print("1 - Добавить Книгу, 2 - Обновить информацию об книге , 3 - Посмотреть книгу , 4 - Удалить книгу , 5 - выйти ")

            commands = input("Выберите действие : ")

            if commands == '1':
                title = input("Название : ")
                author = input("Автор : ")
                year = int(input("Год выпуска: "))
                add_book(title, author, year)
                print("Книга добавлен ")
            
            elif commands == '2':
                book_id = int(input("Введите номер книги для обновления: "))
                title = input("Название книги: ")
                author = input("Автор книги: ")
                year = int(input("Год выпуска: "))
                update_books(book_id,title, author, year)
                print("Информация об книге обновлена")
                

            elif commands == '3':
                books = all_books()
                print("Список книг:")
                for book in books:
                    print(book)
            
            elif commands == '4':
                title = input("Введите название книги, которую нужно удалить: ")
                delete_books(title)
                print("Книга удалена.")
            
            
            elif commands == '5':

        
                break
            else:
                print("Незнакомая команда пожалуйста выберите действие")

main()
