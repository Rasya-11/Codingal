let balance = 0;

function creditAmount() {
  const amount = getAmount();
  if (amount === null) return;

  balance += amount;
  updateUI("Amount credited successfully", "green");
}

function debitAmount() {
  const amount = getAmount();
  if (amount === null) return;

  if (amount > balance) {
    showMessage("Insufficient balance", "red");
    return;
  }

  balance -= amount;
  updateUI("Amount debited successfully", "green");
}

function getAmount() {
  const input = document.getElementById("amount").value.trim();

  if (input === "" || isNaN(input) || input <= 0) {
    showMessage("Please enter a valid amount", "red");
    return null;
  }

  return Number(input);
}

function updateUI(msg, color) {
  document.getElementById("balance").innerText = balance;
  showMessage(msg, color);
  document.getElementById("amount").value = "";
}

function showMessage(text, color) {
  const message = document.getElementById("message");
  message.innerText = text;
  message.style.color = color;
}
