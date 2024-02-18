class Library:
  def __init__(self):
      self.file_path = "books.txt"
      self.file = open(self.file_path, "a+")

  def __del__(self):
      self.file.close()

  def list_books(self):
      self.file.seek(0)
      lines = self.file.read().splitlines()
      for line in lines:
          book_info = line.split(',')
          print(f"Book: {book_info[0]}, Author: {book_info[1]}")

  def add_book(self):
      title = input("Enter book title: ")
      author = input("Enter book author: ")
      release_year = input("Enter release year: ")
      num_pages = input("Enter number of pages: ")

      book_info = f"{title},{author},{release_year},{num_pages}\n"
      self.file.write(book_info)
      print(f"\nBook '{title}' added!")

  def remove_book(self):
      title_to_remove = input("Enter the book title: ")

      self.file.seek(0)
      lines = self.file.read().splitlines()
      updated_books = [line for line in lines if title_to_remove not in line]

      self.file.seek(0)
      self.file.truncate()
      self.file.write('\n'.join(updated_books))

      print(f"\nBook '{title_to_remove}' removed!")

lib = Library()

while True:
  print("***********************")
  print("WELCOME TO LIBRARY")
  print("***********************")
  print("\n MENU ")
  print("1) List Books")
  print("2) Add Book")
  print("3) Remove Book")
  print("4) Quit")

  choice = input("\nEnter your choice (1-4): ")

  if choice == "1":
      lib.list_books()
  elif choice == "2":
      lib.add_book()
  elif choice == "3":
      lib.remove_book()
  elif choice == "4":
      print("\nQuit the Library System!")
      break
  else:
      print("\nInvalid choice! Try again (1-4) ")

