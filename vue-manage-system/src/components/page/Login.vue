<template>
    <div class="login-wrap">
        <div class="ms-title">后台管理系统</div>
        <div class="ms-login">
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px" class="demo-ruleForm">
                <el-form-item prop="username">
                    <el-input v-model="ruleForm.username" placeholder="username"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" placeholder="password" v-model="ruleForm.password" @keyup.enter.native="submitForm('ruleForm')"></el-input>
                </el-form-item>
                <div class="login-btn">
                    <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
                </div>
                <!-- <p style="font-size:12px;line-height:30px;color:#999;">Tips : 用户名和密码随便填。</p> -->
            </el-form>
        </div>
    </div>
</template>

<script>
    export default {
        data: function(){
            return {
                url: '/auth/',
                restoken: '',
                role: '',
                loginres: '',
                ruleForm: {
                    username: '',
                    password: ''
                },
                rules: {
                    username: [
                        { required: true, message: '请输入用户名', trigger: 'blur' }
                    ],
                    password: [
                        { required: true, message: '请输入密码', trigger: 'blur' }
                    ]
                }
            }
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        if (process.env.NODE_ENV === 'development') {
                            this.url = process.env.API_HOST+'/auth/';
                            this.$axios.post(this.url, {
                                username: this.ruleForm.username,
                                password: this.ruleForm.password
                            }).then((res) => {
                                // console.log('subumit login start')
                                this.restoken = res.data.token;
                                this.loginres = res.data.result;
                                this.role = res.data.role;
                                if (this.loginres){
                                    localStorage.setItem('token', this.restoken);
                                    localStorage.setItem('role', this.role);
                                    this.$router.push('/');
                                } else{
                                    this.$router.push('/login')
                                }

                                // console.log(this.restoken);
                            })

                        } else{
                                this.url = '/auth/';
                                this.$axios.post(this.url, {
                                    username: this.ruleForm.username,
                                    password: this.ruleForm.password
                                }).then((res) => {
                                    // console.log('subumit login start')
                                    this.restoken = res.data.token;
                                    this.loginres = res.data.result;
                                    this.role = res.data.role;
                                    if (this.loginres){
                                        localStorage.setItem('token', this.restoken);
                                        localStorage.setItem('role', this.role);
                                        this.$router.push('/');
                                    } else{
                                        this.$router.push('/login')
                                    }
                                    // console.log(this.restoken);
                                })

                            }

                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            }
        }
    }
</script>

<style scoped>
    .login-wrap{
        position: relative;
        width:100%;
        height:100%;
    }
    .ms-title{
        position: absolute;
        top:50%;
        width:100%;
        margin-top: -230px;
        text-align: center;
        font-size:30px;
        color: #fff;

    }
    .ms-login{
        position: absolute;
        left:50%;
        top:50%;
        width:300px;
        height:160px;
        margin:-150px 0 0 -190px;
        padding:40px;
        border-radius: 5px;
        background: #fff;
    }
    .login-btn{
        text-align: center;
    }
    .login-btn button{
        width:100%;
        height:36px;
    }
</style>