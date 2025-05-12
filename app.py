from flask import Flask, render_template, request, send_file
import os
import soundfile as sf
import numpy as np
from stego_utils import generate_h_matrix, embed_message, extract_message

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    file = request.files['audio']
    message = request.form['message']

    if file and message:
        try:
            audio_data, sr = sf.read(file)
            audio_data = np.int16(audio_data * 32767)

            h_matrix = generate_h_matrix(8)
            stego_audio = embed_message(audio_data, message, h_matrix)

            stego_audio_path = 'static/stego_audio.wav'
            os.makedirs(os.path.dirname(stego_audio_path), exist_ok=True)
            sf.write(stego_audio_path, stego_audio, sr)

            if os.path.exists(stego_audio_path):
                return send_file(stego_audio_path, as_attachment=True)
            else:
                return "Error: File was not created."

        except Exception as e:
            return f"Error: {e}"

    return "Error: Missing audio or message."

@app.route('/extract', methods=['POST'])
def extract_audio_message():
    file = request.files['audio']

    if file:
        try:
            audio_data, sr = sf.read(file)
            audio_data = np.int16(audio_data * 32767)

            h_matrix = generate_h_matrix(8)
            extracted_message = extract_message(audio_data, h_matrix)
            return f"Extracted Message: {extracted_message}"

        except Exception as e:
            return f"Error: {e}"

    return "Error: No audio file provided."

if __name__ == '__main__':
    app.run(debug=True)
