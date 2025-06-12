import {
  TOKEN_KEY,
  DASHBOARD_ENDPOINT,
  UPDATE_PROFILE_ENDPOINT,
} from "../contstants.js";

document.getElementById("homeBtn").addEventListener("click", () => {
  window.location.href = "../index.html";
});

console.log("Dashboard localStorage: ", localStorage.getItem(TOKEN_KEY));
console.log("Dashboard sessionStorage: ", sessionStorage.getItem(TOKEN_KEY));

document.addEventListener("DOMContentLoaded", async () => {
  const token =
    localStorage.getItem(TOKEN_KEY) || sessionStorage.getItem(TOKEN_KEY);
  if (!token) {
    alert("You need to login first!");
    window.location.href = "login.html";
    return;
  }

  const response = await fetch(DASHBOARD_ENDPOINT, {
    method: "GET",
    headers: {
      Authorization: token,
    },
  });

  const data = await response.json();

  if (response.ok) {
    document.getElementById("welcome").textContent = `Welcome, ${
      data.user.name || data.user.email || "User"
    }`;
    document.getElementById("nameInput").value = name;
  } else {
    alert("Session expired. Please login again.");
    localStorage.removeItem(TOKEN_KEY);
    window.location.href = "login.html";
  }
});
//Log out button fanctionality
document.getElementById("logoutBtn").addEventListener("click", () => {
  localStorage.removeItem(TOKEN_KEY);
  sessionStorage.removeItem(TOKEN_KEY);
  window.location.href = "../index.html";
});

//change Name button fanctionality
document.getElementById("changeNameBtn").addEventListener("click", async () => {
  const newName = document.getElementById("nameInput").value;
  const token =
    localStorage.getItem(TOKEN_KEY) || sessionStorage.getItem(TOKEN_KEY);

  const res = await fetch(UPDATE_PROFILE_ENDPOINT, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: token,
    },
    body: JSON.stringify({ name: newName }),
  });

  const data = await res.json();
  if (res.ok) {
    alert("Name updated!, Please refresh");
    document.getElementById(
      "greeting"
    ).textContent = `Welcome, ${data.user.name}`;
  } else {
    alert(data.error || "Failed to update name");
  }
});
