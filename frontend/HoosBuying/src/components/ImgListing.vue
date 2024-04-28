<template>

<h1 v-if="imageUrls.length==0">No Images For This Listing</h1>
    <v-carousel v-if="images">
    
     
        
      <v-carousel-item v-for="imageUrl,i in imageUrls"
        :src="imageUrl"
        cover
      >
      <p>DESCRIPTION {{ i }}</p>
    </v-carousel-item>
    
    
    
    </v-carousel>
    
    <button class="btn" @click="fetchImage(1)">Get Image</button>
          
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
          

        async fetchImagesInfo(listing_id){

        },
          
    
        async fetchImage(id){
            const fileReader = new FileReader()
            fileReader.addEventListener('load', () => {
                this.imageUrls.push(fileReader.result)
                console.log(fileReader.result)
            })
           ///ONLY WORKS FOR JPEG
            axios.get('images/id/'+ id).then((res=>{
                this.imageUrls.push("data:image/jpeg;base64," + res.data)
                console.log(res.data)
        }
            ))
            
          },
        },
    };
    </script>
    