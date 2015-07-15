# localhost:5000
import subprocess, sys, time, os.path
from flask import Flask, render_template, request, send_file

# init Flask application
app = Flask(__name__)

# route for default URL
@app.route('/')
def index():
	return render_template('template.html')

# **1**
@app.route('/my-link/')
def my_link():
	print 'I got clicked!'
	return 'Click.'
	# return ('',204)

	
# **3**
@app.route('/test/', methods=['POST'])
def req():
	start = time.time()
	npages = request.form['npages']
	cmd = ["./target_term", "-run", "1", "run", "/home/reid/Dropbox/MATLAB/LL/example.m"]
	q = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
	out,err = q.communicate()
	while os.path.isfile('/home/reid/Downloads/fnmfleet.github.io/templates/perday.png')==False:
		a = 5;
	return render_template('result.html', time=time.time()-start, url0='cumulative.png', url1='pie.png', url2='perday.png')
	# return render_template('result.html', time=time.time()-start)


# images
@app.route('/test/<path:filename>')
def images(filename):
	fullpath = '/home/reid/Downloads/fnmfleet.github.io/templates/' + filename
	return send_file(fullpath)


@app.route('/favicon.ico')
def favicon():
	return send_file('/home/reid/Downloads/fnmfleet.github.io/favicon.png')



# run
if __name__ == '__main__':
  app.run(debug=True)
