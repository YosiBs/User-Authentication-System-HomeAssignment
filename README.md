# User-Authentication-System


<h2>🛠️ Setup Instructions</h2>

<h3>⚙️ Backend Setup</h3>
<ol>
  <li>
    <strong>📦 Install Python dependencies</strong><br>
    Make sure you have Python 3 installed.<br>
    Install the required libraries manually:
    <pre><code>pip install flask flask-cors flask-limiter flask-sqlalchemy bcrypt pyjwt</code></pre>
  </li>
  <li>
    <strong>🗄️ Initialize the database</strong><br>
    Run the following command from the root project folder:
    <pre><code>python -m backend.utils.create_db</code></pre>
  </li>
  <li>
    <strong>🚀 Start the backend server</strong><br>
    From the root folder:
    <pre><code>python -m backend.app</code></pre>
    The backend will start on: <code>http://127.0.0.1:5000</code>
  </li>
</ol>

<h3>🖥️ Frontend Setup</h3>
<ol>
  <li>
    <strong>🌐 Serve the frontend</strong><br>
    Open the <code>frontend/pages/register.html</code> or <code>index.html</code> using the <em>Live Server</em> extension in VS Code.
  </li>
  <li>
    <strong>✅ Ensure backend is running</strong><br>
    The frontend JavaScript makes API requests to <code>http://127.0.0.1:5000</code>, so make sure the backend is up before using the app.
  </li>
</ol>




<hr style="margin: 32px 0; border: none; border-top: 3px solid #ccc;">




<h2>📘 API Documentation</h2>

<h3>📝 1. Register</h3>
<pre><code>POST /register</code></pre>
<b>📤 Request Body (JSON):</b>
<pre>{
  "email": "user@example.com",
  "password": "Aa123456",
  "name": "User"
}</pre>
<b>📥 Responses:</b>
<ul>
  <li>✅ <code>200 OK</code> – User registered successfully</li>
  <li>⚠️ <code>400</code> – Email and password required</li>
  <li>🚫 <code>409</code> – User already exists</li>
</ul>

<h3>🔐 2. Login</h3>
<pre><code>POST /login</code></pre>
<b>📤 Request Body (JSON):</b>
<pre>{
  "email": "user@example.com",
  "password": "Aa123456"
}</pre>
<b>📥 Responses:</b>
<ul>
  <li>✅ <code>200 OK</code> – Returns JWT token</li>
  <li>🚫 <code>401</code> – Invalid credentials</li>
  <li>📧 <code>403</code> – Email not verified</li>
</ul>

<h3>📂 3. Dashboard</h3>
<pre><code>GET /dashboard</code></pre>
<b>🪪 Headers:</b>
<pre>Authorization: Bearer &lt;JWT_TOKEN&gt;</pre>
<b>📥 Responses:</b>
<ul>
  <li>✅ <code>200 OK</code> – Returns user info</li>
  <li>🔒 <code>401</code> – Token missing / expired / invalid</li>
  <li>❓ <code>404</code> – User not found</li>
</ul>

<h3>✉️ 4. Verify Email</h3>
<pre><code>GET /verify?token=&lt;verification_token&gt;</code></pre>
<b>📥 Responses:</b>
<ul>
  <li>✅ <code>200 OK</code> – Verification successful (HTML)</li>
  <li>🚫 <code>400</code> – Invalid verification link</li>
</ul>

<h3>🔑 5. Forgot Password</h3>
<pre><code>POST /forgot-password</code></pre>
<b>📤 Request Body (JSON):</b>
<pre>{
  "email": "user@example.com"
}</pre>
<b>📥 Responses:</b>
<ul>
  <li>✅ <code>200 OK</code> – Reset link sent</li>
  <li>❌ <code>404</code> – Email not found</li>
</ul>

<h3>📩 6. Reset Form</h3>
<pre><code>GET /reset?token=&lt;reset_token&gt;</code></pre>
<b>📄 Returns:</b> Password reset HTML form

