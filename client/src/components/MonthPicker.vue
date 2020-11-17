<template>
  <div>
    <el-date-picker
      class="a"
      v-model="pickMonth"
      type="month"
      placeholder="选择月份"
      @change="monthChange"
    >
    </el-date-picker>
  </div>
</template>

<script>
export default {
  name: "MonthPicker",
  data() {
    return {
      pickMonth: "",
    };
  },
  methods: {
    monthChange(value){
      this.$emit('monthChange',value)
    }
  },
};
</script>
<style scoped>
.a {
  width: 120px;
  border: none;
}
</style>