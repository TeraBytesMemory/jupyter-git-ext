import PopMessageContainer from './PopMessageContainer.vue'

function install (Vue, options = {}) {
  const appWrapper = document.createElement('div')
  appWrapper.setAttribute('id', 'pop-message-wrapper')
  document.body.appendChild(appWrapper)

  const popMessageContainer = new Vue({
    el: '#pop-message-wrapper',
    computed: {
      options: () => options
    },
    render: h => h(PopMessageContainer, { props: options, ref: 'container' })
  })

  Vue.pushMsg = popMessageContainer.$refs.container.push
  Vue.prototype.$pushMsg = popMessageContainer.$refs.container.push
}

export default { install }
