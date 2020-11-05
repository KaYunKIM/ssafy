import STT2

speak = STT2.STT()

speak.file_load("test.wav")

speak.speechtotext()