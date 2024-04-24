<template> 
    <div v-for="selected_tag in all_clicked_tags" :key="selected_tag[0]">
        <p>{{ selected_tag }}</p>
    </div>
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
            @click="change_selected_tag(tag.tag_id)"
            >
                {{ tag.tag_name }}
            </v-chip>
        </v-chip-group>
    </v-card-text>
</template>

<script>
    import store from '@/stores';
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
                console.log("TAG DATA IS", res.data)
                this.tag_result = res.data;
                // console.log("RESULT SHOULD BE THE SAME", this.result);
                })
            },
        change_selected_tag(tag_id) {
                store.dispatch('callChangeTags', tag_id)
                this.get_selected_tags()
            },
        get_selected_tags() {            
                store.dispatch('callTagGetter')
                .then((res) => {
                    this.all_clicked_tags = res;
                })
            },
        }
    }
</script>