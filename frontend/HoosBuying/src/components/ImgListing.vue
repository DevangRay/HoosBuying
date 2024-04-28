<template>

<h1 v-if="images.length==0">No Images For This Listing</h1>
    <v-carousel v-if="images">
    
     
        
      <v-carousel-item v-for="image,i in images"
        :src="image['img']"
        cover
      >
      <p>{{image['image_desc']}} {{ i }}</p>
    </v-carousel-item>
    
    
    
    </v-carousel>
    
    <button class="btn" @click="fetchImagesInfo(1)">Get Image</button>
          
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
            let res= await axios.get('images/'+listing_id)
            console.log(res.data);
            this.images = res.data;
            for(let i=0;i<this.images.length;i++){
                await this.fetchImage(this.images[i]['listing_id']+'.'+this.images[i]['order'],i);
            }
                
            
        },
          
    
        async fetchImage(id,i){
            const fileReader = new FileReader()
            fileReader.addEventListener('load', () => {
                this.imageUrls.push(fileReader.result)
                console.log(fileReader.result)
            })
           ///ONLY WORKS FOR JPEG
            axios.get('images/id/'+ id).then((res=>{
                // this.imageUrls.push("data:image/jpeg;base64," + res.data)
                this.images[i]['img'] = "data:image/jpeg;base64," + res.data;
                
        }
            ))
            
          },
        },
    };
    </script>
    