<template>
    <div v-for="tag in tag_result" :key="tag.tag_id">
        <p>{{ tag.tag_name }}</p>
    </div>
    <v-card-text class="d-flex justify-space-between">
        <v-chip-group 
        v-for="tag in tag_result" 
        :key="tag.tag_id"
        column
        multiple
        selected-class="text-primary"
        >
            <v-chip 
            v-if="tag.tag_id == 1" 
            variant="outlined"
            filter
            >
                {{ tag.tag_name }}
            </v-chip>

            <v-chip 
            v-else 
            variant="elevated"
            filter
            >
                {{ tag.tag_name }}
            </v-chip>
        </v-chip-group>
    </v-card-text>
</template>

<script>
    import axios from 'axios'
    export default{
        name: 'TagsArray',
        data() {
            return {
                tag_result: [],
            };
        },
        props: {
            msg: String
        },
        mounted() {
            this.getTags();
        },
        methods: {
        getTags() {
            const headers = {
                "Access-Control-Allow-Origin":"*",
                "Content-Type": "application/jsonp"
            }
            const url = "http://127.0.0.1:5000/tags/"
            axios.get(url, {headers})

            .then((res) => {
                // console.log("RESULT FOUND ", res);
                console.log("DATA IS", res.data)
                this.tag_result = res.data;
                // console.log("RESULT SHOULD BE THE SAME", this.result);
                })
            }
        }
    }
</script>