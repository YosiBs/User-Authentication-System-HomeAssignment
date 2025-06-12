document.addEventListener("DOMContentLoaded", () => {
  const token =
    localStorage.getItem("token") || sessionStorage.getItem("token");

  console.log("home localStorage: ", localStorage.getItem("token"));
  console.log("home sessionStorage: ", sessionStorage.getItem("token"));

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
  if (!localStorage.getItem("token")) {
    window.location.href = "pages/login.html";
  }
});
document.getElementById("registerBtn").addEventListener("click", () => {
  if (!localStorage.getItem("token")) {
    window.location.href = "pages/register.html";
  }
});
document.getElementById("dashboardBtn").addEventListener("click", () => {
  window.location.href = "pages/dashboard.html";
});
