# Audio Chunk Splitter with Python
A Python script to split audio files into smaller chunks of specified duration.

### Purpose
The primary purpose of this code is to facilitate the segmentation of long audio recordings into smaller, manageable pieces. This is particularly useful for machine learning tasks, audio analysis, or any application requiring fixed-duration audio segments. The code processes all audio files in a specified directory sequentially, applying the same method to each file. Additionally, it creates an indexed number for each split and saved chunk file, with the index starting at 1. This ensures easy identification and organization of the audio segments.



### Features
- Supports various audio formats: `.wav`, `.mp3`, `.flac` + You can adjust the code by adding audio formats that you wish.
- Splits audio files into chunks of configurable duration, in the code it's 3 seconds.
- Automatically handles audio files shorter than the chunk duration.
- Ensures each chunk is the exact specified length using padding if necessary.

### Requirements
- Python 3.x
- `librosa`
- `soundfile`
- `numpy`

### Installation
pip install librosa soundfile numpy


### Usage
1. Define the paths of the input and output directories in the script.
2. Personalize if you need to.
3. Run the script to process and split all audio files in the input directory.

### Example
python
input_dir = 'path/to/your/input_directory'
output_dir = 'path/to/your/output_directory'
process_directory(input_dir, output_dir)


### Arguments :
- file_path (str): Path to the input audio file.
- output_dir (str): Directory to save the audio chunks.
- chunk_duration (float): Duration of each chunk in seconds.
- sr (int): Sampling rate to use for the audio file.    
- input_dir (str): Path to the input directory containing audio files.
    
    
### License
MIT License
