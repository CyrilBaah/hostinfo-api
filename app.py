from flask import Flask, jsonify
import os
import platform
import time
import sys

app = Flask(__name__)


@app.route('/system-info', methods=['GET'])
def get_system_info():
    system_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": sys.version,
        "time_utc": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()),
        "time_local": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
        "env_sample": {
            key: os.environ.get(key)
            for key in list(os.environ)[:5]
        }
    }
    return jsonify(system_info)


if __name__ == '__main__':
    app.run(debug=True)
