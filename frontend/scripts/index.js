import { TOKEN_KEY } from "../contstants.js";
document.addEventListener("DOMContentLoaded", () => {
  const token =
    localStorage.getItem(TOKEN_KEY) || sessionStorage.getItem(TOKEN_KEY);

  console.log("home localStorage: ", localStorage.getItem(TOKEN_KEY));
  console.log("home sessionStorage: ", sessionStorage.getItem(TOKEN_KEY));

  if (token) {
    // Disable Login and Register buttons
    document.getElementById("loginBtn").disabled = true;
    document.getElementById("registerBtn").disabled = true;

    // Optional: Style disabled buttons
    document.getElementById("loginBtn").style.opacity = "0.5";
    document.getElementById("registerBtn").style.opacity = "0.5";
    document.getElementById("loginBtn").style.cursor = "not-allowed";
    document.getElementById("registerBtn").style.cursor = "not-allowed";
  }
});

document.getElementById("loginBtn").addEventListener("click", () => {
  if (!localStorage.getItem(TOKEN_KEY)) {
    window.location.href = "pages/login.html";
  }
});
document.getElementById("registerBtn").addEventListener("click", () => {
  if (!localStorage.getItem(TOKEN_KEY)) {
    window.location.href = "pages/register.html";
  }
});
document.getElementById("dashboardBtn").addEventListener("click", () => {
  window.location.href = "pages/dashboard.html";
});
