from pathlib import Path
import whisper

audio_file = Path("data/raw/defective.wav")
output_dir = Path("data/text")
output_dir.mkdir(parents=True, exist_ok=True)

model = whisper.load_model("base")
result = model.transcribe(str(audio_file))

output_file = output_dir / "defective_transcript.txt"
output_file.write_text(result["text"], encoding="utf-8")

print("✅ Распознавание завершено. Текст сохранён в:", output_file)
