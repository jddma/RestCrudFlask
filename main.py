from  app import create_app

from app.crud import Crud

from flask import render_template

if __name__ == '__main__':
    app = create_app()

    crud = Crud()

    @app.route('/')
    def index():
        data = crud.read()
        return render_template('index.html', data=data)

    app.run(debug=True)