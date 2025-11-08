from pathlib import Path
# пример библиотеки для синтеза голоса
from some_tts_library import synthesize_voice  

audio_file = Path("data/raw/defective.wav")
reference_text = Path("data/text/defective_transcript_fixed.txt")  # правильный текст
output_audio = Path("data/processed/fixed_speech.wav")
output_audio.parent.mkdir(exist_ok=True)

# читаем правильный текст
text = reference_text.read_text(encoding="utf-8")

# синтезируем исправленное аудио с сохранением тембра исходного голоса
synthesize_voice(text=text, voice_source=audio_file, output_file=output_audio)

print("✅ Исправленное аудио создано в:", output_audio)
