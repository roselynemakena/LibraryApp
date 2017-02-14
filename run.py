from app import create_app
import os



config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

@app.route('/')
def index():
# 	name = app.config['MAKENA']
# 	conn = mysql.connect()
# 	cur = conn.cursor()

# 	cur.execute("select * from users")
# 	data = cur.fetchall()
	return "hi"



if __name__ == '__main__':
	app.run(debug=True)

