from flask import Flask,render_template,request
from weather import weather_info,quotes_info

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	if request.method=='POST':
		city=request.form['city']
		units=request.form['units']
		info=weather_info(city,units)
		quote=quotes_info()
		return render_template('home.html',title='homepage',info=info,quote=quote)

	return render_template('home.html',title='homepage')

app.run(debug=True)