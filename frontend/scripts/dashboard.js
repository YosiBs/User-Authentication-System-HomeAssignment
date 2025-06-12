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
    document.getElementById("welcome").textContent = `Welcome, ${
      data.user.name || data.user.email || "User"
    }`;
    document.getElementById("nameInput").value = name;
  } else {
    alert("Session expired. Please login again.");
    localStorage.removeItem("token");
    window.location.href = "login.html";
  }
});
//Log out button fanctionality
document.getElementById("logoutBtn").addEventListener("click", () => {
  localStorage.removeItem("token");
  sessionStorage.removeItem("token");
  window.location.href = "../index.html";
});

//change Name button fanctionality
document.getElementById("changeNameBtn").addEventListener("click", async () => {
  const newName = document.getElementById("nameInput").value;
  const token =
    localStorage.getItem("token") || sessionStorage.getItem("token");

  const res = await fetch("http://127.0.0.1:5000/update-profile", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: token,
    },
    body: JSON.stringify({ name: newName }),
  });

  const data = await res.json();
  if (res.ok) {
    alert("Name updated!");
    document.getElementById(
      "greeting"
    ).textContent = `Welcome, ${data.user.name}`;
  } else {
    alert(data.error || "Failed to update name");
  }
});
