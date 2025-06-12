document.getElementById("homeBtn").addEventListener("click", () => {
  window.location.href = "../index.html";
});

console.log("login localStorage: ", localStorage.getItem("token"));
console.log("login sessionStorage: ", sessionStorage.getItem("token"));

document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const rememberMe = document.getElementById("rememberMe").checked;

  const response = await fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  const data = await response.json();
  console.log("response.status", response.status);
  if (response.status === 429) {
    alert(data.error || "Too many attempts. Try again later.");
    return;
  }
  if (response.ok) {
    if (rememberMe) {
      localStorage.setItem("token", data.token);
    } else {
      sessionStorage.setItem("token", data.token);
    }
    window.location.href = "dashboard.html";
  } else {
    document.getElementById("error").textContent =
      data.error || "Login failed.";
  }
});
