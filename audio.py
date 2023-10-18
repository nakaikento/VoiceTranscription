import openai
import os

def transcribe_audio(audio_bytes):
    # bytes形式の音声を一時的なファイルに書き込む
    temp_file_path = "temp_audio.wav"
    with open(temp_file_path, 'wb') as temp_file:
        temp_file.write(audio_bytes)

    # Whisper APIを使用して文字起こしを実行
    with open(temp_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_file,
            response_format="json",
        )

    # 一時的なファイルを削除
    try:
        os.remove(temp_file_path)
    except OSError as e:
        pass  # エラーが発生しても無視

    # 応答から文字起こし結果を取得
    transcript_text = transcription["text"]
    
    return transcript_text
