// add a li element to a list when the user clicks on the element with id add_item
// ul element with class my_list

document.getElementById('add_item').onclick = addItem;

function addItem() {
  // Select ul element with class my_list
  let ul = document.querySelector("ul.my_list");
  // Create a new 'li' element
  let li = document.createElement("li");
  // create a new text node with the word Item
  let text = document.createTextNode("Item");
  // append 'li' to 'ul'
  ul.appendChild(li);
  // append 'text' to 'li'
  li.appendChild(text);
}
