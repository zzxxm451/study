```
制作一个简单的待办事项列表，用户可以添加新的待办事项、标记已完成的事项、删除已完成的事项。
```
参考代码
HTML 代码
<!DOCTYPE html>
<html>
  <head>
    <title>Todo List</title>
  </head>
  <body>
    <h1>Todo List</h1>
    <form>
      <input type="text" placeholder="Add a new todo">
      <button type="submit">Add</button>
    </form>
    <ul>
      <li><input type="checkbox"> Learn JavaScript</li>
      <li><input type="checkbox"> Build a website</li>
      <li><input type="checkbox"> Run a marathon</li>
    </ul>
    <button>Delete completed todos</button>
  </body>
</html>
JavaScript 代码
// 获取 DOM 元素
const form = document.querySelector('form');
const input = document.querySelector('input');
const ul = document.querySelector('ul');
const deleteButton = document.querySelector('button');

// 添加新的待办事项
form.addEventListener('submit', (event) => {
  event.preventDefault(); // 阻止表单提交的默认行为
  const text = input.value.trim(); // 获取输入框中的文本，并去掉首尾空格
  if (text !== '') {
    const li = document.createElement('li');
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    li.appendChild(checkbox);
    li.appendChild(document.createTextNode(text));
    ul.appendChild(li);
    input.value = ''; // 清空输入框
  }
});

// 标记已完成的事项
ul.addEventListener('change', (event) => {
  const checkbox = event.target;
  const li = checkbox.parentNode;
  if (checkbox.checked) {
    li.classList.add('completed');
  } else {
    li.classList.remove('completed');
  }
});

// 删除已完成的事项
deleteButton.addEventListener('click', () => {
  const completedItems = ul.querySelectorAll('.completed');
  completedItems.forEach((item) => {
    item.remove();
  });
});
CSS 代码
.completed {
  text-decoration: line-through;
}