<h3>🔁 7. Reset Password</h3>
<pre><code>POST /reset</code></pre>
<b>📤 Form Body (URL-encoded):</b>
<pre>
token=abc123&new_password=NewPass123
</pre>
<b>📥 Responses:</b>
<ul>
  <li>✅ <code>200 OK</code> – Password reset successful</li>
  <li>⚠️ <code>400</code> – Invalid or expired token</li>
</ul>

<h3>🧑‍💼 8. Update Profile</h3>
<pre><code>PUT /update-profile</code></pre>
<b>🪪 Headers:</b>
<pre>Authorization: Bearer &lt;JWT_TOKEN&gt;</pre>
<b>📤 Request Body (JSON):</b>
<pre>{
  "name": "New Name"
}</pre>
<b>📥 Responses:</b>
<ul>
  <li>✅ <code>200 OK</code> – Profile updated</li>
  <li>🔒 <code>401</code> – Missing or invalid token</li>
  <li>❓ <code>404</code> – User not found</li>
</ul>

<hr style="margin: 32px 0; border: none; border-top: 3px solid #ccc;">


<h2>🧪 Testing Instructions</h2>

<ol>
  <li>Ensure you're inside the project root directory:</li>
  <pre><code>cd C:\Users\YosiBenShushan\Desktop\HomeAssignment-DriveNets</code></pre>

  <li>Run all unit tests using the following command:</li>
  <pre><code>python -m unittest discover -s backend/tests</code></pre>

  <li>✅ The test suite uses <code>unittest</code> and auto-handles SQLite database setup (no manual DB creation needed).</li>
  
  <li>💡 Test files are located in: <code>backend/tests/</code></li>
</ol>

<hr style="margin: 32px 0; border: none; border-top: 3px solid #ccc;">

<h2>🖼️ Screenshots of the Application</h2>

<ul>
  <li><strong>🔐 Register Page:</strong></li>
  <img src="https://github.com/user-attachments/assets/bc49a1a4-b791-4095-b9f5-64cf354167bd" alt="Register Page" width="250"/>

  <li><strong>✅ Verification Success Email:</strong></li>
  <img src="https://github.com/user-attachments/assets/33b41a4a-f48e-4acd-baae-eac3f7995e53" alt="Email Verified Page" width="400"/>

  <li><strong>🔑 Login Page:</strong></li>
  <img src="https://github.com/user-attachments/assets/ea86b27b-d6f5-4041-9cdf-f760898624d7" alt="Login Page" width="250"/>

  <li><strong>📄 Dashboard (Authorized):</strong></li>
  <img src="https://github.com/user-attachments/assets/aebea70d-db82-40c3-a0e4-7699916edbee" alt="Dashboard" width="300"/>

  <li><strong>🔁 Forgot Password Page:</strong></li>
  <img src="https://github.com/user-attachments/assets/ef64d141-9c85-4515-a324-738bfe61a6bb" alt="Forgot Password Page" width="300"/>
</ul>

<hr style="margin: 32px 0; border: none; border-top: 3px solid #ccc;">

<h2>📝 Additional Notes or Assumptions</h2>

<ul>
  <li>📧 <strong>Email Delivery</strong>: During manual testing, verification and reset emails are actually sent — users must check their inbox to complete these flows. In unit tests, the <code>is_verified</code> flag is set manually in the database to bypass email verification.</li>

  <li>👤 <strong>User Roles</strong>: All users share the same permissions and functionality. There is no role-based access (e.g., admin vs. regular user).</li>

  <li>🔐 <strong>JWT Secret Key</strong>: The JWT <code>SECRET_KEY</code> is hardcoded in <code>config.py</code> for simplicity. In a real deployment, this should be managed via environment variables.</li>

  <li>⏱️ <strong>Rate Limiting</strong>: The login endpoint is limited to 3 attempts per minute using Flask-Limiter. This setting is primarily for demo/testing purposes and can be adjusted.</li>

  <li>🛡️ <strong>Password Strength Enforcement</strong>: Passwords must include at least:
    <ul>
      <li>1 uppercase character</li>
      <li>1 lowercase character</li>
      <li>1 number</li>
      <li>Length: 8–12 characters</li>
    </ul>
  </li>

  <li>🚧 <strong>Deployment Readiness</strong>: This app is a local demo intended for assignment purposes. It is not configured for production use.</li>
</ul>



