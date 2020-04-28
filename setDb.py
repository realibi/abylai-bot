import sqlite3

conn = sqlite3.connect('patientsDB.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE patients (passport_num, full_name, birth_date, diagnosis)''')

cursor.execute('''INSERT INTO patients VALUES ('043690818', 'Сахипова Гульжиян', '16.12.2001', 'Алкаш (хронический)')''')
cursor.execute('''INSERT INTO patients VALUES ('043698773', 'Жумабекова Салтанат', '06.11.2002', 'Қолтық иісі')''')
cursor.execute('''INSERT INTO patients VALUES ('045197962', 'Кубентаева Асем', '09.09.2002', 'Екі қабат')''')
cursor.execute('''INSERT INTO patients VALUES ('042998889', 'Кеңес Тілеуғазы', '27.04.2002', 'Туылганнан сондай')''')
cursor.execute('''INSERT INTO patients VALUES ('043690884', 'Мырзадәулет Меруерт', '09.09.2002', 'COVID-19')''')

conn.commit()
conn.close()