document.getElementById('toggle_header').addEventListener('click', function(e){
  let toggle_header = e.target
  toggle_header.className = (toggle_header.className == 'red') ? 'green' : 'red'
})

// e stands for event
// target is always targeting a html element (here: toggle_header)
