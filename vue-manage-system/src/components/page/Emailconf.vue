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
                    <!-- <el-form-item label="表单名称">
                        <el-input v-model="form.name"></el-input>
                    </el-form-item> -->
                    <!-- <el-form-item label="选择器">
                        <el-select v-model="form.region" placeholder="请选择">
                            <el-option key="bbk" label="步步高" value="bbk"></el-option>
                            <el-option key="xtc" label="小天才" value="xtc"></el-option>
                            <el-option key="imoo" label="imoo" value="imoo"></el-option>
                        </el-select>
                    </el-form-item> -->
                    <!-- <el-form-item label="日期时间">
                        <el-col :span="11">
                            <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
                        </el-col>
                        <el-col class="line" :span="2">-</el-col>
                        <el-col :span="11">
                            <el-time-picker placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
                        </el-col>
                    </el-form-item> -->
                    <!-- <el-form-item label="城市级联">
                        <el-cascader :options="options" v-model="form.options"></el-cascader>
                    </el-form-item> -->
                    <!-- <el-form-item label="选择开关">
                        <el-switch v-model="form.delivery"></el-switch>
                    </el-form-item> -->
                    <!-- <el-form-item label="多选框">
                        <el-checkbox-group v-model="form.type">
                            <el-checkbox label="步步高" name="type"></el-checkbox>
                            <el-checkbox label="小天才" name="type"></el-checkbox>
                            <el-checkbox label="imoo" name="type"></el-checkbox>
                        </el-checkbox-group>
                    </el-form-item>
                    <el-form-item label="单选框">
                        <el-radio-group v-model="form.resource">
                            <el-radio label="步步高"></el-radio>
                            <el-radio label="小天才"></el-radio>
                            <el-radio label="imoo"></el-radio>
                        </el-radio-group>
                    </el-form-item> -->

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
                url: './mail/',
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