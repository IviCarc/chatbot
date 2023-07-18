const mostrarChat = (chat) => {
    // console.log(chat)
    chatBodyText = ""
    for (const mensaje of chat.split('/')) {
        // console.log(mensaje)
        if (mensaje.includes('BOT:')) {
            nuevoMensaje = mensaje.replace("BOT: ", "")
            chatBodyText += `<div class="message bot-message">${nuevoMensaje}</div>`
            // chatBodyText = chat.replace(mensaje, `<div class="message bot-message">${mensaje}</div>`)
        } else {
            nuevoMensaje = mensaje.replace("USUARIO: ", "")
            chatBodyText += `<div class="message user-message">${nuevoMensaje}</div>`
        }
    }
    html =  `<div class="chat-container card shadow-lg">
                <div class="chat-header" id="chat-header">
                    <h1 class="chat-title">Chatbot</h1>
                    <h2 class="chat-subtitle">Laboratorio Consultar SRL</h2>
                </div>
                <div class="chat-body" id="chat-body">
                    ${chatBodyText}
                </div>
            </div>`
    
    let div = document.createElement('div')
    div.innerHTML = html
    document.querySelector('.layout-container').appendChild(div)
}