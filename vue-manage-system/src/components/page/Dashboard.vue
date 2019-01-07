
<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="8">
                <el-row>
                    <el-col>
                        <el-card shadow="hover" class="mgb20">
                            <div class="user-info">
                                <img src="/static/img/img.jpg" class="user-avator" alt="">
                                <div class="user-info-cont">
                                    <div class="user-info-name">admin</div>
                                    <div>fighting~</div>
                                </div>
                            </div>
                            <!-- <div class="user-info-list">上次登录时间：<span>2018-01-01</span></div> -->
                            <!-- <div class="user-info-list">上次登录地点：<span>东莞</span></div> -->
                        </el-card>
                        <!-- 饼图 -->
                        <div style="background:white; height: 335px;">
                            <v-chart :forceFit="true" :height="height" :data="data" :scale="scale">
                            <v-tooltip :showTitle="false" dataKey="item*percent" />
                            <v-axis />
                            <v-legend dataKey="item" />
                            <v-pie
                                position="percent"
                                color="item"
                                :vStyle="pieStyle"
                                :label="labelConfig"
                            />
                            <v-coord type="theta" />
                            </v-chart>
                        </div>
                        <!-- 饼图 end-->
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="16">
                <div style="background:white; ">
                    <!-- 折线图 -->
                    <v-chart :forceFit="true" :height="heightz" :data="dataz" :scale="scalez">
                    <v-tooltip />
                    <v-axis />
                    <v-legend />
                    <v-smooth-line position="month*attacknum" color="city" shape="smooth" />
                    <v-point position="month*attacknum" color="city" shape="circle" />
                    </v-chart>
                     <!-- 折线图 end-->
                </div>
            </el-col>
        </el-row>
    </div>
</template>



//折线图
<script>
    import Vue from 'vue';
    import axios from 'axios';
    Vue.prototype.$axios = axios;
    const DataSetz = require('@antv/data-set');

export default {
    data: function(){
        return {
            urlline: '/chart?line',
            urlpie: '/chart/',
        //折线图数据部分
            sourceDataz:'',
            dvz:'',
            dataz:'',
            scalez:'',
            heightz: 553,

        // 饼图数据部分
            sourceData:'',
            data: '',
            scale: '',
            dv: '',
            height: 350,
            pieStyle: {
            stroke: "#fff",
            lineWidth: 1
            },

            labelConfig: ['percent', {
            offset: -40,
            textStyle: {
                rotate: 0,
                textAlign: 'center',
                shadowBlur: 2,
                shadowColor: 'rgba(0, 0, 0, .45)'
            }
            }],
        };
    },

    created() {
        this.getLineData();
        this.getPieData();
    },
    methods: {

        // 获取 easy-mock 的模拟数据
        getLineData() {
            // 开发环境使用 easy-mock 数据，正式环境使用 json 文件
            if (process.env.NODE_ENV === 'development') {
                this.urlline = process.env.API_HOST+'/chart?line';
                axios.get(this.urlline)
                .then((res) => {
                    // 折线图
                    this.sourceDataz = res.data;
                    this.dvz = new DataSetz.View().source(res.data);
                    this.dvz.transform({
                    type: 'fold',
                    fields: ['attack', 'white'],
                    key: 'city',
                    value: 'attacknum',
                    });
                    this.dataz = this.dvz.rows;

                    this.scalez = [{
                    dataKey: 'month',
                    min: 0,
                    max: 1,
                    }];
                })
            }else{
                this.$axios.get(this.urlline)
                .then((res) => {
                    // 折线图
                    this.sourceDataz = res.data;
                    this.dvz = new DataSetz.View().source(res.data);
                    this.dvz.transform({
                    type: 'fold',
                    fields: ['attack', 'white'],
                    key: 'city',
                    value: 'attacknum',
                    });
                    this.dataz = this.dvz.rows;

                    this.scalez = [{
                    dataKey: 'month',
                    min: 0,
                    max: 1,
                    }];
                })
            }

        },
        getPieData() {
            // 开发环境使用 easy-mock 数据，正式环境使用 json 文件
            if (process.env.NODE_ENV === 'development') {
                this.urlpie = process.env.API_HOST+'/chart/';
                axios.get(this.urlpie)
                .then((res) => {

                    // 饼图
                    this.sourceData = res.data;
                    // this.sourceData = [{"count": 1, "item": "mssql"}, {"count": 1, "item": "snmp"}, {"count": 6, "item": "sip"},{"count": 6, "item": "rdp"},{"count": 3, "item": "vnc"},{"count": 6, "item": "tcpbanner"},{"count": 3, "item": "redis"},{"count": 3, "item": "ntp"},{"count": 2, "item": "git"},{"count": 1, "item": "ftp"}, {"count": 0, "item": "http"}, {"count": 0, "item": "ssh"}, {"count": 0, "item": "telnet"}, {"count": 0, "item": "portscan"}, {"count": 0, "item": "mysql"}];
                    // console.log(this.sourceData);
                    this.scale = [{
                      dataKey: 'percent',
                      min: 0,
                      formatter: '.0%',
                    }];
                    this.dv = new DataSetz.View().source(this.sourceData);
                    this.dv.transform({
                      type: 'percent',
                      field: 'count',
                      dimension: 'item',
                      as: 'percent'
                    });
                    this.data = this.dv.rows;
                    // console.log(this.data);
                })
            }else{
                this.$axios.get(this.urlpie)
                .then((res) => {
                    // 饼图
                    this.sourceData = res.data;
                    this.scale = [{
                      dataKey: 'percent',
                      min: 0,
                      formatter: '.0%',
                    }];
                    this.dv = new DataSetz.View().source(this.sourceData);
                    this.dv.transform({
                      type: 'percent',
                      field: 'count',
                      dimension: 'item',
                      as: 'percent'
                    });
                    this.data = this.dv.rows;

                })
            }

        },

    }

};
</script>


