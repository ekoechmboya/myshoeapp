import sqlite3

connection = sqlite3.connect("database.db")
with open('schema.sql') as a:
    connection.executescript(a.read())
cursor = connection.cursor()
cursor.execute("INSERT INTO shoes (name, image, price) VALUES (?, ?,?)",
               ("airforce", "https://www.kilimall.co.ke/new/goods/17960037", "10000$"))
cursor.execute("INSERT INTO shoes (name,image, price) VALUES (?, ?, ?)", ('puma',
                                                                          "https://www.google.com/imgres?imgurl=https%3A%2F%2Fke.jumia.is%2Funsafe%2Ffit-in%2F500x500%2Ffilters%3Afill(white)%2Fproduct%2F76%2F766045%2F1.jpg%3F1747&imgrefurl=https%3A%2F%2Fwww.jumia.co.ke%2Ffashion-women-shoes-ladies-shoes-for-women-shoe-54066767.html&tbnid=Jy4NVS_eVh5SuM&vet=12ahUKEwjfvLHD6Lf9AhVKnCcCHRDdBrcQMygCegUIARCQAw..i&docid=PhnzW5MHTooRzM&w=500&h=500&q=shoes%20on%20fashion%20images&ved=2ahUKEwjfvLHD6Lf9AhVKnCcCHRDdBrcQMygCegUIARCQAw",
                                                                          "500$"))
connection.commit()
connection.close()
