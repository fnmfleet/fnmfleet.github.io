import subprocess
from flask import Flask, render_template, request, url_for

# init Flask application
app = Flask(__name__)

# route for default URL
@app.route('/')
def index():
	return render_template('template.html')

@app.route('/my-link/')
def my_link():
	print 'I got clicked!'
	return 'Click.'

@app.route('/my-link-2/')
def my_link_2():
	cmd = ["./download.pl"]
	p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)
	out,err = p.communicate()
	return out

@app.route('/request/', methods=['POST'])
def req():
	npages = request.form['npages']
	cmd = ["./download2.pl", str(npages)]
	print cmd
	p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
	out,err = p.communicate()
#	return npages
#	return render_template('result.html', npages=npages)
	filename = "test%s.htm" % str(npages)
	return render_template(filename)

# run
if __name__ == '__main__':
  app.run(debug=True)
