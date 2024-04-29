<template>


<v-carousel v-model="currIndex">

  <h1 v-if="imageUrls.length==0">No Images</h1>
  <v-carousel-item v-for="imageUrl,i in imageUrls"
    :src="imageUrl"
    ref = "curImage"
    :key = "i" 
    cover
  >
    
    <!-- <v-text-field></v-text-field > -->
</v-carousel-item>

</v-carousel>

<v-btn color ='red' v-if="currIndex>=0 && imageUrls.length!=0" @click= deleteImage(i)>Delete Image #{{ currIndex+1}}</v-btn>
<!-- <v-btn v-if="imageUrls.length!=0" @click= uploadImage(i)>UPLOAD {{ currIndex}}</v-btn> -->


<v-btn class="btn" @click="onPickFile">Add Image(.jpg Only!!)</v-btn>
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
      currIndex: null,
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
      // console.log(files[0])
      // console.log(this.imageUrls.length)
      this.curImage++;
      },
      deleteImage(i){
        this.images.splice(i,1);
        this.imageUrls.splice(i,1)
      },

      async uploadImages(listing_id){
        // console.log("UPLOADING IMAGES to " + listing_id)
        for(let i=0;i<this.images.length;i++) {
          // console.log("IMAGE " + i + "uploading")
          let imgForm = new FormData()
          imgForm.append('file',this.images[i])
          imgForm.append('listing_id',listing_id)
          imgForm.append('order',i)
          await axios.post('images/upload', imgForm)
        }
      },
    },
};
</script>
