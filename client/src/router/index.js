import Vue from 'vue'
import VueRouter from 'vue-router'

const Home = () => import('@/views/Home')
const Record = () => import('@/views/record/Record')
const Statistic = () => import('@/views/Statistic')

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    redirect: '/record'
  },
  {
    path: '/home',
    component: Home,
  },
  {
    path: '/record',
    component: Record,
  },
  { 
    path: '/statistic',
    component: Statistic,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
