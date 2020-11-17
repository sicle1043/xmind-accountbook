import axios from 'axios'

function request(config) {
  const instance = axios.create({
    baseURL: 'http://localhost:8000/journal',
    timeout: 5000
  })

  // 拦截器
  instance.interceptors.response.use(
    res => {
      return res.data
    },
    err => {
      return err
    }
  )

  return instance(config)
}

export function getRecord() {
  return request({ url: '/records' })
}
export function getCategory(){
  return request({url:'/category'})
}
export function postRecord(postData) {
  return request({
    url: '/records/',
    method: 'post',
    data: {
      'type': Number(postData.type),
      'time': new Date(Number(postData.time)),
      'category': postData.category,
      'amount': Number(postData.amount)
    }
  })
}