import os

deleted = False

print("Удаление всех файлов сессий..")
for file in os.listdir():
    if file.endswith(".session") or file.endswith(".session-journal"):
        os.remove(file)
        print("Удалён файл: " + file)
        deleted = True
else:
    if not deleted:
        print("Нет файлов для удаления!")
