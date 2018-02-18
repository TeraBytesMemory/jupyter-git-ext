import App from '../app/App.vue'
import popMssage from '../pop_msg_plugin'
import Vue from 'vue'

export default function appendApp () {
  const appWrapper = document.createElement('div')
  appWrapper.setAttribute('id', 'git-ext-app')
  appWrapper.setAttribute('style', 'padding: 0; margin: 0;')
  document.body.appendChild(appWrapper)
  Vue.use(popMssage)

  /* eslint-disable no-new */
  new Vue({
    el: '#git-ext-app',
    render: h => h(App)
  })
}
