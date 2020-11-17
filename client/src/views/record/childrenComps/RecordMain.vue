<template>
  <div class="record-main">
    <el-table
      :data="pickedRecords"
      style="width: 100%; margin-bottom: 20px"
      height="90vh"
      row-key="id"
      default-expand-all
      :tree-props="{ children: 'monthRecord' }"
    >
      <el-table-column label="项目" width="500" prop="time">
        <template slot="header" slot-scope="scope">
          <month-picker @monthChange="pickMonth"></month-picker>
        </template>
        <template slot-scope="scope">
          <div style="display:inline">
            <span style="margin-left: 10px; font-size: 20px">{{
              scope.row.category || ""
            }}</span>
            <i class="el-icon-time"></i>
            <span style="margin-left: 10px">{{ scope.row.time }}</span>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="金额">
        <template slot-scope="scope">
          <span>
            {{ showAmount(scope.row) }}
          </span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import MonthPicker from "@/components/MonthPicker.vue";
export default {
  name: "RecordMain",
  data() {
    return {
      pickedRecords:[],
    };
  },
  props: {
    records: {
      default: [],
    },
  },
  components: {
    MonthPicker,
  },
  created() {
    this.pickedRecords = this.records
  },
  methods: {
    pickMonth(pickedMonth) {
      if(pickedMonth){
        this.pickedRecords = this.records.filter((item)=>{
          console.log(new Date(item.time).getMonth());
          let pickTime = new Date(item.time)
          return pickTime.getMonth() === pickedMonth.getMonth() && pickTime.getFullYear() === pickedMonth.getFullYear()
        })
      }
      else{
        this.pickedRecords = this.records
      }
      
    },
    showAmount(row) {
      if (row.amount) {
        return row.amount;
      } else {
        return (
          "收入：" +
          row.monthRecord
            .filter((a) => a.type !== 0)
            .reduce((total, a) => {
              return total + a.amount;
            }, 0) +
          "\t" +
          "支出：" +
          row.monthRecord
            .filter((a) => a.type === 0)
            .reduce((total, a) => {
              return total + a.amount;
            }, 0)
        );
      }
    },
    filterHandler(value, row, column) {
      const property = column["property"];
      return row[property] === value;
    },
  },
};
</script>

<style>
</style>