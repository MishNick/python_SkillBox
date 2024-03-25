from flask import Flask, request

app = Flask(__name__)

@app.route('/logs', methods=['POST'])
def receive_logs():
    log_record = request.json
    return 'Log received'

if __name__ == '__main__':
    app.run()
