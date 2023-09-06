from pydub import AudioSegment
import whisper




# 讀取下載下來的音檔
# audio_file = AudioSegment.from_file("/Users/chunchun/pyClassKeeping/one_minute_song.mp3")

# # 檢查音檔是否可以正常解碼
# print(audio_file)

# 將音檔轉換為 MP3 格式
# mp3_file = audio_file.export("path/to/save/directory/audio.mp3", format="mp3")

# 讀取 MP3 檔案，轉成文字檔案
model = whisper.load_model("medium")
result = model.transcribe("/Users/chunchun/pyClassKeeping/嵌入式系統_L1.m4a",language='zh')
print(result["text"])