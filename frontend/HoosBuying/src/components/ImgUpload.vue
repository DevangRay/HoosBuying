<template>


<v-carousel>

  <h1 v-if="imageUrls.length==0">No Images</h1>
  <v-carousel-item v-for="imageUrl,i in imageUrls"
    :src="imageUrl"
    cover
  >
    <v-btn @click= deleteImage(i)>Delete Me {{ i }}</v-btn>
    <v-btn @click= uploadImage(i)>UPLOAD {{ i }}</v-btn>
    <!-- <v-text-field></v-text-field > -->
</v-carousel-item>

</v-carousel>

<button class="btn" @click="onPickFile">Add Image</button>
        <input
            type="file"
            style="display: none"
            ref="fileInput"
            accept="image/*"
            @change="onFilePicked"/>
      
</template>

<script>

import axios from 'axios'; 


export default {
  name: "ImgUpload",
  components: {},
  data() {
    return {
      images: [],
      imageUrls: [],
    };
  },
  methods: {
      onPickFile () {
      this.$refs.fileInput.click()
      },
      onFilePicked (event) {
      const files = event.target.files

      // let filename = files[0].name
      const fileReader = new FileReader()
      fileReader.addEventListener('load', () => {
          this.imageUrls.push(fileReader.result)
      })
      fileReader.readAsDataURL(files[0])
      this.images.push(files[0])
      console.log(files[0])
      console.log(this.imageUrls.length)
      },
      deleteImage(i){
        this.images.splice(i,1);
        this.imageUrls.splice(i,1)
      },



      async uploadImage(i){
        this.images[i];
        let imgForm = new FormData()
        imgForm.append('file',this.images[i])
        await axios.post('images/upload', imgForm)
      }
    },
};
</script>
