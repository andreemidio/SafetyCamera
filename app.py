from flask import Flask, render_template, Response
from camera import camera_stream

app = Flask(__name__)

@app.route('/')
def index():
    """Que haja luz"""
    return render_template('index.html')


def generatorFrame():

    while (True):
        frame =  camera_stream()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') # concatena cada frame um a um

@app.route('/video')
def video():

    return Response(
    generatorFrame(),
    mimetype = 'multipart/x-mixed-replace; boundary = frame' 

    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)