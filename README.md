# Audio Analyzer

An audio analysis script built with **librosa**. Estimates tempo (BPM), spectral brightness, and duration, then visualizes the waveform and spectrogram.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![librosa](https://img.shields.io/badge/librosa-Audio%20Analysis-teal)

---

## 🇬🇧 English.

### Overview
This script loads an audio file and extracts several analytical features: estimated tempo (BPM), spectral centroid (a measure of "brightness"), and total duration. It then renders two plots — a waveform and a spectrogram — for visual inspection.

### Features
- Tempo (BPM) estimation via beat tracking
- Spectral centroid calculation (brightness/timbre indicator)
- Duration reporting
- Combined waveform + spectrogram visualization
- Structured logging via Loguru
- Clear error handling for missing files

### Requirements
- Python 3.10 or higher
- `librosa`
- `matplotlib`
- `numpy`
- `loguru`

### Installation
```bash
pip install librosa matplotlib numpy loguru
```

### Usage
1. Place your audio file in the same folder as the script (or update `INPUT_FILE` with the full path).
2. Run:
```bash
python audio_analyzer.py
```

A window will open showing the waveform on top and the spectrogram below.

### How it works
`librosa.load()` reads the audio into a waveform array (`y`) along with its sample rate (`sr`). `librosa.beat.beat_track()` estimates the tempo by detecting rhythmic beat positions. `librosa.feature.spectral_centroid()` computes the "center of mass" of the frequency spectrum at each point in time — higher values indicate a brighter, more treble-heavy sound. The spectrogram is generated via `librosa.stft()` (Short-Time Fourier Transform), converted to decibels, and displayed on a logarithmic frequency axis for readability.

---

## 🇩🇪 Deutsch

### Überblick
Dieses Skript lädt eine Audiodatei und extrahiert mehrere analytische Merkmale: geschätztes Tempo (BPM), spektralen Schwerpunkt (ein Maß für "Helligkeit") und die Gesamtdauer. Anschließend werden zwei Diagramme gerendert — eine Wellenform und ein Spektrogramm — zur visuellen Untersuchung.

### Funktionen
- Tempo-Schätzung (BPM) über Beat-Tracking
- Berechnung des spektralen Schwerpunkts (Helligkeits-/Klangfarbenindikator)
- Ausgabe der Dauer
- Kombinierte Wellenform- + Spektrogramm-Visualisierung
- Strukturiertes Logging über Loguru
- Klare Fehlerbehandlung bei fehlenden Dateien

### Voraussetzungen
- Python 3.10 oder höher
- `librosa`
- `matplotlib`
- `numpy`
- `loguru`

### Installation
```bash
pip install librosa matplotlib numpy loguru
```

### Verwendung
1. Lege deine Audiodatei im selben Ordner wie das Skript ab (oder aktualisiere `INPUT_FILE` mit dem vollständigen Pfad).
2. Ausführen:
```bash
python audio_analyzer.py
```

Ein Fenster öffnet sich mit der Wellenform oben und dem Spektrogramm darunter.

### Funktionsweise
`librosa.load()` liest das Audio in ein Wellenform-Array (`y`) zusammen mit seiner Abtastrate (`sr`) ein. `librosa.beat.beat_track()` schätzt das Tempo, indem es rhythmische Beat-Positionen erkennt. `librosa.feature.spectral_centroid()` berechnet den "Schwerpunkt" des Frequenzspektrums zu jedem Zeitpunkt — höhere Werte deuten auf einen helleren, höhenlastigeren Klang hin. Das Spektrogramm wird über `librosa.stft()` (Short-Time Fourier Transform) erzeugt, in Dezibel umgewandelt und zur besseren Lesbarkeit auf einer logarithmischen Frequenzachse dargestellt.

---

## 🇹🇷 Türkçe

### Genel Bakış
Bu script bir ses dosyasını yükler ve birkaç analitik özellik çıkarır: tahmini tempo (BPM), spektral merkez (bir "parlaklık" ölçüsü) ve toplam süre. Ardından görsel inceleme için iki grafik render eder — bir waveform (dalga formu) ve bir spectrogram (spektrogram).

### Özellikler
- Beat tracking (vuru tespiti) yoluyla tempo (BPM) tahmini
- Spektral merkez hesaplaması (parlaklık/tını göstergesi)
- Süre raporlama
- Birleşik waveform + spectrogram görselleştirmesi
- Loguru üzerinden yapılandırılmış loglama
- Eksik dosyalar için net hata yönetimi

### Gereksinimler
- Python 3.10 veya üzeri
- `librosa`
- `matplotlib`
- `numpy`
- `loguru`

### Kurulum
```bash
pip install librosa matplotlib numpy loguru
```

### Kullanım
1. Ses dosyanı scriptle aynı klasöre koy (veya `INPUT_FILE`'ı tam dosya yoluyla güncelle).
2. Çalıştır:
```bash
python audio_analyzer.py
```

Üstte waveform, altta spectrogram olacak şekilde bir pencere açılır.

### Nasıl çalışır?
`librosa.load()`, sesi örnekleme hızıyla (`sr`) birlikte bir waveform dizisine (`y`) okur. `librosa.beat.beat_track()`, ritmik vuru pozisyonlarını tespit ederek tempoyu tahmin eder. `librosa.feature.spectral_centroid()`, her zaman noktasında frekans spektrumunun "kütle merkezini" hesaplar — daha yüksek değerler daha parlak, tiz ağırlıklı bir sesi gösterir. Spectrogram, `librosa.stft()` (Kısa Süreli Fourier Dönüşümü) ile üretilir, desibele dönüştürülür ve okunabilirlik için logaritmik bir frekans ekseninde gösterilir.
