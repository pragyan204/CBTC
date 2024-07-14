import sounddevice as sd
import wavio

def record_audio(filename, duration):
    print("Recording now...")

    # Setting of parameters for recording audio.

    samplerate = 44100    # Sampling rate in Hz
    channels = 2     # Stereo audio

    # Recording the audio for the given duration.

    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels)
    sd.wait()    # Wait until recording is finished
    print("Recording finished.")

    # Saving the recorded audio as a WAV file

    wavio.write(filename, audio_data, samplerate, sampwidth=2)
    print(f"Audio saved as {filename}")

def main():
    filename = "recorded_audio.wav"
    duration = 15  # Duration of audio recording in seconds

    print("Welcome to the Simple Voice Recorder")

    # Start recording
    
    record_audio(filename, duration)

    print("Recording completed successfully.")

if __name__ == "__main__":
    main()
