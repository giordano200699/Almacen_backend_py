from flask import (render_template)
import connexion


app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')

@app.route('/')
def vistaInicial():
	return render_template('vistaInicial.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=False)