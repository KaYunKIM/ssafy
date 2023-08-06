import io
import os
import re
from google.cloud import speech
from . import TextRank
from . import Todo 

class STT():
    
    def __init__(self):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        self.file_name = ''

    def file_load(self,file_path):
        #self.file_name = os.path.join(os.path.dirname(__file__), "./", "test.wav")
        self.file_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), "media" , file_path)
        print(self.file_name)

    def speechtotext(self):
        client = speech.SpeechClient()
        with io.open(self.file_name, "rb") as audio_file:
            content = audio_file.read()
            #print(content)
            audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code="ko-KR",
            audio_channel_count=2,
        )

        # Detects speech in the audio file
        response = client.recognize(request={"config": config, "audio": audio})

        to_do_list = []
        todolist = Todo.ToDoList()
        tmp_text = ''''''
        for result in response.results:
            line = result.alternatives[0].transcript.strip() + "."
            print(line)
            tmp_text += (line + "\n")
            if(todolist.predict2(line) == 1) :
                to_do_list.append(line)
            
        textrank = TextRank.TextRank(tmp_text)
        txtComment = []
        num = 1
        to_do_num = 1

        for row in textrank.summarize(3):
            txtComment.append(row)
                
        for sentence in txtComment:
            print(str(num) + "." + sentence)
            num = num + 1

        print("\n상위 3개 키워드\n")
        key_list = []
        for key in textrank.keywords()[:3]:
            print(key)
            key_list.append(key)
                            
        print("\n업무로 분류된 문장\n")
        print(len(to_do_list))
        for line in to_do_list :
            print(str(to_do_num)+ ". " + line + "\n")
            to_do_num = to_do_num + 1

        return txtComment , key_list , to_do_list
    
    def get_tasklist(self, origin_text):
        
        to_do_list = []
        todolist = Todo.ToDoList()
        
        process_text = origin_text.replace("?", ".\n").replace("!", ". ").split(".")
        
        print(process_text)
        for line in process_text:
            print(line)
            if(todolist.predict2(line) == 1) :
                to_do_list.append(line)
            
        textrank = TextRank.TextRank(origin_text)
        txtComment = []
        num = 1
        to_do_num = 1

        for row in textrank.summarize(3):
            txtComment.append(row)
                
        for sentence in txtComment:
            print(str(num) + "." + sentence)
            num = num + 1

        print("\n상위 3개 키워드\n")
        key_list = []
        for key in textrank.keywords()[:3]:
            print(key)
            key_list.append(key)
                            
        print("\n업무로 분류된 문장\n")
        print(len(to_do_list))
        for line in to_do_list :
            print(str(to_do_num)+ ". " + line + "\n")
            to_do_num = to_do_num + 1

        return txtComment , key_list , to_do_list