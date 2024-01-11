"""
PDF to Audio Converter
This script converts all PDF files in a specified directory to MP3 audio files using pyttsx3 and PyPDF3 libraries.
"""

import pyttsx3
import PyPDF3
import os

# Define the path to the directory containing PDF files
files_path = "YOUR FOLDER PATH"

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Fetch all PDF files in the specified directory
files = [file for file in os.listdir(files_path) if file.endswith('.pdf')]

# Process each PDF file
for file in files:
    # Construct the full path to the file
    file_path = os.path.join(files_path, file)
    print(f"Processing {file_path}")

    # Use a context manager to open the file
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF3.PdfFileReader(pdf_file)
        full_text = []

        # Extract text from each page and clean it
        for page_num in range(pdf_reader.numPages):
            text = pdf_reader.getPage(page_num).extractText()
            clean_text = text.strip().replace('\n', ' ')
            full_text.append(clean_text)

        # Combine the extracted text from all pages
        all_text = ' '.join(full_text)

        # Convert the text to an audio file and save it
        audio_file_path = f"{file}.mp3"
        speaker.save_to_file(all_text, audio_file_path)
        speaker.runAndWait()
        speaker.stop()
        print(f"{file} has been successfully converted to audio.")
