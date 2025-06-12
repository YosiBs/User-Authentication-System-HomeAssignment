import { TOKEN_KEY, LOGIN_ENDPOINT } from "../contstants.js";

document.getElementById("homeBtn").addEventListener("click", () => {
  window.location.href = "../index.html";
});

console.log("login localStorage: ", localStorage.getItem(TOKEN_KEY));
console.log("login sessionStorage: ", sessionStorage.getItem(TOKEN_KEY));

document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const rememberMe = document.getElementById("rememberMe").checked;

  const response = await fetch(LOGIN_ENDPOINT, {
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
      localStorage.setItem(TOKEN_KEY, data.token);
    } else {
      sessionStorage.setItem(TOKEN_KEY, data.token);
    }
    window.location.href = "dashboard.html";
  } else {
    document.getElementById("error").textContent =
      data.error || "Login failed.";
  }
});
