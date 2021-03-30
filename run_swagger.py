import connexion
import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('./sources/config.ini')
    host = config['swagger_server']['host']
    port = config['swagger_server']['port']
    app = connexion.FlaskApp(__name__, host=host, port=int(port), specification_dir='sources/')
    app.add_api('../sources/swagger.yaml', arguments={'title': 'Server Song Swagger'})
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Swagger is waiting for you at: http://' + str(host) + ':' + str(port) + '/ui')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    app.run()
