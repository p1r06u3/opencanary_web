import Vue from 'vue';
import App from './App';
import router from './router';
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';    // 默认主题
// import '../static/css/theme-green/index.css';       // 浅绿色主题
import './assets/icon/iconfont.css'                 //蚂蚁icon
import "babel-polyfill";
import Viser from 'viser-vue'

Vue.use(ElementUI, { size: 'small' });
Vue.prototype.$axios = axios;

//使用钩子函数对路由进行权限跳转
router.beforeEach((to, from, next) => {
    // const role = localStorage.getItem('role');
    this.JWT_TOKEN = localStorage.getItem('token');
    // http request 拦截器 给header添加Authorization

    axios.interceptors.request.use(
        config =>{
            if (this.JWT_TOKEN){
                // JWT_TOKEN = localStorage.getItem('token');
                config.headers.Authorization = `opencanary ${this.JWT_TOKEN}`;   
            }
        return config;
    }, error => {
        return Promise.reject(error)
    })

    axios.interceptors.response.use(
        response => {
            return response;
        },
        error => {
            if (error.response) {
                switch (error.response.status) {
                    case 401:
                        // 返回 401 清除token信息并跳转到登录页面
                        window.localStorage.clear();
                        next('/login');
                        router.replace({
                            path: '/login',
                            query: {redirect: router.currentRoute.fullPath}
                        })
                }
            }
            return Promise.reject(error.response.data)   // 返回接口返回的错误信息
        });





    if(!this.JWT_TOKEN && to.path !== '/login'){
        // 未认证且路由不是login
        next('/login')
    }else if(this.JWT_TOKEN && to.path =='/login'){
        // 有认证头但路由是login
        window.localStorage.clear();
        next()
    }else{
        // 简单的判断IE10及以下不进入富文本编辑器，该组件不兼容
        if(navigator.userAgent.indexOf('MSIE') > -1 && to.path === '/editor'){
            Vue.prototype.$alert('vue-quill-editor组件不兼容IE10及以下浏览器，请使用更高版本的浏览器查看', '浏览器不兼容通知', {
                confirmButtonText: '确定'
            });
        }else{
            next();
        }
    }
})

new Vue({
    router,
    render: h => h(App)
}).$mount('#app');

Vue.use(Viser)