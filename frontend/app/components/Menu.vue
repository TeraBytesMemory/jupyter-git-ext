<template>
  <div id="git-ext-menu" :style="{ top: `${posY}px`, left: `${posX}px` }">
    <ul>
      <li @click="bus.$emit('changeMode', 'checkout')">
        checkout
      </li>
      <li @click="bus.$emit('changeMode', 'commit')">
        commit
      </li>
    </ul>
  </div>
</template>
<script>
import bus from '../bus'

export default {
  props: {
    top: {
      type: Number,
      default: 0
    },
    left: {
      type: Number,
      default: 0
    },
    y: {
      type: Number,
      default: 0
    },
    x: {
      type: Number,
      default: 0
    }
  },
  computed: {
    posX () {
      return this.x || this.left
    },
    posY () {
      return this.y || this.top
    },
    bus: () => bus
  },
  data: () => ({

  })
}
</script>
<style scoped>
#git-ext-menu {
  position: fixed;
  font-size: 1em;
  width: 160px;
  height: auto;
  z-index: 2000;
}

ul {
  list-style-type: none;
  padding: 0;
  background-color: #e7e7e7;
}
li {
  width: 100%;
  border: 1px solid #ddd;
  padding: 8px;
}
li:hover {
  background-color: #ccc;
  cursor: pointer;
}

li.selected {
  background-color: #fff;
  cursor: default;
}
</style>
