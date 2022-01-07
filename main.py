'''
Moonboard website app Moonlitsonata
Oscar Hendrick

This app builds has a website that allows
user login to create/edit/submit climb routes
per Barbara's moonboard specification
'''
from website import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)