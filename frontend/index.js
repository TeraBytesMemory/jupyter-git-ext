import configure from './utils/configure'
import appendApp from './utils/appendApp'

export function load_ipython_extension () {
  const Jupyter = window.Jupyter

  appendApp()
  const full_action_name = Jupyter.actions.register(
    configure.action,
    configure.action_name,
    configure.prefix
  )
  Jupyter.toolbar.add_buttons_group([full_action_name])
}
