<template>
  <transition
    enter-active-class="animated bounceInRight"
    leave-active-class="animated bounceOutRight"
  >
    <div class="message" :class="classAttr">
      {{message}}
    </div>
  </transition>
</template>
<script>
export default {
  props: {
    message: String,
    type: String
  },
  computed: {
    classAttr () {
      return {
        successmsg: this.type === "success",
        errormsg: this.type === "error"
      }
    }
  }
}
</script>
<style lang="scss" scoped>
$use-bounceInRight: true;
$use-bounceOutRight: true;
@import '~animate/animate';

.message {
  width: 100%;
  height: calc(24px + 1em);
  padding: 12px;
  margin: 12px 0;
  border-radius: 4px;
}

.message.successmsg {
  background-color: #088ae9;
  color: white;
}

.message.errormsg {
  background-color: #ca3827;
  color: white;
}
</style>
