<template>
  <div>
    <v-row justify="center">
      <v-col
        cols="12"
        sm="10"
        md="8"
        lg="6"
      >
        <v-card ref="form" class="px-3 pb-3">
          <v-card-text class="text-center">
            <v-card-title>
              <h2>{{ selectedPost.cafename }}</h2>
            </v-card-title>
            <v-divider class="mb-3"></v-divider>

            <v-row class="d-flex align-center justify-center">
              <span>맛</span>
              <v-rating
                v-model="selectedPost.taste"
                color="yellow darken-3"
                background-color="grey darken-1"
                empty-icon="$ratingFull"
                hover
              ></v-rating>
              <span>({{ selectedPost.taste }})</span>
            </v-row>

            <v-row class="d-flex align-center justify-center">
              <span>분위기</span>
              <v-rating
                v-model="selectedPost.mood"
                color="yellow darken-3"
                background-color="grey darken-1"
                empty-icon="$ratingFull"
                hover
              ></v-rating>
              <span>({{ selectedPost.mood }})</span>
            </v-row>

            <v-row class="d-flex align-center justify-center">
              <span>위생</span>
              <v-rating
                v-model="selectedPost.clean"
                color="yellow darken-3"
                background-color="grey darken-1"
                empty-icon="$ratingFull"
                hover
              ></v-rating>
              <span>({{ selectedPost.clean }})</span>
            </v-row>
            
            <v-textarea 
              label="Content" 
              v-model="selectedPost.contents"
              id="content"
              autofocus
            >
            </v-textarea>

            <v-file-input 
              accept="image/*"
              label="File input"
              @change="onFileChange"
              hint="* 사진을 변경할 경우 새로운 사진을 업로드 해주세요."
              persistent-hint
              class="mb-3"
            ></v-file-input>
            <v-img v-if="url" :src="url" contain max-width="100%" max-height="300px"></v-img>
          </v-card-text>
          <v-card-actions>
            <v-btn color="secondary" @click="$router.go(-1)" text>cancle</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="secondary" @click="uploadImage({selectedPost, formData})">Save</v-btn>
          </v-card-actions>
        </v-card>  
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'postUpdateView',
  data() {
    return {
      formData: new FormData(),
      url: null,
      selectedFile: null,
      disabled: true,
    }
  },
  computed: {
    ...mapState([
        'currentUser',
        'selectedPost',
      ])
  },
  methods: {
    ...mapActions([
        'uploadImage',
      ]),
    onFileChange(e) {
      if (!e) {
        this.url = null
      } else {
        this.selectedFile = e
        this.url = URL.createObjectURL(this.selectedFile)
        if (this.formData.get("image")) {
          this.formData.set("image", this.selectedFile, this.selectedFile.name)
        } else {
          this.formData.append("image", this.selectedFile, this.selectedFile.name)
        }
      }
    },
    checkImage(value) {
      if (!value) {
        return '사진을 등록해주세요.'
      } else {
        this.disabled = false
      }
    },
  },
  created() {
    this.url = 'https://i3a203.p.ssafy.io:5000/api/post/get/image/'+this.selectedPost.pno+'/'+new Date()
  },
}
</script>

<style scoped>
.post-checklist {
  justify-content: center;
  width: 100%;
  margin-top: 1rem;
}

.disabled-button {
  pointer-events: none;
}

</style>