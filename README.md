# Adaptive Audio Steganography using Syndrome-Trellis Codes (STC) and GOAS

## 🔐 Overview
This project presents an intelligent, secure, and robust audio steganography system designed for real-time applications. It employs a hybrid approach integrating:
- **Syndrome-Trellis Codes (STC)** for secure and imperceptible data embedding
- **Global Optimization of Adaptive Steganography (GOAS)** for optimal segment selection
- **Hamming (7,4) Codes** for error correction

---

## 🎯 Features
- ✅ **Secure and Non-Intrusive Audio Embedding**
- 🎧 **Preserves Audio Quality** with high SNR and PSNR values
- 📈 **Performance Metrics**: SNR, PSNR, and BER computed
- 🧠 **GOAS for Intelligent Embedding Region Selection**
- ♻️ **Error Correction** with Hamming (7,4) codes
- 🌐 **User-Friendly Flask GUI**
- 📊 **Auto-Generated PDF Reports** with waveform and spectrogram plots

---

## 🧱 System Architecture
- **Preprocessing Module** – PCM conversion and normalization
- **Message Encoding** – Hamming-based error control
- **GOAS Segment Selector** – Identifies optimal regions for embedding
- **STC Embedding Engine** – Secure and low-distortion message embedding
- **Extraction Engine** – Accurate recovery using GOAS + Hamming Decoding
- **PDF Generator** – Report generation with visual and metric outputs

---

## 💡Future Enhancements
- Deep Learning-based embedding optimization

- Multi-format audio (MP3, FLAC, AAC) support

- Mobile app integration (Flutter/React Native)

- Real-time steganography for live voice calls

- Cloud deployment with API-based access
