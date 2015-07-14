# localhost:5000
import subprocess, sys
from flask import Flask, render_template, request, url_for

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
	return 'ClickClick!'
	# return ('',204)

# **2**
@app.route('/my-link-2/')
def my_link_2():
	cmd = ["perl", "/home/reid/Downloads/fnmfleet.github.io/download.pl"]
	p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)
	out,err = p.communicate()
	return out
	
# **3**
@app.route('/test/', methods=['POST'])
def req():
	npages = request.form['npages']
	# cmd = ["./download2.pl", str(npages)]
#	p = subprocess.Popen(cmd, stdout = subprocess.STDOUT,
#                            stderr=subprocess.STDOUT)
#	out,err = p.communicate()
	cmd = ["matlab", "-nodesktop", "-nosplash", "-r", "run('/home/reid/Dropbox/MATLAB/LL/example.m')"]
	print cmd
	q = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
	out,err = q.communicate()
#	return npages
	return render_template('result.html', npages=npages)
#	filename = "test%s.htm" % str(npages)
#	return render_template(filename)

# **4**
@app.route('/image/')
def upImage():
	cmd = ["./imgur", "templates/pie.png", "templates/cumulative.png", "templates/perday.png"]
	# p = subprocess.Popen(cmd, stdout = subprocess.PIPE)
	# out,err = p.communicate()
	url = range(4)
	out = 'http://i.imgur.com/3EsN13V.png\nhttp://i.imgur.com/S8Itlve.png\nhttp://i.imgur.com/xQBjh5S.png\nasdf'
	for idx, line in enumerate(out.split('\n')):
		url[idx] = line	
	return render_template('image.html', url0=url[0], url1=url[1], url2=url[2])

# run
if __name__ == '__main__':
  app.run(debug=True)
