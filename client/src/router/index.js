import Vue from 'vue'
import VueRouter from 'vue-router'


const Record = () => import('@/views/record/Record')


Vue.use(VueRouter)

const routes = [
  {
    path: '',
    redirect: '/record'
  },

  {
    path: '/record',
    component: Record,
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
