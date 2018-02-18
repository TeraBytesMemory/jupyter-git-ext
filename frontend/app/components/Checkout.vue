<template>
  <div id="git-ext-checkout">
    <div class="description">
      checkout a branch.
    </div>
    <ul>
      <li v-for="branch in branches" :key="branch"
       :class="{ selected: selected === branch }" @click="checkout(branch)">
        {{branch}}
      </li>
      <li>
        <div class="new-branch-container"
         v-if="selected && !newBranchInput" @click.self="selected=''">
          <i class="fa fa-plus"></i>
          <div>new branch</div>
        </div>
        <div class="new-branch-container" v-else>
          <i class="fa fa-plus"></i>
          <input-wrapper style="width: 100%">
            <input type="text"
             v-model="newBranchInput"
             placeholder="new branch name"
             @focus="Jupyter.keyboard_manager.disable()"
             @blur="Jupyter.keyboard_manager.enable()"
             @keyup.enter="checkout(newBranchInput)">
          </input-wrapper>
        </div>
      </li>
    </ul>
  </div>
</template>
<script>
import axios from 'axios'
import InputWrapper from './utils/InputWrapper.vue'
import PushMsg from './utils/PushMsg.vue'
import JupyterMixin from './mixin/jupyter'

export default {
  data () {
    return {
      branches: [],
      selected: '',
      newBranchInput: ''
    }
  },
  mounted () {
    this.fetchBranches()
  },
  methods: {
    checkout (branch) {
      if (this.selected === branch) {
        return false;
      }
      axios.post('/git_ext/api/checkout', {
        branch,
        new_branch: !this.selected
      }).then(() => {
        this.$pushMsg(PushMsg, {
          type: 'success',
          message: `change to the branch ${branch}...`
        })
        this.selected = branch
        window.location.reload()
      })
    },
    fetchBranches () {
      axios.get('/git_ext/api/branch')
        .then(res => {
          this.selected = res.data.body.current_branch
          this.$set(this.$data, 'branches', res.data.body.branches)
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
#git-ext-checkout {
  width: 40vw;
  margin: 20vh auto 0;
  padding: 12px;
  background-color: #e7e7e7;
  font-size: 1.2em;
}
.description {
  padding: 12px;
}
ul {
  width: 90%;
  list-style-type: none;
  padding: 12px 0;
  margin: 0 auto;
}
li {
  width: 100%;
  border: 1px solid #b8b8b8;
  padding: 8px;
  padding-left: 32px;
  background-color: #f5f5f5;
}
li:hover {
  background-color: #ccc;
  cursor: pointer;
}
li:active {
  background-color: #fff;
}

li.selected {
  background-color: #fff;
  cursor: default;
}

.fa-plus {
  color: #67a925;
  margin-right: 1em;
}

.new-branch-container {
  display: flex;
  align-items: center;
}
</style>
