<template>
  <div class="input-wrapper">
    <slot></slot>
  </div>
</template>
<script>
export default {
}
</script>
<style scoped>
.input-wrapper {
  position: relative;
}

.input-wrapper::after {
  background-color: #67a925;
  bottom: -4px;
  content: '';
  display: block;
  height: 2px;
  left: 0;
  position: absolute;
  transition: .5s all;
  width: 100%;
}

.input-wrapper > input[type="text"] {
  font-size: 1em;
  width: 100%;
  border-style: hidden;
  outline: 0;
  background-color: transparent;
}
</style>
