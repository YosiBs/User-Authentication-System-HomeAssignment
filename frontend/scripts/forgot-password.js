document.getElementById("forgotForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value;

  const response = await fetch("http://127.0.0.1:5000/forgot-password", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email }),
  });

  const data = await response.json();

  if (response.ok) {
    document.getElementById("message").textContent = data.message;
    document.getElementById("message").style.color = "green";
  } else {
    document.getElementById("message").textContent =
      data.error || "Something went wrong.";
    document.getElementById("message").style.color = "red";
  }
});

document.getElementById("homeBtn").addEventListener("click", () => {
  window.location.href = "../index.html";
});
