<template>
	<v-container>
		<p class="font-weight-medium">오늘의 회의를 시작하세요 :)</p>
		<v-row cols="12" style="margin: auto 0;">
			<v-col cols="8">
				<v-select v-bind:items="items" v-model="selected" label="녹음 언어를 선택해주세요"></v-select>
			</v-col>
			<v-col cols="4">
				<v-btn v-show="btn" @click.native="startRecording" class="ma-2" outlined fab color="#4c4c65">
					<v-icon>fas fa-microphone</v-icon></v-btn>
				<v-btn v-show="btnStop" @click.native="stopRecording" class="ma-2" outlined fab color="error">
					<v-icon>fas fa-microphone</v-icon></v-btn>
			</v-col>
		</v-row>
		<transition name="slide">
			<div v-show="result">
				<v-card color="#4c4c65" dark>
					<v-card-title class="headline">
						오늘의 회의가 녹음되고 있습니다 :)
					</v-card-title>
					<v-divider class="mx-4"></v-divider>
					<v-card-subtitle>
						<div>{{textResult}}</div>
					</v-card-subtitle>
				</v-card>
			</div>
		</transition>
	</v-container>
</template>

<script>
// var audioContext = new(window.AudioContext || window.webkitAudioContext)();
var audioContext = null;
var socket = io.connect('http://k3a305.p.ssafy.io:3555');
var ssStream = ss.createStream();
var scriptNode;
import { mapActions} from "vuex";

export default {
	data() {
		return {
      originData : {
        text: "",
        meetingId: "",
      },
			btn: true,
			btnStop: false,
			result: false,
			resultError: false,
			textResult: "",
			selected: 'ko-KR',
			intervalTime: 3600000,
			items: [
				{
					text: '한국어 (대한민국)',
					value: 'ko-KR'
				},
				{
					text: 'English (Great Britain)',
					value: 'en-GB'
				},
				{
					text: 'English (India)',
					value: 'en-IN'
				},
				{
					text: 'English (United States)',
					value: 'en-US'
				},
				{
					text: 'Français (France)',
					value: 'fr-FR'
				},
				{
					text: '日本語（日本)',
					value: 'ja-JP'
				},
				{
					text: '普通话 (中国大陆)',
					value: 'cmn-Hans-CN'
				}
			]
		}
  },
  props: {
    meetingId: Number
  },
  methods: {
    ensureAudioContext() {
      // due to https://goo.gl/7K7WLu we don't activate AudioContext until after a user interaction (such as clicking the record button)
      audioContext = audioContext || new(window.AudioContext || window.webkitAudioContext)();
    },
    successCallback(stream) {
      this.ensureAudioContext();
      const vm = this;
      console.log('successCallback:....IN');
      var input = audioContext.createMediaStreamSource(stream);
      var bufferSize = 2048;
      scriptNode = audioContext.createScriptProcessor(bufferSize, 1, 1);
      scriptNode.onaudioprocess = scriptNodeProcess;
      input.connect(scriptNode);
      // console.log('ScriptNode BufferSize:', scriptNode.bufferSize);
      function scriptNodeProcess(audioProcessingEvent) {
        var inputBuffer = audioProcessingEvent.inputBuffer;
        var outputBuffer = audioProcessingEvent.outputBuffer;
        var inputData = inputBuffer.getChannelData(0);
        var outputData = outputBuffer.getChannelData(0);


        // Loop through the 4096 samples
        for (var sample = 0; sample < inputBuffer.length; sample++) {
          outputData[sample] = inputData[sample];
        }
        ssStream.write(new ss.Buffer(vm.downsampleBuffer(inputData, 44100, 16000)));
      }
    },
    downsampleBuffer(buffer, sampleRate, outSampleRate) {
      if (outSampleRate == sampleRate) {
        return buffer;
      }
      if (outSampleRate > sampleRate) {
        throw "downsampling rate show be smaller than original sample rate";
      }
      var sampleRateRatio = sampleRate / outSampleRate;
      var newLength = Math.round(buffer.length / sampleRateRatio);
      var result = new Int16Array(newLength);
      var offsetResult = 0;
      var offsetBuffer = 0;
      while (offsetResult < result.length) {
        var nextOffsetBuffer = Math.round((offsetResult + 1) * sampleRateRatio);
        var accum = 0,
          count = 0;
        for (var i = offsetBuffer; i < nextOffsetBuffer && i < buffer.length; i++) {
          accum += buffer[i];
          count++;
        }
        
        result[offsetResult] = Math.min(1, accum / count) * 0x7FFF;
        offsetResult++;
        offsetBuffer = nextOffsetBuffer;
      }
      return result.buffer;
    },
    startRecording() {
      this.ensureAudioContext();
      const languageSelected = this.selected;
      socket.emit('LANGUAGE_SPEECH', languageSelected);
      this.result = true;
      this.btn = false;
      this.btnStop = true;
      scriptNode.connect(audioContext.destination);
      ss(socket).emit('START_SPEECH', ssStream);
      setInterval(function() {
        this.stopRecording();
      }.bind(this), this.intervalTime);
    },
    stopRecording() {
      this.ensureAudioContext();
      this.btnStop = false;
      this.btn = true;
      this.intervalTime = 0;
      scriptNode.disconnect(audioContext.destination);
      ssStream.end();
      socket.emit('STOP_SPEECH', {});
      this.originData.text = this.textResult
      this.originData.meetingId = this.meetingId
      this.updateSTTInfo(this.originData);
    },
    errorCallback(error) {
      console.log('errorCallback:', error);
    },
    redirectError(){
      window.location.href = "http://localhost:8080/"
    },
    ...mapActions([
      "updateSTTInfo"
    ]),
  },
  created() {
    const that = this;
    
    socket.on('SPEECH_RESULTS', function(text) {
      if('Reached_transcription_time_limit' == text){
        that.resultError = true;
      } else {
              that.textResult += text;
        }
      })
        if (navigator.mediaDevices.getUserMedia) {
          console.log('getUserMedia supported...');
          navigator.webkitGetUserMedia({ audio: true }, function(stream) {
            that.successCallback(stream)
          }, function(error) {
            that.errorCallback(error)
          });
        } else {
          console.log('getUserMedia not supported on your browser!');
        }
      }
    }
</script>


<style>
  .slide-enter {
    opacity: 0;
  }

  .slide-enter-active {
    animation: slide-in 1s ease-out forwards;
    transition: opacity .5s;
  }

  .slide-move {
    transition: transform 1s;
  }

  @keyframes slide-in {
    from {
      transform: translateY(20px);
    }
    to {
      transform: translateY(0);
    }
  }
</style>
