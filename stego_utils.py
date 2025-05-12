import numpy as np
from bitarray import bitarray
from scipy.linalg import hadamard

def text_to_bits(message):
    return np.array([int(b) for char in message for b in format(ord(char), '08b')])

def bits_to_text(bits):
    chars = [chr(int(''.join(map(str, bits[i:i+8])), 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)

def hamming_encode_4bit(data_bits):
    G = np.array([[1, 0, 0, 0, 1, 1, 0],
                  [0, 1, 0, 0, 1, 0, 1],
                  [0, 0, 1, 0, 0, 1, 1],
                  [0, 0, 0, 1, 1, 1, 1]])
    return np.dot(data_bits, G) % 2

def hamming_decode_7bit(code_bits):
    H = np.array([[1, 1, 0, 1, 1, 0, 0],
                  [1, 0, 1, 1, 0, 1, 0],
                  [0, 1, 1, 1, 0, 0, 1]])
    syndrome = np.dot(H, code_bits) % 2
    error_index = int(''.join(map(str, syndrome)), 2)
    if error_index > 0 and error_index <= 7:
        code_bits[error_index - 1] ^= 1
    return code_bits[:4]

def goas_select_segments(audio, block_size, num_segments_needed):
    complexities = []
    for i in range(0, len(audio) - block_size, block_size):
        block = audio[i:i + block_size]
        diff = np.sum(np.abs(np.diff(block)))
        complexities.append((i, diff))
    complexities.sort(key=lambda x: -x[1])
    return [idx for idx, _ in complexities[:num_segments_needed]]

def generate_h_matrix(order):
    return hadamard(order)

def embed_message(audio, message, h_matrix):
    bits = text_to_bits(message)
    block_size = h_matrix.shape[1]
    num_segments = int(np.ceil(len(bits) / block_size))
    segment_indices = goas_select_segments(audio, block_size, num_segments)
    embedded_audio = audio.copy()

    idx = 0
    for seg_start in segment_indices:
        if idx >= len(bits):
            break
        segment = audio[seg_start:seg_start + block_size]
        for i in range(block_size):
            if idx < len(bits):
                segment[i] = (segment[i] & ~1) | bits[idx]
                idx += 1
        embedded_audio[seg_start:seg_start + block_size] = segment
    return embedded_audio

def extract_message(audio, h_matrix):
    block_size = h_matrix.shape[1]
    num_bits = 1000  # You may dynamically detect this in future
    num_segments = int(np.ceil(num_bits / block_size))
    segment_indices = goas_select_segments(audio, block_size, num_segments)
    extracted_bits = []

    for seg_start in segment_indices:
        segment = audio[seg_start:seg_start + block_size]
        for i in range(min(block_size, num_bits - len(extracted_bits))):
            extracted_bits.append(segment[i] & 1)
        if len(extracted_bits) >= num_bits:
            break

    return bits_to_text(extracted_bits)
