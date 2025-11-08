from pathlib import Path

data_dir = Path("data/raw")
text_dir = Path("data/text")

for audio_file in data_dir.glob("*.wav"):
    text_file = text_dir / (audio_file.stem + ".txt")
    if text_file.exists():
        correct_text = text_file.read_text(encoding="utf-8")
        audio_features = extract_audio_features(audio_file)  # функция подготовки аудио
        model.train_step(audio_features, correct_text)       # обучение модели
