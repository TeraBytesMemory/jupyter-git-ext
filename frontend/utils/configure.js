import bus from '../app/bus'

const configure = {
  action: {
    icon: 'fa-code-fork',
    help: 'operate git',
    help_index: 'g',
    handler () {
      bus.$emit('showMenu', window.event.clientX, window.event.clientY)
    }
  },
  prefix: '',
  action_name: ''
}

export default configure
