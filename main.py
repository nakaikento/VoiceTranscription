from audio import transcribe_audio
import streamlit as st
from audio_recorder_streamlit import audio_recorder

st.title("Voice Transcription")

audio_bytes = audio_recorder(
      text="",
      icon_size="6x",
)

if audio_bytes:

      # 上で取得したaudio_bytesを使用して文字起こしを実行
      audio_transcription = transcribe_audio(audio_bytes)

      # 結果を出力
      st.write(audio_transcription)