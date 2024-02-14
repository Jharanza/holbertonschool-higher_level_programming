
document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.querySelector('#add_item');
  addItem.addEventListener('click', () => {
    const li = document.createElement('li');
    li.innerText = 'Item';
    const myList = document.querySelector('#my_list');
    myList.appendChild(li);
  });
});
