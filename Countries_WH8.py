import sqlite3

def get_connection():
    conn = sqlite3.connect('Countries_WH8.db')
    return conn

def get_students_by_city_id(city_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.first_name, s.last_name, c.title, c.area, co.title 
        FROM students s 
        JOIN cities c ON s.city_id = c.id 
        JOIN countries co ON c.country_id = co.id 
        WHERE c.id = ?
    """, (city_id,))
    students = cursor.fetchall()
    conn.close()
    return students

def get_cities():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    conn.close()
    return cities

def main():
    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    cities = get_cities()
    for city in cities:
        print(f"{city[0]}: {city[1]}")
    city_id = int(input("Введите номер города: "))
    if city_id != 0:
        students = get_students_by_city_id(city_id)
        for student in students:
            print(f"Имя: {student[0]}, Фамилия: {student[1]}, Город: {student[2]}, Площадь города: {student[3]}, Страна: {student[4]}")

if __name__ == "__main__":
    main()