<style scoped>
    .el-row {
        margin-bottom: 20px;
    }

    .grid-content {
        display: flex;
        align-items: center;
        height: 100px;
    }

    .grid-cont-right {
        flex: 1;
        text-align: center;
        font-size: 12px;
        color: #999;
    }

    .grid-num {
        font-size: 30px;
        font-weight: bold;
    }

    .grid-con-icon {
        font-size: 50px;
        width: 100px;
        height: 100px;
        text-align: center;
        line-height: 100px;
        color: #fff;
    }

    .grid-con-1 .grid-con-icon {
        background: rgb(45, 140, 240);
    }

    .grid-con-1 .grid-num {
        color: rgb(45, 140, 240);
    }

    .grid-con-2 .grid-con-icon {
        background: rgb(100, 213, 114);
    }

    .grid-con-2 .grid-num {
        color: rgb(45, 140, 240);
    }

    .grid-con-3 .grid-con-icon {
        background: rgb(242, 94, 67);
    }

    .grid-con-3 .grid-num {
        color: rgb(242, 94, 67);
    }

    .user-info {
        display: flex;
        align-items: center;
        padding-bottom: 20px;
        border-bottom: 2px solid #ccc;
        margin-bottom: 20px;
    }

    .user-avator {
        width: 120px;
        height: 120px;
        border-radius: 50%;
    }

    .user-info-cont {
        padding-left: 50px;
        flex: 1;
        font-size: 14px;
        color: #999;
    }

    .user-info-cont div:first-child {
        font-size: 30px;
        color: #222;
    }

    .user-info-list {
        font-size: 14px;
        color: #999;
        line-height: 25px;
    }

    .user-info-list span {
        margin-left: 70px;
    }

    .mgb20 {
        margin-bottom: 20px;
    }

    .todo-item {
        font-size: 14px;
    }

    .todo-item-del {
        text-decoration: line-through;
        color: #999;
    }

</style>
