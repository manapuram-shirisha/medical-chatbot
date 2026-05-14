function send() {
    let msg = document.getElementById("msg").value;
    let chatbox = document.getElementById("chatbox");

    if (!msg) {
        alert("Enter symptoms!");
        return;
    }

    // Show user message
    chatbox.innerText += "\nYou: " + msg + "\n\n";

    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ symptoms: msg })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);  // 🔥 IMPORTANT DEBUG

        chatbox.innerText += data.response + "\n";
        chatbox.innerText += "-------------------------------------------------\n";
    })
    .catch(error => {
        console.error(error);
        chatbox.innerText += "Bot: Error connecting to server!\n";
    });

    document.getElementById("msg").value = "";
}