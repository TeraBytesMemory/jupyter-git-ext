<template>
  <div id="git-ext" :class="{ active: isOpenModal }" @click.self="closeModal">
    <menu-container :x="menuX" :y="menuY" v-if="isShowMenu" />
    <checkout v-if="mode === 'checkout'" />
    <commit v-else-if="mode === 'commit'" />
  </div>
</template>
<script>
import bus from './bus'
import Checkout from './components/Checkout.vue'
import Commit from './components/Commit.vue'
import MenuContainer from './components/Menu.vue'

export default {
  data () {
    return {
      mode: '',
      isShowMenu: false,
      menuX: 0,
      menuY: 0
    }
  },
  components: {
    Checkout,
    Commit,
    MenuContainer
  },
  computed: {
    isOpenModal () {
      return Boolean(this.mode)
    }
  },
  created() {
    bus.$on('changeMode', this.changeMode)
    bus.$on('hideModal', () => this.changeMode(''))
    bus.$on('showMenu', this.showMenu)
  },
  methods: {
    showMenu(x, y) {
      const fixedY = Math.max(y, document.getElementById('site').offsetTop)
      this.menuX = x
      this.menuY = fixedY
      this.isShowMenu = true
    },
    changeMode(mode) {
      this.mode = mode
      this.isShowMenu = false
    },
    closeModal () {
      this.mode = ''
      this.isShowMenu = false
    }
  }
}
</script>
<style scoped>
#git-ext {
  position: fixed;
  top: 0;
  left: 0;
}

#git-ext.active {
  z-index: 1000;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}
</style>
