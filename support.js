const chatBox = document.getElementById('chatBox');
const chatForm = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');
const displayBtn = document.getElementById('displayBtn');
const historyTable = document.getElementById('historyTable');

const API_URL = "http://localhost:8000"; // Change if backend runs elsewhere

chatForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    const userText = userInput.value.trim();
    if (!userText) return;

    // Add user message
    const userMsg = document.createElement('div');
    userMsg.className = 'user-message';
    userMsg.textContent = userText;
    chatBox.appendChild(userMsg);

    // Call backend
    const aiMsg = document.createElement('div');
    aiMsg.className = 'ai-message';
    aiMsg.textContent = "Thinking...";
    chatBox.appendChild(aiMsg);

    try {
        const res = await fetch(`${API_URL}/chat`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({prompt: userText})
        });
        const data = await res.json();
        aiMsg.textContent = data.response;
    } catch (err) {
        aiMsg.textContent = "Error contacting AI assistant.";
    }

    userInput.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;
});

// Display chat history
displayBtn.addEventListener('click', async function() {
    try {
        const res = await fetch(`${API_URL}/history`);
        const data = await res.json();
        if (data.history.length === 0) {
            historyTable.innerHTML = "<p>No chat history yet.</p>";
            return;
        }
        let html = `<table border="1" style="width:100%;margin-top:1rem;"><tr><th>ID</th><th>Prompt</th><th>Response</th></tr>`;
        for (const row of data.history) {
            html += `<tr><td>${row.id}</td><td>${row.prompt}</td><td>${row.response}</td></tr>`;
        }
        html += "</table>";
        historyTable.innerHTML = html;
    } catch (err) {
        historyTable.innerHTML = "<p>Error loading history.</p>";
    }
}); 