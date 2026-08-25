import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from loguru import logger

INPUT_FILE = "input.wav"


def analyze_audio(file_path):
    logger.info(f"Loading {file_path}...")

    try:
        y, sr = librosa.load(file_path)

        # Estimate tempo (BPM). In recent librosa versions, tempo is returned as an array.
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        bpm = float(tempo[0]) if isinstance(tempo, (np.ndarray, list)) else float(tempo)
        logger.success(f"Estimated tempo: {bpm:.2f} BPM")

        # Estimate spectral centroid (a rough measure of "brightness" of the sound)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        avg_brightness = float(np.mean(spectral_centroid))
        logger.info(f"Average spectral centroid: {avg_brightness:.2f} Hz")

        duration = librosa.get_duration(y=y, sr=sr)
        logger.info(f"Duration: {duration:.2f} seconds")

        # Plot waveform and spectrogram side by side
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))

        librosa.display.waveshow(y, sr=sr, color="cyan", ax=axes[0])
        axes[0].set_title("Waveform")
        axes[0].set_xlabel("Time (s)")
        axes[0].set_ylabel("Amplitude")

        spectrogram = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
        img = librosa.display.specshow(spectrogram, sr=sr, x_axis="time", y_axis="log", ax=axes[1])
        axes[1].set_title("Spectrogram")
        fig.colorbar(img, ax=axes[1], format="%+2.0f dB")

        plt.tight_layout()
        logger.info("Rendering plots...")
        plt.show()

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    analyze_audio(INPUT_FILE)
