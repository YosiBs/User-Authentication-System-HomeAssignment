import { TOKEN_KEY, REGISTER_ENDPOINT } from "../contstants.js";

document.getElementById("homeBtn").addEventListener("click", () => {
  window.location.href = "../index.html";
});

console.log("register localStorage: ", localStorage.getItem(TOKEN_KEY));
console.log("register sessionStorage: ", sessionStorage.getItem(TOKEN_KEY));

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
      document.getElementById("error").textContent = "Passwords do not match!";
      return;
    }

    const response = await fetch(REGISTER_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password, name }),
    });

    const data = await response.json();

    if (response.ok) {
      alert("Registration successful! Please go to your email and verify.");
      window.location.href = "../index.html";
    } else {
      document.getElementById("error").textContent =
        data.error || "Registration failed.";
    }
  });
