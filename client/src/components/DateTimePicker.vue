<template>
  <div class="block">
    <span class="demonstration"></span>
    <el-date-picker
      v-model="pickDateTime"
      :value="pickDateTime"
      type="datetime"
      placeholder="选择日期时间"
      @change="timePick"

    >
    </el-date-picker>
  </div>
</template>

<script>
export default {
  name:'DateTimePicker',
  data() {
    return {
      pickDateTime: "",
    };
  },
  methods: {
    timePick(value){
      this.$emit('timePick',value)
    }
  },
};
</script>