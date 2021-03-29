import logging

import pymysql.cursors

import os

import sys

import json

class Crud():

    def open_connection(self):
        try:
            self.__connection = pymysql.connect(
                host=os.environ["MY_HOST"],
                user=os.environ["MY_USER"],
                password=os.environ["MY_PASSWORD"],
                db="tenis_db",
                cursorclass=pymysql.cursors.DictCursor
            )
            pass
        except KeyError:
            logging.fatal('Error al obtener las credenciales de la base de datos')
            sys.exit()

    def close_connection(self):
        self.__connection.close()

    def read(self):
        self.open_connection()

        cursor = self.__connection.cursor()
        sql = 'SELECT id, user FROM user'
        cursor.execute(sql)
        data = []
        for i in cursor:
            data.append(i)

        self.close_connection()

        return data