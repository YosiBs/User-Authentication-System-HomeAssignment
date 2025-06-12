document.getElementById("homeBtn").addEventListener("click", () => {
  window.location.href = "../index.html";
});

console.log("Dashboard localStorage: ", localStorage.getItem("token"));
console.log("Dashboard sessionStorage: ", sessionStorage.getItem("token"));

document.addEventListener("DOMContentLoaded", async () => {
  const token =
    localStorage.getItem("token") || sessionStorage.getItem("token");
  if (!token) {
    alert("You need to login first!");
    window.location.href = "login.html";
    return;
  }

  const response = await fetch("http://127.0.0.1:5000/dashboard", {
    method: "GET",
    headers: {
      Authorization: token,
    },
  });

  const data = await response.json();

  if (response.ok) {
    document.getElementById("welcome").textContent = data.message;
  } else {
    alert("Session expired. Please login again.");
    localStorage.removeItem("token");
    window.location.href = "login.html";
  }
});

document.getElementById("logoutBtn").addEventListener("click", () => {
  localStorage.removeItem("token");
  sessionStorage.removeItem("token");
  window.location.href = "../index.html";
});
