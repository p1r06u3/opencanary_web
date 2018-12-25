<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-date"></i> 主机状态</el-breadcrumb-item>
                <!-- <el-breadcrumb-item>主机状态</el-breadcrumb-item> -->
            </el-breadcrumb>
        </div>
        <div class="container" >
            <el-table :data="tableData" style="width: 100%">
                <el-table-column prop="date" label="最后在线" sortable width="280" >
                </el-table-column>
                <el-table-column prop="name" label="主机名" width="280">
                </el-table-column>
                <el-table-column prop="address" label="ip地址" width="280" :formatter="formatter">
                </el-table-column>
                <el-table-column prop="tag" label="是否在线" :filters="[{ text: 'online', value: 'online' }, { text: 'offline', value: 'offline' }]" :filter-method="filterTag" filter-placement="bottom-end">
                <template slot-scope="scope">
                    <el-tag :type="scope.row.tag === 'online' ? 'success' : 'info'" disable-transitions>{{scope.row.tag}}</el-tag>
                </template>
                </el-table-column>
            </el-table>
        </div>

    </div>
</template>

<script>

    export default {
        name: 'baseform',
        data() {
            return {
                url: '/gethost/',
                tableData:[]
                // tableData: [{
                //     date: '2018-10-30 12:20:25',
                //     name: 'yf-fsp-sec-honeypot05',
                //     address: '10.10.10.10',
                //     tag: 'online'
                // }, {
                //     date: '2018-10-30 12:20:21',
                //     name: 'yf-fsp-sec-honeypot03',
                //     address: '10.1.1.1',
                //     tag: 'offline'
                // }, {
                //     date: '2018-10-29 00:20:25',
                //     name: 'yf-fsp-sec-honeypot01',
                //     address: '222.222.222.222',
                //     tag: 'online'
                // }, {
                //     date: '2018-9-30 09:20:25',
                //     name: 'yf-fsp-sec-honeypot02',
                //     address: '192.168.1.1',
                //     tag: 'offline'
                // }
                // ]
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
                    this.url = process.env.API_HOST+'/gethost/';
                    this.$axios.get(this.url)
                    .then((res) => {
                        // console.log(res.data.list);
                        this.tableData = res.data.list;
                    })
                }else{
                    this.$axios.get(this.url)
                    .then((res) => {
                        // console.log(res.data);
                        this.tableData = res.data.list;
                    })
                }

            },
            formatter(row, column) {
                return row.address;
            },
            filterTag(value, row) {
                return row.tag === value;
            },
            filterHandler(value, row, column) {
                const property = column['property'];
                return row[property] === value;
            }
            // methodInput() {
            //     // 开发环境使用 easy-mock 数据，正式环境使用 json 文件
            //     if (process.env.NODE_ENV === 'development') {
            //         this.url = process.env.API_HOST+'/mail/';
            //         this.$axios.post(this.url,{
            //             user : this.email,
            //         })
            //         .then((res) => {
            //             this.$message.success('提交成功！');
            //             return this.email;
            //         })
            //     } else{
            //         this.$axios.post(this.url,{
            //             user : this.email,
            //         })
            //         .then((res) => {
            //             this.$message.success('提交成功！');
            //             return this.email;
            //         })
            //     }

            // }
        }
    }

    
    
</script>