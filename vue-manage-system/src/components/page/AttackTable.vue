<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-tickets"></i> 攻击列表</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <!-- <div class="handle-box">
                <el-button type="primary" icon="delete" class="handle-del mr10" @click="delAll">批量删除</el-button> -->
                <!-- <el-select v-model="select_cate" placeholder="筛选省份" class="handle-select mr10">
                    <el-option key="1" label="广东省" value="广东省"></el-option>
                    <el-option key="2" label="湖南省" value="湖南省"></el-option>
                </el-select>
                <el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>
                <el-button type="primary" icon="search" @click="search">搜索</el-button> -->
            <!-- </div> -->
            <!-- <el-table :data="data" border style="width: 100%" ref="multipleTable" @selection-change="handleSelectionChange">
                <el-table-column type="selection" width="55"></el-table-column>
                <el-table-column prop="local_time" label="攻击时间">
                </el-table-column>
                <el-table-column prop="src_host" label="攻击来源">
                </el-table-column>
                <el-table-column prop="dst_host" label="目标主机">
                </el-table-column>
                <el-table-column prop="dst_port" label="目的端口">
                </el-table-column>
                <el-table-column prop="logtype" label="日志类型">
                </el-table-column>
                <el-table-column label="操作" width="180">
                    <template slot-scope="scope">
                        <el-button size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                        <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                    </template>
                </el-table-column>
            </el-table> -->

  <el-table
    :data="data"
    style="width: 100%"
    :default-sort = "{prop: 'local_time', order: 'descending'}"
    >
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item v-if="props.row.hostname" label="HOSTNAME: ">
            <span>{{ props.row.hostname }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.username" label="USERNAME: ">
            <span>{{ props.row.username }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.password" label="PASSWORD: ">
            <span>{{ props.row.password }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.path" label="PATH: ">
            <span>{{ props.row.path }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.useragent" label="USERAGENT: ">
            <span>{{ props.row.useragent }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.session" label="SESSION: ">
            <span>{{ props.row.session }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.localversion" label="LOCALVERSION: ">
            <span>{{ props.row.localversion }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.remoteversion" label="REMOTEVERSION: ">
            <span>{{ props.row.remoteversion }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.inin" label="IN: ">
            <span>{{ props.row.inin }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.mac" label="MAC: ">
            <span>{{ props.row.mac }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.proto" label="PROTO: ">
            <span>{{ props.row.proto }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.ttl" label="TTL: ">
            <span>{{ props.row.ttl }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.window" label="WINDOW: ">
            <span>{{ props.row.window }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.repo" label="REPO: ">
            <span>{{ props.row.repo }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.ntp_cmd" label="NTP CMD: ">
            <span>{{ props.row.ntp_cmd }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.args" label="ARGS: ">
            <span>{{ props.row.args }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.cmd" label="CMD: ">
            <span>{{ props.row.cmd }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.banner_id" label="BANNER_ID: ">
            <span>{{ props.row.banner_id }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.function" label="FUNCTION: ">
            <span>{{ props.row.function }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.vnc_client_response" label="VNC Client Response: ">
            <span>{{ props.row.vnc_client_response }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.vnc_password" label="VNC Password: ">
            <span>{{ props.row.vnc_password }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.vnc_server_challenge" label="VNC Server Challenge: ">
            <span>{{ props.row.vnc_server_challenge }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.inputs" label="INPUT: ">
            <span>{{ props.row.inputs }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.domain" label="DOMAIN: ">
            <span>{{ props.row.domain }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.headers_call_id" label="call-id: ">
            <span>{{ props.row.headers_call_id }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.headers_content_length" label="content-length: ">
            <span>{{ props.row.headers_content_length }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.headers_cseq" label="cseq: ">
            <span>{{ props.row.headers_cseq }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.headers_from" label="from: ">
            <span>{{ props.row.headers_from }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.headers_to" label="to: ">
            <span>{{ props.row.headers_to }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.headers_via" label="via: ">
            <span>{{ props.row.headers_via }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.community_string" label="COMMUNITY_STRING: ">
            <span>{{ props.row.community_string }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.requests" label="REQUESTS: ">
            <span>{{ props.row.requests }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.urg" label="URG: ">
            <span>{{ props.row.urg }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.psh" label="PSH: ">
            <span>{{ props.row.psh }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.fin" label="FIN: ">
            <span>{{ props.row.fin }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.appname" label="AppName: ">
            <span>{{ props.row.appname }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.cltintname" label="CltIntName: ">
            <span>{{ props.row.cltintname }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.database" label="Database: ">
            <span>{{ props.row.database }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.language" label="Language: ">
            <span>{{ props.row.language }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.servername" label="ServerName: ">
            <span>{{ props.row.servername }}</span>
          </el-form-item>
          <el-form-item v-if="props.row.domainname" label="DOMAINNAME: ">
            <span>{{ props.row.domainname }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      label="攻击时间"
      prop="local_time"
      sortable
      >
    </el-table-column>
    <el-table-column
      label="攻击来源"
      prop="src_host"
      sortable
      >
    </el-table-column>
    <el-table-column
      label="来源端口"
      prop="src_port"
      sortable
      >
    </el-table-column>
    <el-table-column
      label="攻击类型"
      prop="logtype"
      sortable
      >
    </el-table-column>
    <el-table-column
      label="探针节点"
      prop="node_id"
      sortable
      >
    </el-table-column>
    <el-table-column
      label="目标主机"
      prop="dst_host"
      sortable
      >
    </el-table-column>
    <el-table-column
      label="目标端口"
      prop="dst_port"
      sortable
      >
    </el-table-column>
    <!-- <el-table-column label="操作" width="180">
        <template slot-scope="scope">
            <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
    </el-table-column> -->
  </el-table>

            <div class="pagination">
                <el-pagination @current-change="handleCurrentChange" layout="prev, pager, next" :total="totalData">
                </el-pagination>
            </div>
        </div>

        <!-- 
        <el-dialog title="编辑" :visible.sync="editVisible" width="30%">
            <el-form ref="form" :model="form" label-width="50px">
                <el-form-item label="日期">
                    <el-date-picker type="date" placeholder="选择日期" v-model="form.date" value-format="yyyy-MM-dd" style="width: 100%;"></el-date-picker>
                </el-form-item>
                <el-form-item label="姓名">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="地址">
                    <el-input v-model="form.address"></el-input>
                </el-form-item>

            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="editVisible = false">取 消</el-button>
                <el-button type="primary" @click="saveEdit">确 定</el-button>
            </span>
        </el-dialog>
        编辑弹出框 -->

        <!-- 删除提示框 -->
        <el-dialog title="提示" :visible.sync="delVisible" width="300px" center>
            <div class="del-dialog-cnt">删除不可恢复，是否确定删除？</div>
            <span slot="footer" class="dialog-footer">
                <el-button @click="delVisible = false">取 消</el-button>
                <el-button type="primary" @click="deleteRow">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: 'basetable',
        data() {
            return {
                url: '/log/list/',
                purl: '/log/list?type=2',
                tableData: [],
                totalData: 0,
                cur_page: 1,
                multipleSelection: [],
                select_cate: '',
                select_word: '',
                del_list: [],
                is_search: false,
                editVisible: false,
                delVisible: false,
                form: {
                    name: '',
                    date: '',
                    address: ''
                },
                idx: -1
            }
        },
        created() {
            this.getData();
            this.getTotal();
        },
        computed: {
            data() {
                return this.tableData.filter((d) => {
                    let is_del = false;
                    for (let i = 0; i < this.del_list.length; i++) {
                        if (d.name === this.del_list[i].name) {
                            is_del = true;
                            break;
                        }
                    }
                    if (!is_del) {
                        if (d.local_time.indexOf(this.select_cate) > -1 &&
                            (d.dst_host.indexOf(this.select_word) > -1 ||
                                d.dst_port.indexOf(this.select_word) > -1)
                        ) {
                            return d;
                        }
                    }
                })
            }
        },
        methods: {
            // 分页导航
            handleCurrentChange(val) {
                this.cur_page = val;
                this.getData();
            },
            // 获取 easy-mock 的模拟数据
            getData() {
                // 开发环境使用 easy-mock 数据，正式环境使用 json 文件
                if (process.env.NODE_ENV === 'development') {
                    this.url = process.env.API_HOST+'/log/list/';
                };
                this.$axios.post(this.url, {
                    page: this.cur_page
                }).then((res) => {
                    this.tableData = res.data.list;
                })
            },
            getTotal() {
                // 开发环境使用 easy-mock 数据，正式环境使用 json 文件
                if (process.env.NODE_ENV === 'development') {
                    this.url = process.env.API_HOST+'/log/list?type=2';
                    this.$axios.get(this.url)
                    .then((res) => {
                        // console.log(res.data);
                        this.totalData = res.data;
                    })
                }else{
                    this.$axios.get(this.purl)
                    .then((res) => {
                        // console.log(res.data);
                        this.totalData = res.data;
                    })
                }

            },
            search() {
                this.is_search = true;
            },
            // formatter(row, column) {
            //     return row.local_time;
            // },
            filterTag(value, row) {
                return row.tag === value;
            },
            handleEdit(index, row) {
                this.idx = index;
                const item = this.tableData[index];
                this.form = {
                    name: item.name,
                    date: item.date,
                    address: item.address
                }
                this.editVisible = true;
            },
            handleDelete(index, row) {
                this.idx = index;
                this.delVisible = true;
            },
            delAll() {
                const length = this.multipleSelection.length;
                let str = '';
                this.del_list = this.del_list.concat(this.multipleSelection);
                for (let i = 0; i < length; i++) {
                    str += this.multipleSelection[i].name + ' ';
                }
                this.$message.error('删除了' + str);
                this.multipleSelection = [];
            },
            handleSelectionChange(val) {
                this.multipleSelection = val;
            },
            // 保存编辑
            saveEdit() {
                this.$set(this.tableData, this.idx, this.form);
                this.editVisible = false;
                this.$message.success(`修改第 ${this.idx+1} 行成功`);
            },
            // 确定删除
            deleteRow(){
                this.tableData.splice(this.idx, 1);
                this.$message.success('删除成功');
                this.delVisible = false;
            }
        }
    }

</script>

<style scoped>
    .handle-box {
        margin-bottom: 20px;
    }

    .handle-select {
        width: 120px;
    }

    .handle-input {
        width: 300px;
        display: inline-block;
    }
    .del-dialog-cnt{
        font-size: 16px;
        text-align: center
    }
</style>
