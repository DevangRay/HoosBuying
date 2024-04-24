<template> 
    <p>allTags: {{ selected_Tags }}</p>
    <v-card-text class="d-flex justify-space-between">
        <v-chip-group 
        v-for="tag in tag_result" 
        :key="tag.tag_id"
        column
        multiple
        selected-class="text-primary"
        >
            <!-- <v-chip 
            v-if="tag.tag_id == 1" 
            variant="outlined"
            filter
            @click="log(tag.tag_id)"
            >
                {{ tag.tag_name }}
            </v-chip> -->

            <v-chip 
            variant="elevated"
            filter
            @click="log(tag.tag_id)"
            >
                {{ tag.tag_name }}
            </v-chip>
        </v-chip-group>
    </v-card-text>
</template>

<script>
    import axios from 'axios'
    import { mapState } from 'vuex';

    export default{
        name: 'TagsArray',
        data() {
            return {
                tag_result: [],
                all_clicked_tags: [],
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
            },
            log(tag_id) {
                console.log("pressing the fucking button")
                console.log("id is ", tag_id)
                this.$store.commit('changeTags', tag_id)
            }
        }, 
        computed: {
            ...mapState({
                selected_tags: 'selected_tags'
            })
        }
    }
</script>