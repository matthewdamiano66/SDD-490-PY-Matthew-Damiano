import sqlite3
from sqlite3 import Error
import dataBaseStuff
test_api_data_entry = [{"id": "this is test data", "rank": "19992", "title": "Comp490 Project 1 Show",
                        "fullTitle": "Comp490 Project 1(2022)", "year": "2022", "image": "",
                        "crew": "A lot of people who exist", "imDbRating": "8.8",
                        "imDbRatingCount": "50"}]
def test_enter_data():
    test_data_entry = [("this is test data", 19992, "Comp490", "Comp490 Project 1 (2022)", 2022,
                        "", "This is a test for crew", 8.8, 50)]
    connection, db_cursor = dataBaseStuff.open_db("testDatabase.sqlite")
    dataBaseStuff.create_top250_table(db_cursor)
    dataBaseStuff.put_top_250_in_database(test_data_entry, db_cursor)
    connection.commit()
    db_cursor.execute("SELECT COUNT() FROM top_show_data WHERE ttid = 'tttestdata'")
    record_count_set = db_cursor.fetchone()
    number_of_records = record_count_set[0]
    assert number_of_records == 1
    db_cursor.execute("SELECT * FROM top_show_data WHERE ttid = 'tttestdata'")
    record_set = db_cursor.fetchall()
    assert record_set[0] == test_data_entry[0]
    def sql_connection():
        try:
            con = sqlite3.connect('project1db.sqlite')
            print("Houston we have lift off ")
        except Error:
            print(Error)
        finally:
            con.close()
    sql_connection()
