"use client";

import { useState } from "react";
import styles from "./page.module.css";
import { MdEmail } from "react-icons/md";
import { RiLock2Fill } from "react-icons/ri";
import toast from "react-hot-toast"; // 1. IMPORT THE TOAST FUNCTION

// Simulated credentials
const credentials = [
  { email: "test@example.com", password: "Test@1234" },
  { email: "user@example.com", password: "User@5678" },
];

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [hideForm, setHideForm] = useState(false);

  // Handle login form submission
  const handleLogin = (e) => {
    e.preventDefault();
    setError(""); // Clear previous errors at the start of submission

    // Input Validation Checks (Error Toasts)
    if (!email.trim() && !password.trim()) {
      setError("Email and password cannot be empty");
     // Show Error Toast
      return;
    } else if (!email.trim()) {
      setError("Email cannot be empty");
       // Show Error Toast
      return;
    } else if (!password.trim()) {
      setError("Password cannot be empty");
     // Show Error Toast
      return;
    }

    // Find user by email
    const user = credentials.find((cred) => cred.email === email);
    if (!user) {
      setError("Email does not exist");

      return;
    }

    // Password validation regex
    const passwordRegex =
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]).{8,16}$/;
    if (!passwordRegex.test(password)) {
      setError(
        "Password must be 8-16 characters, include uppercase, lowercase, number, and symbol"
      );

      return;
    }

    // Check password correctness
    if (user.password !== password) {
      setError("Incorrect password");

      return;
    }

    // Successful login
    setHideForm(true);

    // 2. ***** REPLACE alert() WITH toast.success() *****
    toast.success(`Welcome, ${email}!`, {
      duration: 3000,
      position: 'top-center', // Ensure it uses your desired position

    });
    // *************************************************

    setError(""); // clear previous error
    // Removed: alert("Login successful!");
  };

  // Handle logout
  const handleLogout = () => {
    setHideForm(false);
    setEmail("");
    setPassword("");
    toast('Logged out successfully.', {
        icon: '👋', // A friendly icon for logout
        position: 'top-center'
    });
  };

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        {hideForm ? (
          <div className={styles.welcome}>
            <h1>Welcome {email}!</h1>
            <h3>You have successfully logged in.</h3>
            <button
              type="button"
              onClick={handleLogout}
              className={styles.button}
            >
              Logout
            </button>
          </div>
        ) : (
          <form className={styles.loginForm} onSubmit={handleLogin}>
            <h1 className={styles.heading}>Login</h1>

           <div className={styles.inputGroup}>
           <MdEmail className={styles.icon} />
            <input
              type="email"
              placeholder="Email"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className={styles.inputField}
              required
            />
              </div>

           <div className={styles.inputGroup}>
              <RiLock2Fill className={styles.icon} />
            <input
              type="password"
              placeholder="Password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className={styles.inputField}
              required
            />
            </div>
            <a href="#" className={styles.forgotPasswordLink}>
                Forgot Password?
            </a>

            <p className={`${styles.error} ${!error ? styles.hidden : ''}`}>{error}</p>

            <button
              type="submit"
              className={styles.button}
            >
              Login
            </button>
          </form>
        )}
      </main>
    </div>
  );
}