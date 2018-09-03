<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-tickets"></i> 白名单ip</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <el-input
            type="textarea"
            :rows="2"
            placeholder="请输入内容"
            v-model="whiteips">
            </el-input>
        </div>
    </div>
</template>

<script>

    export default {
        data() {
            return {
                url: './whiteiplist/',
                whiteips: '',
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: true,
                    type: ['步步高'],
                    resource: '小天才',
                    desc: '',
                    options: []
                }
            }
        },
        created() {
            this.getData();
        },
        methods: {

            // 获取 easy-mock 的模拟数据
            getData() {
                // 开发环境使用 easy-mock 数据，正式环境使用 json 文件
                if (process.env.NODE_ENV === 'development') {
                    this.url = process.env.API_HOST+'/whiteiplist/';
                    this.$axios.get(this.url)
                    .then((res) => {
                        // console.log(res.data.user);
                        this.whiteips = res.data;
                    })
                }else{
                    this.$axios.get(this.url)
                    .then((res) => {
                        // console.log(res.data.user);
                        this.whiteips = res.data;
                    })
                }

            }
        }
    }

    
    
</script>