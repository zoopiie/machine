import MySQLdb


def fetchone(k):
    connection = MySQLdb.connect("192.168.0.15", "admin", "fablab70300", "scan_machine")
    cursor = connection.cursor()
    cursor.execute(k)
    b = cursor.fetchone()
    connection.commit()
    connection.close()
    return b


def execute(k):
    connection = MySQLdb.connect("192.168.0.15", "admin", "fablab70300", "scan_machine")
    cursor = connection.cursor()
    cursor.execute(k)
    connection.commit()
    connection.close()


def fetchall(k):
    connection = MySQLdb.connect("192.168.0.15", "admin", "fablab70300", "scan_machine")
    cursor = connection.cursor()
    cursor.execute(k)
    b = cursor.fetchall()
    connection.commit()
    connection.close()
    return b
