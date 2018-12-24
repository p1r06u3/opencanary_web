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
            placeholder="白名单ip"
            v-model="whiteips">
            </el-input>
            <p style="font-size:12px;font-family:'PingFang SC';color:grey; margin-top: 7px;">若配置了白名单ip，则攻击来源ip为白名单ip的攻击记录将会进入后台的过滤列表。</p>

        </div>
        <br>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-tickets"></i> 白名单端口</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="form-box">
                <el-form ref="form" :model="form" label-width="80px" >

                    <el-input
                    type="textarea"
                    :rows="2"
                    placeholder="请输入内容"
                    v-model="whiteports">
                    </el-input>

                    <p style="font-size:12px;font-family:'PingFang SC';color:grey; margin-top: 7px;">若配置了白名单端口，则被攻击客户端的目的端口为白名单端口的攻击记录将不会进入后台。</p>
                    
                    <el-form-item style="float: right; margin-top:-10px;">
                        <el-button type="primary" @click="PostWhiteport" >提交配置</el-button>
                    </el-form-item>
                    <p style="font-size:12px;font-family:'PingFang SC';color:grey; margin-top: 7px;">举例：3306,3389。端口之间用英文逗号分隔。</p>

                </el-form>
            </div>
        </div>
        
    </div>



</template>

<script>

    export default {
        data() {
            return {
                url: '/whiteiplist/',
                porturl: '/whiteport/',
                whiteips: '',
                whiteports: '',
                port: '',
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
            this.getWhiteport();
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

            },
            getWhiteport() {
                // 开发环境使用 easy-mock 数据，正式环境使用 json 文件
                if (process.env.NODE_ENV === 'development') {
                    this.porturl = process.env.API_HOST+'/whiteport/';
                    this.$axios.get(this.porturl)
                    .then((res) => {
                        // console.log(res.data.user);
                        this.whiteports = res.data;
                    })
                }else{
                    this.$axios.get(this.porturl)
                    .then((res) => {
                        // console.log(res.data.user);
                        this.whiteports = res.data;
                    })
                }

            },
            PostWhiteport() {
                // 开发环境使用 easy-mock 数据，正式环境使用 json 文件
                if (process.env.NODE_ENV === 'development') {
                    this.porturl = process.env.API_HOST+'/whiteport/';
                    this.$axios.post(this.porturl,{
                        port : this.whiteports,
                    })
                    .then((res) => {
                        this.$message.success('提交成功！');
                        return this.whiteports;
                    })
                }else{
                    this.$axios.post(this.porturl,{
                        port : this.whiteports,
                    })
                    .then((res) => {
                        this.$message.success('提交成功！');
                        return this.whiteports;
                    })
                }

            }
        }
    }

    
    
</script>