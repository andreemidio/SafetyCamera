from flask import Flask, render_template, Response
from camera import camera_stream

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')

def gen_frame():
    
    while True:
        frame = camera_stream()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

@app.route('/video_feed')
def video_feed():
    
    return Response(gen_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
