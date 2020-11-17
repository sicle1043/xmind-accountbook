<template>
  <div class="record-footer">
    <el-button
      type="warning"
      circle
      style="padding: 0px"
      @click="dialogFormVisible = true"
      ><i class="el-icon-circle-plus" style="font-size: 40px"></i
    ></el-button>

    <el-dialog title="添加账单" :visible.sync="dialogFormVisible">
      <el-form :model="form" :rules="rules" ref="submitForm">
        <el-form-item label="类型" :label-width="formLabelWidth">
          <el-radio @change="typeChange" v-model="form.type" label="0"
            >支出</el-radio
          >
          <el-radio @change="typeChange" v-model="form.type" label="1"
            >收入</el-radio
          >
        </el-form-item>
        <el-form-item label="时间" :label-width="formLabelWidth" prop="time">
          <date-time-picker @timePick="timePick"></date-time-picker>
        </el-form-item>

        <el-form-item
          label="分类"
          :label-width="formLabelWidth"
          v-show="form.type.toString() === '0'"
          prop="category"
        >
          <el-select v-model="form.category" placeholder="请选择">
            <el-option
              v-for="item in paymentCategory"
              :key="item.name"
              :label="item.name"
              :value="item.id"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item
          label="分类"
          v-show="form.type.toString() === '1'"
          prop="category"
          :label-width="formLabelWidth"
        >
          <el-select v-model="form.category" placeholder="请选择分类">
            <el-option
              v-for="item in revenueCategory"
              :key="item.name"
              :label="item.name"
              :value="item.id"
            ></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="金额" :label-width="formLabelWidth" prop="amount">
          <el-input
            v-model.number="form.amount"
            autocomplete="off"
            type="number"
          >
            <template slot="prepend">￥</template>
          </el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogFormClick('submitForm')"
          >确 定</el-button
        >
      </div>
    </el-dialog>
  </div>
</template>

<script>
import DateTimePicker from "@/components/DateTimePicker.vue";
import { postRecord } from "@/network/request.js";
export default {
  components: { DateTimePicker },
  name: "RecordFooter",
  props: {
    recordCategory: {
      default: {},
    },
  },
  data() {
    return {
      dialogFormVisible: false,
      form: {
        type: "0",
        time: "",
        category: "",
        amount: 0.0,
      },
      revenueCategory: [],
      paymentCategory: [],
      formLabelWidth: "120px",
      rules: {
        amount: [
          {
            type: "number",
            required: true,
            message: "请输入金额",
            trigger: "blur",
          },
        ],
        time: [
          {
            required: true,
            message: "请选择时间",
            trigger: "blur",
          },
        ],
        category: [
          {
            required: true,
            message: "请选择分类",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    postRecord() {
      return postRecord(this.form);
    },
    dialogFormClick(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.postRecord().then((res) => {
            this.$emit("recordSubmit", res);
          });
          this.dialogFormVisible = false;

          alert("提交成功");
        } else {
          this.dialogFormVisible = false;
          alert("提交失败");
          return false;
        }
      });
    },
    timePick(pickTime) {
      this.form.time = pickTime;
    },
    seperateCategory() {
      for (let index in this.recordCategory) {
        if (!this.recordCategory.hasOwnProperty(index)) {
          continue;
        }
        if (this.recordCategory[index].type === 0) {
          this.paymentCategory.push({
            name: this.recordCategory[index].name,
            id: index,
          });
        } else {
          this.revenueCategory.push({
            name: this.recordCategory[index].name,
            id: index,
          });
        }
      }
    },
    typeChange(value) {
      this.form.category = "";
    },
  },
  created() {
    setTimeout(this.seperateCategory, 1000);
  },
};
</script>

<style>
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}
input[type="number"] {
  -moz-appearance: textfield;
}
</style>