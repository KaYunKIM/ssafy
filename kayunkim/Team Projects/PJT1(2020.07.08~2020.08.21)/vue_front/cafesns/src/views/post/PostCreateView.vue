<template>
  <div>
    <v-row justify="center">
      <v-col
        cols="12"
        sm="10"
        md="8"
        lg="6"
      >
        <v-card ref="form" class="px-3">
          <v-card-text class="text-center">
            <v-card-title>
              <h1>{{ selectedCafe.name }}</h1>
            </v-card-title>
            <v-divider class="mb-3"></v-divider>

            <v-row class="d-flex align-center justify-center">
              <span>맛</span>
              <v-rating
                v-model="postList.taste"
                color="yellow darken-3"
                background-color="grey darken-1"
                empty-icon="$ratingFull"
                hover
              ></v-rating>
              <span>({{ postList.taste }})</span>
            </v-row>

            <v-row class="d-flex align-center justify-center">
              <span>분위기</span>
              <v-rating
                v-model="postList.mood"
                color="yellow darken-3"
                background-color="grey darken-1"
                empty-icon="$ratingFull"
                hover
              ></v-rating>
              <span>({{ postList.mood }})</span>
            </v-row>

            <v-row class="d-flex align-center justify-center">
              <span>위생</span>
              <v-rating
                v-model="postList.clean"
                color="yellow darken-3"
                background-color="grey darken-1"
                empty-icon="$ratingFull"
                hover
              ></v-rating>
              <span>({{ postList.clean }})</span>
            </v-row>
            
            <v-textarea 
              label="Content" 
              v-model="postList.contents"
              id="content"
              autofocus
              :rules="[ checkContents ]"
            >
            </v-textarea>

            <v-file-input accept="image/*" label="File input" @change="onFileChange" :rules="[ checkImage ]"></v-file-input>
            <v-img v-if="url" :src="url" contain max-width="100%" max-height="300px"></v-img>
          </v-card-text>
          <div class="text-center mb-3 pb-3">
            <v-btn color="secondary" :disabled="disabled" @click="uploadImage({postList, formData})">Save</v-btn>
          </div>
        </v-card>  
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'postCreateView',

  data() {
    return {
      postList: {
        cafeno: null,
        cafename: null,
        contents: null,
        taste: 0,
        mood: 0,
        clean: 0,
        uid: null,
        image: null,
      },
      formData: new FormData(),
      url: null,
      selectedFile: null,
      disabled: true,
    }
  },

  computed: {
    ...mapState([
        'currentUser',
        'selectedCafe',
      ]),
    ...mapGetters(['isLoggedIn']),
  },

  methods: {
    ...mapActions(['uploadImage']),
    onFileChange(e) {
      if (!e) {
        this.url = null
      } else {
        this.selectedFile = e
        this.url = URL.createObjectURL(this.selectedFile)
        if (this.formData.get("image")) {
          this.formData.delete("image")
          this.formData.set("image", this.selectedFile, this.selectedFile.name)
        } else {
          this.formData.append("image", this.selectedFile, this.selectedFile.name)
        }
      }
    },
    checkContents(value) {
      if (!value) {
        return '내용을 입력해주세요.'
      } else if (this.postList.contents && this.url) {
        this.disabled = false
      }
    },
    checkImage(value) {
      if (!value) {
        return '사진을 등록해주세요.'
      } else if (this.url && this.postList.contents) {
        this.disabled = false
      }
    },
  },

  created() {
    if (!this.isLoggedIn) {
      this.$router.replace({ name: 'Login'})
    }
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