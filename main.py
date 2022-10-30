from website import create_app

app = create_app()

if __name__ == '__main__':      #if we run the main file
    app.run(debug = True)       #We run the application (runs the web server any time we make a change) - remove when in production

