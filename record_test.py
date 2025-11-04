# --- Imports ---
import sounddevice as sd            # audio recording (mic capture)
import numpy as np                  # arrays / math (peak calculation, etc.)
import scipy.io.wavfile             # simple WAV writer
import ffmpeg                       # Python wrapper for FFmpeg CLI (for MP3 conversion)
import shutil                       # to locate ffmpeg via PATH (shutil.which)
import os                           # filesystem ops (exists, remove, abspath)
import re                           # sanitize filenames (remove illegal chars on Windows)
from datetime import datetime       # timestamps (optional in filenames)

"""
    Sanitize a user-supplied filename for Windows:
    - Trim whitespace
    - Replace illegal characters <>:\"/\\|?* with underscores
    - Remove trailing spaces/dots (Windows doesn't like them)
    - Fallback to 'recording' if empty
"""
def new_filename(name: str) -> str:
    name = name.strip()
    if not name:
        name = "recording"
    name = re.sub(r'[<>:"/\\|?*]', "_", name)   # illegal chars -> "_"
    name = name.rstrip(" .")                    # no trailing dot/space
    return name or "recording"

# --- Filename input + sanitize + ensure uniqueness
user_name = input("Save name (without extension): ").strip()  # e.g., "lecture01"
user_name = new_filename(user_name)                            # clean up for Windows

# Ask if you want to append a timestamp (helps keep files unique & sortable)
add_ts = input("Add timestamp to filename? (y/N): ").strip().lower() == "y"
if add_ts:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")          # e.g., 20251031_123045
    base = f"{user_name}_{stamp}"
else:
    base = user_name

"""
    Avoid accidental overwrite by appending _1, _2, ... if a file exists.
    Checks both .wav and .mp3.
"""
def unique_base(base: str) -> str:
    candidate = base
    i = 1
    while os.path.exists(f"{candidate}.wav") or os.path.exists(f"{candidate}.mp3"):
        candidate = f"{base}_{i}"
        i += 1
    return candidate

base = unique_base(base)                  # make sure name doesn't clash
WAV_OUT = f"{base}.wav"                   # final WAV path
MP3_OUT = f"{base}.mp3"                   # final MP3 path

print(f"\nFiles will be saved as:\n  WAV → {WAV_OUT}\n  MP3 → {MP3_OUT}\n")

# Recording parameters
DURATION = 5                               # seconds to record
CHANNELS = 1                               # 1=mono (common for built-in mics). Use 2 for stereo-capable mics.

# When you want to save just 1 output
# WAV_OUT = "temp.wav"
# MP3_OUT = "output.mp3"

# List available audio devices so you can pick the correct mic index (look for in: > 0)
print("\n=== Available audio devices ===")
for i, d in enumerate(sd.query_devices()):
    print(f"{i:>2}: {d['name']}  (in:{d['max_input_channels']}, out:{d['max_output_channels']})")

# IMPORTANT: Set this to your mic's index from the printed list above
INPUT_DEVICE_INDEX = 1  # apne mic ka index yahan set karo (e.g., 0, 1, 2...)

# Choose a safe sample rate: prefer device default; otherwise fall back to 44100 Hz
default_sr = int(sd.query_devices(kind='input')['default_samplerate'])
SAMPLE_RATE = default_sr if default_sr else 44100
print(f"\nUsing sample rate: {SAMPLE_RATE}")

# Record audio
print("\nRecording...")
sd.default.samplerate = SAMPLE_RATE
if INPUT_DEVICE_INDEX is not None:
    # Set default devices as a tuple (input, output). We only set input here.
    sd.default.device = (INPUT_DEVICE_INDEX, None)

# Validate device / samplerate / channels before recording (raises helpful error if invalid)
sd.check_input_settings(
    device=sd.default.device[0] if isinstance(sd.default.device, tuple) else sd.default.device,
    samplerate=SAMPLE_RATE, channels=CHANNELS
)

# Start recording into an int16 numpy array with shape (num_samples, channels)
audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='int16')
sd.wait()                                   # block until capture finishes
print("Recording complete.")

# Quick sanity check: if peak ~ 0, input was silent (wrong device, muted mic, gain/permissions issue)
peak = int(np.abs(audio).max())
print(f"Peak level: {peak} (0 means silence)")

# Save WAV with the chosen name (lossless & good for debugging if MP3 conversion fails)
scipy.io.wavfile.write(WAV_OUT, SAMPLE_RATE, audio.squeeze())
print(f"WAV saved: {os.path.abspath(WAV_OUT)}")

# --- Resolve FFmpeg path ---
ffmpeg_bin = shutil.which("ffmpeg")  # first try system PATH
if ffmpeg_bin is None:
    # Fallback: your local ffmpeg.exe path (update if your folder is different)
    ffmpeg_bin = r"C:\USA\UMBC\PROJECT\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

print(f"Using ffmpeg at: {ffmpeg_bin}")

# Convert WAV → MP3
# - format='mp3': output codec/container
# - audio_bitrate='192k': common quality setting
# - ar=SAMPLE_RATE & ac=CHANNELS: keep consistency with the recording
(
    ffmpeg
    .input(WAV_OUT)
    .output(MP3_OUT, format='mp3', audio_bitrate='192k', ar=SAMPLE_RATE, ac=CHANNELS)
    .run(cmd=ffmpeg_bin, overwrite_output=True)
)

# Delete WAV after converting (keep folder clean). Comment out if you want to retain WAV.
try:
    os.remove(WAV_OUT)
    print(f"Deleted temp file: {WAV_OUT}")
except OSError:
    # If deletion fails (e.g., file open in another app), ignore
    pass


print(f"MP3 saved: {os.path.abspath(MP3_OUT)}")

