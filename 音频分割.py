import librosa
import soundfile


def wavfile_split(filename, split_at_timestamp=20, min_time=12):
    wav_list = []
    data, rate = soundfile.read(filename)  # 调用soundfile载入音频
    split_at_frame = rate * split_at_timestamp
    wav_time = librosa.get_duration(filename=filename, sr=rate)
    num = int(wav_time / split_at_timestamp)
    for i in range(num):
        split_data = data[i * split_at_frame:(i + 1) * split_at_frame]
        wav_list.append(split_data)
        new_path = 'foo_{}.wav'.format(i)
        soundfile.write(new_path, split_data, 16000)
    if wav_time % split_at_timestamp > min_time:
        wav_list.append(data[-split_at_frame:])
        num = num + 1

        new_path = 'foo_{}.wav'.format(num)
        soundfile.write(new_path, data[-split_at_frame:], 16000)
    return wav_list