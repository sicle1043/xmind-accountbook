<template>
  <div class="main-body">
    <record-main :records="records"></record-main>
    <record-footer
      :recordCategory="recordCategory"
      @recordSubmit="recordSubmit"
    ></record-footer>
  </div>
</template>
<script>
import { getRecord, getCategory } from "@/network/request.js";
import RecordMain from "./childrenComps/RecordMain";
import RecordFooter from "./childrenComps/RecordFooter.vue";
export default {
  components: { RecordMain, RecordFooter },
  name: "Record",
  data() {
    return {
      records: [],
      recordCategory: {},
      recordId: [],
    };
  },
  methods: {
    getCategory() {
      getCategory().then((res) => {
        res.forEach((element) => {
          this.recordCategory[element.id] = {
            name: element.name,
            type: element.type,
          };
        });
      });
    },
    getRecord() {
      getRecord().then((res) => {
        res.forEach((element) => {
          this.constructRecord(element);
        });
        // this.records = res;
      });
    },
    constructRecord(element) {
      let year = new Date(element.time).getFullYear().toString();
      let month = (new Date(element.time).getMonth() + 1).toString();
      let id = year + month;
      let belongTOId = this.recordId.indexOf(id)
      if (belongTOId === -1) {
        this.records.push({
          year: year,
          month: month,
          time: year + "/" + month,
          id: id,
          monthRecord: [
            {
              id: element.id,
              time: this.constructDateTime(element.time),
              type: element.type,
              category: this.recordCategory[element.category].name,
              amount: element.type === 1 ? element.amount : -element.amount,
            },
          ],
        });
        this.recordId.push(id);
      } else {
        this.records[belongTOId].monthRecord.push({
          id: element.id,
          time: this.constructDateTime(element.time),
          type: element.type,
          amount: element.type === 1 ? element.amount : -element.amount,
          category: this.recordCategory[element.category].name,
        });
      }
    },

    constructDateTime(timeStr) {
      timeStr = new Date(timeStr);
      return (
        timeStr.toLocaleDateString() + " " + timeStr.toTimeString().slice(0, 9)
      );
    },
    recordSubmit(formRes) {
      // this.getRecord();
      this.constructRecord(formRes);
    },
  },
  created() {
    this.getCategory();
    this.getRecord();
    // this.postRecord();
    // let y = this.records[0]["amount"]
  },
  mounted() {
    
  },
};
</script>
<style scoped>
</style>