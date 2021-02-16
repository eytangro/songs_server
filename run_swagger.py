import connexion
import configparser

# app = connexion.FlaskApp(__name__)
# app.add_api('./sources/swagger.yaml')
# app.run(host='127.0.0.1', port=8080)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('./sources/config.ini')
    host = config['server']['host']
    port = config['server']['port']
    app = connexion.FlaskApp(__name__,host = host, port=int(port), specification_dir='openapi/')
    app.add_api('../sources/swagger.yaml', arguments={'title': 'Server Song Swagger'})
    app.run()