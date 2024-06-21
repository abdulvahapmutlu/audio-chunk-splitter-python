import os
import librosa
import soundfile as sf
import numpy as np

def split_audio(file_path, output_dir, chunk_duration=3.0, sr=22050):
    try:
        # Load the audio file
        y, sr = librosa.load(file_path, sr=sr)
        
        # Calculate the number of samples per chunk
        chunk_length = int(chunk_duration * sr)
        
        # Skip audio files that are shorter than the chunk duration
        if len(y) < chunk_length:
            print(f"Skipping {file_path}: audio file is shorter than {chunk_duration} seconds.")
            return
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Split the audio into chunks
        for i in range(0, len(y), chunk_length):
            chunk = y[i:i + chunk_length]
            
            # Ensure the chunk is exactly the right length
            if len(chunk) < chunk_length:
                chunk = np.pad(chunk, (0, chunk_length - len(chunk)), mode='constant')
            
            # Save the chunk to a file
            chunk_filename = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(file_path))[0]}_chunk{i//chunk_length}.wav")
            sf.write(chunk_filename, chunk, sr)
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(input_dir, output_dir, chunk_duration=3.0, sr=22050):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(('.wav', '.mp3', '.flac')):  # Adjust according to your file formats
                file_path = os.path.join(root, file)
                split_audio(file_path, output_dir, chunk_duration, sr)

# Define the input and output directories
input_dir = 'path/to/input_directory'
output_dir = 'path/to/output_directory'

# Process the directory
process_directory(input_dir, output_dir)
