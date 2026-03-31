async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value;
    if (!message) return;

    // User-message
    chatBox.innerHTML += `<div class="message user">${message}</div>`;
    input.value = "";

    // Backend
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    // Bot-reply
    chatBox.innerHTML += `<div class="message bot">${data.reply}</div>`;

    chatBox.scrollTop = chatBox.scrollHeight;
}