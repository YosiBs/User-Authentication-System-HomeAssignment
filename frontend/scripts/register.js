console.log("loaded");

import { TOKEN_KEY, REGISTER_ENDPOINT } from "../contstants.js";

document.getElementById("homeBtn").addEventListener("click", () => {
  window.location.href = "../index.html";
});

console.log("register localStorage: ", localStorage.getItem(TOKEN_KEY));
console.log("register sessionStorage: ", sessionStorage.getItem(TOKEN_KEY));

window.addEventListener("beforeunload", () => {
  console.log("🔥 Page is unloading");
});

document.addEventListener("DOMContentLoaded", (e) => {
  e.preventDefault();
  console.log("🚀 DOM fully loaded");
  document
    .getElementById("registerForm")
    .addEventListener("submit", async (e) => {
      e.preventDefault();

      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      const confirmPassword = document.getElementById("confirmPassword").value;
      const name = document.getElementById("name").value;

      const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,12}$/;
      if (!passwordRegex.test(password)) {
        alert(
          "Password must have:\n 1 uppercase letter\n 1 lowercase letter\n 1 number\n 8–12 characters long"
        );
        return;
      }

      if (password !== confirmPassword) {
        document.getElementById("error").textContent =
          "Passwords do not match!";
        return;
      }
      try {
        const response = await fetch("http://127.0.0.1:5000/register", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email, password, name }),
        });
        console.log(response);

        const data = await response.json();
        console.log(data);

        console.log(response.ok);
        if (response.ok) {
          alert("Registration successful! Please go to your email and verify.");
          window.location.href = "../index.html";
        } else {
          document.getElementById("error").textContent =
            data.error || "Registration failed.";
        }
      } catch (err) {
        console.error("❌ Fetch failed:", err);
      }
    });
});
