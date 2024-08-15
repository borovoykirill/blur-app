import os
import cv2
import numpy as np
from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

ENABLE_TOOL = os.getenv('ENABLE_TOOL')


@app.route('/blur', methods=['POST'])
def blur_image():

    if ENABLE_TOOL != 'true':
        return "The tool is not activated", 403

    image_file = request.files['image']
    image = Image.open(image_file)
    image = np.array(image)

    blurred_image = cv2.GaussianBlur(image, (21, 21), 0)
    blurred_image = Image.fromarray(blurred_image)

    img_io = io.BytesIO()
    blurred_image.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')


@app.route('/readiness', methods=['GET'])
def readiness():
    return "Ready", 200


@app.route('/liveness', methods=['GET'])
def liveness():
    return "Alive", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
