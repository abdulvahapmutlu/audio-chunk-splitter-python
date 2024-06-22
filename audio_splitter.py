import os
import librosa
import soundfile as sf
import numpy as np

def split_audio(file_path, output_dir, chunk_duration=3.0, sr=22050, start_index=1):
    try:
        
        # Load the audio file
        y, sr = librosa.load(file_path, sr=sr)
        duration = librosa.get_duration(y=y, sr=sr)
        
        # Skip audio files that are shorter than or equal to the chunk duration
        if duration <= chunk_duration:
            print(f"Skipping file {file_path} because its duration ({duration} seconds) is less than or equal to {chunk_duration} seconds.")
            return start_index

        # Calculate the number of samples per chunk
        chunk_length = int(chunk_duration * sr)
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        index = start_index

        # Split the audio into chunks
        for i in range(0, len(y), chunk_length):
            chunk = y[i:i + chunk_length]

            # Ensure the chunk is exactly the right length
            if len(chunk) < chunk_length:
                chunk = np.pad(chunk, (0, chunk_length - len(chunk)), mode='constant')
            
            # Save the chunk to a file
            chunk_filename = os.path.join(output_dir, f"{index}.wav")
            sf.write(chunk_filename, chunk, sr)
            index += 1
        
        return index
    
    except Exception as e:
        print(f"File can not be processed. {file_path}: {e}")
        return start_index

def process_directory(input_dir, output_dir, chunk_duration=3.0, sr=22050):
    index = 1
    for root, _, files in os.walk(input_dir):
        for file in files:
            #You can customize file extension here.
            if file.endswith(('.wav', '.mp3', '.flac')):
                file_path = os.path.join(root, file)
                index = split_audio(file_path, output_dir, chunk_duration, sr, index)

# Define the input and output directories
input_dir = 'path/to/input_directory'
output_dir = 'path/to/output_directory'

# Process the directory
process_directory(input_dir, output_dir)

#Finish
print("Process completed")
