import logging

import pymysql.cursors

import os

import sys

import json

class Crud():

    def __open_connection(self):
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

    def __close_connection(self):
        self.__connection.close()

    #Método para obtener los registros de la BD
    def read(self):
        self.__open_connection()

        cursor = self.__connection.cursor()
        sql = 'SELECT id, user FROM user'
        cursor.execute(sql)
        data = []
        for i in cursor:
            data.append(i)
        cursor.close()

        self.__close_connection()

        return json.dumps(data)

    def create(self, data: str):
        data_dic = json.loads(data)

        self.__open_connection()

        cursor = self.__connection.cursor()
        sql = 'INSERT INTO user (user, password) VALUES (%s, %s)'
        cursor.execute(sql, (data_dic['user'], data_dic['password']))
        cursor.close()

        self.__connection.commit()
        self.__close_connection()

        response = {"status": "ok"}
        return json.dumps(response)

    def update(self, data: str):
        data_dic = json.loads(data)

        self.__open_connection()

        cursor = self.__connection.cursor()
        sql = "UPDATE user SET user = %s, password = %s WHERE id = %s"
        cursor.execute(sql, (data_dic['user'], data_dic['password'], data_dic['id']))
        cursor.close()

        self.__connection.commit()
        self.__close_connection()

        response = {"status": "ok"}
        return json.dumps(response)

    def delete(self, data: str):
        data_dic = json.loads(data)

        self.__open_connection()

        cursor = self.__connection.cursor()
        sql = 'DELETE FROM user WHERE id = %s'
        cursor.execute(sql, (data_dic['id']))
        cursor.close()

        self.__connection.commit()
        self.__close_connection()

        response = {"status": "ok"}
        return json.dumps(response)