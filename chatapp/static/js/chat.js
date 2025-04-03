const getCookie = (name) => {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
};


window.addEventListener("DOMContentLoaded", () => {
  const userId = getCookie('user_id');
  const conversation_id = getCookie('conversation_id')
  const websocket = new WebSocket(`ws://localhost:5000/ws/${userId}/${conversation_id}`)
  const event = {
    "type": "message",
    "text": `Hello I'm User with id ${userId} `
  }
  const button = document.querySelector(".chat-submit")

  websocket.onmessage = function(event) {
    let messages = document.querySelector(".messages-container")
    let message = document.createElement('div')
    message.classList.add("message")
    message.classList.add("user-message")
    let paragraph = document.createElement('p')
    let content = document.createTextNode(event.data)
    paragraph.appendChild(content)
    message.appendChild(paragraph)
    messages.appendChild(message)
    messages.scrollTop = messages.scrollHeight
  };

  function sendMessage(){
    message = document.getElementById("messageText")
    websocket.send(message.value)
    message.value = ''
  }
  

  button.addEventListener("click", (e) => {
    e.preventDefault()
    sendMessage(websocket)
    // websocket.send(JSON.stringify(event))
  })  

  websocket.addEventListener("message", ({data}) => {
    console.log(data)
  })
})