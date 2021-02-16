import connexion

# app = connexion.FlaskApp(__name__)
# app.add_api('./sources/swagger.yaml')
# app.run(host='127.0.0.1', port=8080)

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='openapi/')
    app.add_api('../sources/swagger.yaml', arguments={'title': 'Server Song Swagger'})
    app.run()