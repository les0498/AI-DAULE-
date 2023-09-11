import subprocess
import tkinter as tk
from gtts import gTTS
import os
import random

# Create a Tkinter window
window = tk.Tk()
window.title("ChatGPT Output")
window.geometry("400x300")

# Create a label to display the output
output_label = tk.Label(window, text="ChatGPT Output:", font=("Arial", 14))
output_label.pack(pady=10)

output_text = tk.Text(window, height=10, width=40)
output_text.pack()

# Function to generate and play TTS audio
def generate_tts():
    with open("chatGPT_result.txt", "r", encoding="utf-8") as file:
        GPT = file.read()

    lines = GPT.splitlines()
    random_line = random.choice(lines)

    if '1.' in random_line:
        tts_text = random_line.replace("1.", "")
    if '2.' in random_line:
        tts_text = random_line.replace("2.", "")
    if '3.' in random_line:
        tts_text = random_line.replace("3.", "")
    if '4.' in random_line:
        tts_text = random_line.replace("4.", "")
    if '5.' in random_line:
        tts_text = random_line.replace("5.", "")

    tts = gTTS(text=tts_text, lang='ko')
    output_file = "output.mp3"
    tts.save(output_file)
    os.system(f"start {output_file}")

# Button to generate TTS audio
generate_button = tk.Button(window, text="Generate TTS", command=generate_tts)
generate_button.pack(pady=10)

# Function to open the Satisfaction_check.py script
def open_satisfaction_check():
    subprocess.Popen(['python', 'Satisfaction_check.py'])

# Button to open Satisfaction_check.py
satisfaction_button = tk.Button(window, text="Open Satisfaction Check", command=open_satisfaction_check)
satisfaction_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
