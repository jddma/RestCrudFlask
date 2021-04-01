from  app import create_app

from app.crud import Crud

from flask import request, make_response

if __name__ == '__main__':
    app = create_app()

    #Instanciar el método de la clase crud encargada de realizar las operaciones sobre la BD
    crud = Crud()

    @app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def user():

        response = None
        #Identificar el método de la solicitud
        if request.method == 'GET':
            response = make_response(crud.read())
            response.headers['Content-Type'] = 'application/json'
            return response
        elif request.method == 'POST':
            response = make_response(crud.create(request.data.decode()))
            response.headers['Content-Type'] = 'application/json'
            return response
        elif request.method == 'PUT':
            response = make_response(crud.update(request.data.decode()))
            response.headers['Content-Type'] = 'application/json'
            return response
        elif request.method == 'DELETE':
            response = make_response(crud.delete(request.data.decode()))
            response.headers['Content-Type'] = 'application/json'
            return response

    app.run(debug=True)