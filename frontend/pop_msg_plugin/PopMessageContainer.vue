<template>
  <div id="pop-message" :style="customStyle">
    <component :is="msg.Component" v-bind="msg.props"
     v-for="(msg, index) in messages" :key="index" />
  </div>
</template>
<script>
import Vue from 'vue'

export default {
  props: {
    customStyle: {
      type: Object,
      default: () => ({})
    },
    showSec: {
      type: Number,
      default: 3
    }
  },
  data: () => ({
    messages: []
  }),
  methods: {
    push (Component, props) {
      this.$data.messages.push({ Component, props })
      setTimeout(() => {
        this.$data.messages.shift()
      }, this.showSec * 1000)
    }
  }
}
</script>
<style scoped>
#pop-message {
  position: fixed;
  top: 10vh;
  right: 40px;
  z-index: 2147483647;
  width: 10vw;
  height: 100vh;

  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
</style>
