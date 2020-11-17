<template>
  <el-page-header @back="goBack">
    <slot></slot>
  </el-page-header>
</template>

<script>
export default {
  methods: {
    goBack() {
      console.log("go back");
    },
  },
};
</script>