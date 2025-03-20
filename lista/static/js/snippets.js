// Modal for deleting or adding meal ingredients
const globalModal = document.getElementById('globalModal')
if (globalModal) {
  globalModal.addEventListener('show.bs.modal', event => {
    // Button that triggered the modal
    const button = event.relatedTarget
    // Extract info from data-bs-* attributes
    const name = button.getAttribute('data-bs-name')
    const functionName = button.getAttribute('data-bs-function')
    const id = button.getAttribute('data-bs-id')
    const operation = button.getAttribute('data-bs-operation')

    // Update the modal's content.
    const modalTitle = globalModal.querySelector('.modal-title')
    const modalBodyContent = globalModal.querySelector('.modal-body')
    const modalOkButton = globalModal.querySelector('#globalButton')

    if (operation === 'delete') {
      globalModal.classList.remove('modal-lg')
      modalTitle.textContent = 'Ojito cuidao'
      modalBodyContent.innerHTML = `<p>Se va a borrar ${name}. ¿Seguro?</p>`
      modalOkButton.href = `/${functionName}/${id}/${operation}/`
    }
    if (operation === 'ingredients') {
      globalModal.classList.add('modal-lg')
      modalTitle.textContent = `¿Qué lleva ${name}?`
      const ingredientOuterNode = document.getElementById('hidden_ingredient_list').cloneNode(true)
      const innerTable = ingredientOuterNode.children[0]
      modalBodyContent.innerHTML = ''
      resetCheckedMealIngredients()
      const filterField = createSearchField()
      const pillContainer = createPillContainer()

      modalBodyContent.appendChild(filterField)
      modalBodyContent.appendChild(pillContainer)
      modalBodyContent.appendChild(innerTable)
      getMealIngredientsData(`/${functionName}/${id}/${operation}/`)
      modalOkButton.onclick = function (event) {
        event.preventDefault()
        saveMealIngredientsData(`/${functionName}/${id}/${operation}/save/`)
        const modalInstance = bootstrap.Modal.getInstance(globalModal)
        modalInstance.toggle()
      }
    }
  })
}
const createPillContainer = () => {
  const pillContainer = document.createElement('div')
  const pillProps = { id: 'pillContainer', class: 'my-2 gap-2' }
  setAttributes(pillContainer, pillProps)
  return pillContainer
}
const createSearchField = () => {
  const filterField = document.createElement('input')
  const filterProps = { type: 'text', class: 'form-control my-4', placeholder: 'Escribe para filtrar' }
  setAttributes(filterField, filterProps)
  filterField.addEventListener('keyup', event => {
    const searchTerm = event.target.value.toLowerCase()
    const fullList = document.querySelectorAll('.destination .ingredient-list')
    for (item of fullList) {
      const rowElement = item.parentElement.parentElement.parentElement
      const found = item.nextElementSibling.textContent.toLowerCase().includes(searchTerm)
      if (found)
        rowElement.classList.remove('d-none')
      else
        rowElement.classList.add('d-none')
    }
  })
  return filterField
}
const createPill = (pillId, pillText) => {
  const removeButton = document.createElement('button')
  const removeButtonProps = { type: 'button', class: 'btn-close' }
  setAttributes(removeButton, removeButtonProps)
  removeButton.addEventListener('click', () => removePill(pillId))

  const removeWrapper = document.createElement('span')
  const removeWrapperProps = { class: 'badge mr-1', style: 'top: -4px' }
  setAttributes(removeWrapper, removeWrapperProps)
  removeWrapper.appendChild(removeButton)

  const text = document.createElement('label')
  text.setAttribute('class', 'px-2 mt-1')
  text.innerText = pillText

  const pill = document.createElement('button')
  const pillProps = { class: 'btn btn-outline-primary btn-sm m-2 p-1', id: pillId }
  setAttributes(pill, pillProps)
  pill.appendChild(removeWrapper)
  pill.appendChild(text)

  const pillContainer = document.getElementById('pillContainer')
  pillContainer.appendChild(pill)
}
const removePill = (pillId) => {
  const pill = document.getElementById(pillId)
  pill.remove()
  const id = pillId.split('-')[1]
  removeIngredientFromMeal(id)
  const check = document.querySelector(`.destination #check-${id}`)
  check.checked = false
}

// Collect meal ingredients
const mealIngredients = []
const resetCheckedMealIngredients = () => mealIngredients.length = 0
const checkIngredient = (item) => {
  const check = item.children[0]
  const checkId = check.id.split('-')[1]
  const label = item.children[1].innerText
  check.checked = !check.checked
  if (check.checked) {
    addIngredientToMeal(checkId)
    createPill(`pill-${checkId}`, label)
  }
  else {
    removeIngredientFromMeal(checkId)
  }
}
const addIngredientToMeal = (ingredient) => mealIngredients.push(ingredient)
const removeIngredientFromMeal = (ingredient) => {
  const index = mealIngredients.indexOf(ingredient)
  if (index > -1) mealIngredients.splice(index, 1)
}
const saveMealIngredientsData = (endpoint) => {
  const formData = getFormWithToken()
  formData.append('ingredients', JSON.stringify({data: mealIngredients}))
  fetch(endpoint, {
    method: 'POST',
    body: formData
  })
}
const getMealIngredientsData = (endpoint) => {
  const formData = getFormWithToken()
  fetch(endpoint, {
    method: 'POST',
    body: formData
  }).then(data =>
    data.json()
  ).then(data => {
    const checkedIngredients = data.data.map(item => item.toString())
    const ingredientList = document.querySelectorAll('.destination .ingredient-list')
    for (item of ingredientList) {
      const itemId = item.id.split('-')[1]
      if (checkedIngredients.includes(itemId)) {
        item.checked = true
        addIngredientToMeal(itemId)
        const label = item.nextElementSibling.innerText
        createPill(`pill-${itemId}`, label)
      }
    }
  })
}
const setAttributes = (el, attrs) => {
  Object.keys(attrs).forEach(key => el.setAttribute(key, attrs[key]))
}
const getFormWithToken = () => {
  const formData = new FormData()
  const token = document.forms[0].getElementsByTagName('input').csrfmiddlewaretoken.value
  formData.append('csrfmiddlewaretoken', token)
  return formData
}