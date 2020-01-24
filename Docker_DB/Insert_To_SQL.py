import os 
import mysql.connector as mysql

wav_files = os.listdir("/Users/johnminhdo/Desktop/Bird-Box/Cardinal Calls")
wav_files = sorted(wav_files)


def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData= file.read()
    return binaryData


def insertBLOB(name, audio):
    db = mysql.connect(
        host = "localhost",
        user = "root",
        password = "seniorcapstone",
        auth_plugin="mysql_native_password",
        database = "birds"
    )

    cursor = db.cursor()

    query = "INSERT INTO bird_audio (name, audio) VALUES (%s, %s)"
    

    audio_file = convertToBinaryData(audio)


    insert_blob_tuple = (name, audio_file)

    result = cursor.execute(query, insert_blob_tuple)

    db.commit()

    print("It is completed!")


# for files in wav_files:
#     print(files)
#     insertBLOB("cardinal" + files[14:18] , "/Users/johnminhdo/Desktop/Bird-Box/Cardinal Calls/" + files)


insertBLOB("cardinal", "/Users/johnminhdo/Downloads/cardinal.mp3")


