import serial
import time
import sqlite3
from threading import Timer
import MySQLdb

ser = serial.Serial('COM3', 9600)
aux=0
s=1
def execute(k):
    connection = MySQLdb.connect("192.168.0.15", "admin", "password", "scan_machine")

    cursor = connection.cursor()

    cursor.execute(k)

    connection.commit()

    connection.close()


def fetchone(k):
    connection = MySQLdb.connect("192.168.0.15", "admin", "password", "scan_machine")

    cursor = connection.cursor()

    cursor.execute(k)

    b = cursor.fetchone()

    connection.commit()

    connection.close()

    return b


def decodage():
    global a
    aux = ser.readline()
    a = ""
    k = []
    for s in aux:
        d=chr(s)
        k.append(d)
    #print(k)
    if (len(k)>8):
        for i in range (0, 8):
            f = k[i]

            a = "%s%s" % (a,f)
    print(str(a))


def lectureSerie():# fonction de lecture série

    if (ser.inWaiting()):
        decodage()
        global a
        if (a == '8b5b24a3'):
            ser.write(b'1/r/n')
            print("rfid envoyé")


    Timer(0.5, lectureSerie).start()


def testlaser():
    global a

    sql = "SELECT * FROM client WHERE rfid='"

    sql = "%s%s" % (sql, a)

    sql = "%s%s" % (sql, "'")

    #b = fetchone(sql)

    c = b[3]

    if ( c == 'autorisé'):
        #commande a mettre dans l'arduino
        pass

def testcnc():
    """global a

    sql = "SELECT * FROM client WHERE rfid='"

    sql = "%s%s" % (sql, a)

    sql = "%s%s" % (sql, "'")

    #b = fetchone(sql)

    #c = b[4]"""
    if(ser.inWaiting()):
        c = input("autorisé ou pas  ")

        if (c == 'autorisé'):

            print("ok")
            i = 'on'.strip()

            ser.write(b'1')

            time.sleep(2)

            print("sleep ok")

            print(ser.read().decode('ascii'))

        else :
            print("ok")
            i = 'on'.strip()

            ser.flushInput()

            ser.write(b'2/r/n')

            time.sleep(2)

            print("sleep ok2")

            ser_bytes = ser.readline()
            decoded_bytes = str(ser_bytes[6:len(ser_bytes)].decode("utf-8"))
            print(decoded_bytes)



def decodage():
    global a
    aux = ser.readline()
    a = ""
    k = []
    for s in aux:
        d=chr(s)
        k.append(d)
    #print(k)
    if (len(k)>8):
        for i in range (0, 8):
            f = k[i]

            a = "%s%s" % (a,f)
    """print(str(a))
    print(aux)"""
    return a



def lectureSerie():# fonction de lecture série

    if (ser.inWaiting()):

        aux3 = decodage()
        if ( aux3 == '8b5b24a3'):
            print('ouaaah')
            ser.write(b'2/r/n')
            time.sleep(0.1)
            print(ser.readline().decode('ascii'))

        #print(aux)
        time.sleep(1)
        if (aux3 == '66def329'):
            print('chocapic')
            ser.write(b'1/r/n')
            time.sleep(0.1)
            print(ser.readline().decode('ascii'))


    Timer(0.5, lectureSerie).start()

if __name__ == "__main__":
    lectureSerie()