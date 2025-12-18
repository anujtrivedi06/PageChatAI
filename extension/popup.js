const BACKEND = "http://localhost:5000";
const chat = document.getElementById("chat");

function log(text) {
  chat.textContent += text + "\n\n";
}

async function currentURL() {
  return new Promise(resolve => {
    chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
      resolve(tabs[0].url);
    });
  });
}

document.getElementById("init").onclick = async () => {
  const url = await currentURL();
  log("Loading page...");

  const res = await fetch(`${BACKEND}/init`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url })
  });

  const data = await res.json();
  log("AI: " + data.message);
};

document.getElementById("ask").onclick = async () => {
  const q = document.getElementById("question").value;
  if (!q) return;

  log("You: " + q);

  const res = await fetch(`${BACKEND}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: q })
  });

  const data = await res.json();
  log("AI: " + data.reply);
};
