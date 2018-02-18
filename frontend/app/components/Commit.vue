<template>
  <div id="git-ext-commit">
    <div class="description">
      commit {{Jupyter.notebook.notebook_path}} changes.
    </div>
    <input-wrapper>
      <input type="text"
       v-model="commitMessage"
       placeholder="commit message"
       @focus="Jupyter.keyboard_manager.disable()"
       @blur="Jupyter.keyboard_manager.enable()"
       @keyup.enter="commit">
    </input-wrapper>
    <div class="button" @click="commit" stlye="cursor: pointer;">
      commit
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import InputWrapper from './utils/InputWrapper.vue'
import PushMsg from './utils/PushMsg.vue'
import JupyterMixin from './mixin/jupyter'
import bus from '../bus'

export default {
  data: () => ({
    commitMessage: ''
  }),
  methods: {
    commit (branch) {
      if (this.selected === branch) {
        return false;
      }
      axios.post('/git_ext/api/commit', {
        files: [this.Jupyter.notebook.notebook_path],
        commit_message: this.commitMessage
      }).then(() => {
        bus.$emit('hideModal')
        this.$pushMsg(PushMsg, {
          type: 'success',
          message: 'success to commit.'
        })
      })
    }
  },
  mixins: [JupyterMixin],
  components: {
    InputWrapper
  }
}
</script>
<style scoped>
#git-ext-commit {
  width: 40vw;
  margin: 20vh auto 0;
  padding: 12px;
  background-color: #e7e7e7;
  font-size: 1.2em;
}

#git-ext-commit > div {
  margin: 12px;
}

.button {
  border: 1px solid #b8b8b8;
  padding: 4px 12px;
  background-color: #f5f5f5;
  border-radius: 12px;
  box-shadow: 1px 2px 2px #b8b8b8;
  width: fit-content;
}

.button:hover {
  background-color: #ccc;
  cursor: pointer;
}

.button:active {
  background-color: #fff;
}
</style>
