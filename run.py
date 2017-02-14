from app import create_app
import os



config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

@app.route('/')
def index():
	return "hi"



if __name__ == '__main__':
	app.run(debug=True)

