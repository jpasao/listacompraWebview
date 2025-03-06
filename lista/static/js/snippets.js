const deleteModal = document.getElementById('deleteModal')
if (deleteModal) {
  deleteModal.addEventListener('show.bs.modal', event => {
    // Button that triggered the modal
    const button = event.relatedTarget
    // Extract info from data-bs-* attributes
    const recipient = button.getAttribute('data-bs-name')
    const functionName = button.getAttribute('data-bs-function')
    const id = button.getAttribute('data-bs-id') 

    // Update the modal's content.
    const modalTitle = deleteModal.querySelector('.modal-title')
    const modalBodyContent = deleteModal.querySelector('.modal-body p')
    const modalOkButton = deleteModal.querySelector('#deleteButton')

    modalTitle.textContent = `Borrando ${recipient}...`
    modalBodyContent.textContent = `Se va a borrar ${recipient}. ¿Seguro?`
    modalOkButton.href = `/${functionName}/${id}/delete/`
  })
}