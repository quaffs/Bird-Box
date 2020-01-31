import mysql.connector as mysql

def write_file(data, filename):
    with open(filename, 'wb') as file:
        audio_file = file.write(data)
    return audio_file

def readBLOB(name, audio):
  
    db = mysql.connect(
        host = "localhost",
        user = "root",
        password = "seniorcapstone",
        auth_plugin="mysql_native_password",
        database = "birds",
        use_pure=True
    )

    cursor = db.cursor()

    query = "select audio from bird_audio where name = %s"


    cursor.execute(query, (name,))

    record = cursor.fetchall()

    for row in record:
        audio_file = row[0]
        write_file(audio_file, audio)

    print("It is completed!")

readBLOB("cardinal", "/Users/johnminhdo/Desktop/cardinal.mp3")
