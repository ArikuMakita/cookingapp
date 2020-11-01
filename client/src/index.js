document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('btn')
  const input = document.getElementById('input')
  const container = document.getElementById('container')
  getAllTodo()

  container.addEventListener('click', containerClickHandler)
  btn.addEventListener('click', addTodo)
  input.addEventListener('keydown', addTodoOnEnter)

  const actions = {
    delete: deleteTodoById
  }

  async function containerClickHandler(e) {
    await actions[e.target.dataset.action](e)
  }

  async function getAllTodo() {
    const todos = JSON.parse(await eel.getAllTodo()())
    todos.forEach(todo => {
      const html = `<p><span data-action="delete" data-id="${todo.id}">X</span> ${todo.title}</p>`
      container.insertAdjacentHTML('beforeend', html)
    })
  }

  async function addTodoOnEnter(e) {
    if (e.key === 'Enter') {
      await addTodo()
    }
  }
  async function addTodo() {
    const todo = {
      title: input.value,
    }
    const res = await eel.addTodo(JSON.stringify(todo))()
    const new_todo = JSON.parse(res)
    input.value = ''
    container.insertAdjacentHTML(
      'beforeend',
      `<p><span data-action="delete" data-id="${new_todo.id}">X</span> ${new_todo.title}</p>`
    )
  }

  async function deleteTodoById(e) {
    const todo = {
      id: e.target.dataset.id,
    }
    await eel.deleteTodoById(JSON.stringify(todo))()
    e.target.closest('p').remove()
  }
})
