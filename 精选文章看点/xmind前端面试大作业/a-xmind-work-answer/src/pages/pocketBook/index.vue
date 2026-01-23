<template>
  <div v-loading="loading">
    <h5>记账本</h5>
    <el-form @keyup.enter.native="onSearch" inline label-width="100px" class="search">
      <el-form-item label="账单月份">
        <el-select v-model="searchTime" placeholder="请选择" clearable>
          <el-option
            v-for="item in 12"
            :key="item"
            :label="item + '月'"
            :value="item">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="账单分类">
        <el-select v-model="searchCategory" placeholder="请选择账单分类" clearable>
          <el-option
            v-for="item in categories"
            :key="item.id"
            :label="item.name"
            :value="item.id">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="dialogVisible = true">新增</el-button>
        <el-button type="default" @click="onSearch">查询</el-button>
      </el-form-item>
    </el-form>

    <div class="content">
      <el-row class="count" v-if="showCount && searchTime">
        <el-col :span="5">
          {{searchTime}}月收入：<span>{{totalIncome}}</span>
        </el-col>
        <el-col :span="5">
          {{searchTime}}月支出：<span>{{totalExpenditure}}</span>
        </el-col>
      </el-row>

      <el-table
        :data="tableData"
        stripe
        border
        size="small"
        :show-summary="searchCategory ? true : false"
        style="width: 800%">
        <el-table-column label="账单时间">
          <template slot-scope="scope">
            {{fromTime(Number(scope.row.time))}}
          </template>
        </el-table-column>
        <el-table-column label="账单类型">
          <template slot-scope="scope">
            {{['支出', '收入'][Number(scope.row.type)]}}
          </template>
        </el-table-column>
        <el-table-column label="账单分类">
           <template slot-scope="scope">
            {{writeCategory(scope.row)}}
          </template>
        </el-table-column>
        <el-table-column prop="amount" label="账单金额（￥）">
          <template slot-scope="scope">
            {{ Math.floor(scope.row.amount * 100) / 100}}
          </template>
        </el-table-column>
      </el-table>
    </div>

    <el-dialog
      title="新增账单"
      :visible.sync="dialogVisible"
      width="40%"
      @close="handleClose">
      <el-form
        :model="form"
        ref="form"
        label-width="110px"
        @keyup.enter.native="onSumbit"
      >
        <el-form-item prop="type" label="账单类型" :rules="[{ required: true, message: '请选择账单类型', trigger: 'blur' }]">
          <el-radio-group v-model="form.type">
            <el-radio :label="0">支出</el-radio>
            <el-radio :label="1">收入</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item prop="category" label="账单分类" :rules="[{ required: true, message: '请选择账单分类', trigger: 'blur' }]">
          <el-select v-model="form.category" placeholder="请选择账单分类">
            <el-option
              v-for="item in categories"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item prop="amount" label="账单金额" :rules="[{ required: true, message: '请输入账单金额', trigger: 'blur' }]">
          <el-input-number v-model="form.amount" :precision="2" :min="0" placeholder="请输入账单金额"></el-input-number>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSumbit">确定</el-button>
          <el-button type="default" @click="dialogVisible = false">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  data () {
    return {
      categories: require('../../assets/json/categories.json'),
      bills: require('../../assets/json/bill.json'),
      loading: false,
      tableData: [],
      searchTime: '',
      dialogVisible: false,
      form: {
        type: '',
        category: '',
        amount: 0
      },
      totalIncome: 0,
      totalExpenditure: 0,
      showCount: false,
      searchCategory: ''
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.loading = true
      this.tableData = this.bills
      this.showCount = false
      const timer = setTimeout(() => {
        this.loading = false
        clearTimeout(timer)
      }, 500)
    },
    onSearch () {
      if (this.searchTime && this.searchCategory) {
        const m = this.searchTime - 1
        const arr = this.bills.filter(item => moment(new Date(Number(item.time))).month() == m && item.category == this.searchCategory)
        this.tableData = arr.sort(this.sortData);
        this.totalAmount(this.tableData)
      } else if (this.searchTime) {
        const m = this.searchTime - 1
        this.tableData = this.bills.filter(item => moment(new Date(Number(item.time))).month() == m)
        this.totalAmount(this.tableData)
      } else if (this.searchCategory) {
        this.tableData = this.bills.filter(item => item.category == this.searchCategory)
        this.totalAmount(this.tableData)
      } else {
        this.getList()
      }
    },
    writeCategory(row) {
      return this.categories.find(item => item.id == row.category).name
    },
    fromTime(time) {
      return moment(time).format()
    },
    handleClose () {
      this.$refs.form.resetFields()
      this.dialogVisible = false
    },
    onSumbit () {
      this.$refs.form.validate((valid) => {
        if (valid) {
          const from = JSON.parse(JSON.stringify(this.form))
          from.time = new Date().getTime().toString()
          this.tableData.unshift(from)
          this.bills = this.tableData
          this.dialogVisible = false
        }
      })
    },
    totalAmount(data) {
      this.totalIncome = 0
      this.totalExpenditure = 0
      if (data && data.length) {
        const income = data.filter(item => item.type == 1)
        const expenditure = data.filter(item => item.type == 0)
        if (income && income.length) {
          this.totalIncome = income.map(item => Number(item.amount)).reduce((prev, curr) => {
            return prev + curr
          })
        }
        if (expenditure && expenditure.length) {
          this.totalExpenditure = expenditure.map(item => Number(item.amount)).reduce((prev, curr)  => {
            return prev + curr
          })
        }
      }
      this.showCount = true
    },
    sortData(a, b) {
      return b.amount - a.amount
    }
  }
}
</script>

<style scoped>
  .content{
    width: 80%;
    margin: 0 auto;
  }

  .count{
    padding: 15px;
    background: #eee;
    margin-bottom: 30px;
    text-align: left;
  }
  .count span {
    font-weight: bold;
  }
</style>