<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-date"></i> 邮件配置</el-breadcrumb-item>
                <el-breadcrumb-item>告警邮件</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="form-box">
                <el-form ref="form" :model="form" label-width="80px">
                    <el-form-item label="邮件列表">
                        <el-input type="textarea" rows="5" v-model="email">
                        </el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="methodInput">提交配置</el-button>

                    </el-form-item>
                </el-form>
            </div>

        </div>

    </div>
</template>

<script>

    export default {
        name: 'baseform',
        data() {
            return {
                url: '/mail/',
                email: '',
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
                    this.url = process.env.API_HOST+'/mail/';
                    this.$axios.get(this.url)
                    .then((res) => {
                        // console.log(res.data.user);
                        this.email = res.data.user;
                    })
                }else{
                    this.$axios.get(this.url)
                    .then((res) => {
                        // console.log(res.data.user);
                        this.email = res.data.user;
                    })
                }

            },
            methodInput() {
                // 开发环境使用 easy-mock 数据，正式环境使用 json 文件
                if (process.env.NODE_ENV === 'development') {
                    this.url = process.env.API_HOST+'/mail/';
                    this.$axios.post(this.url,{
                        user : this.email,
                    })
                    .then((res) => {
                        this.$message.success('提交成功！');
                        return this.email;
                    })
                } else{
                    this.$axios.post(this.url,{
                        user : this.email,
                    })
                    .then((res) => {
                        this.$message.success('提交成功！');
                        return this.email;
                    })
                }

            }
        }
    }

    
    
</script>