"use client";

import { useState } from "react";
import styles from "./page.module.css";
// Import icons to display in input fields
import { MdEmail } from "react-icons/md";
import { RiLock2Fill } from "react-icons/ri";
// Import toast for notifications
import toast from "react-hot-toast";

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

    setError(""); // clear previous errors

    // Trimmed inputs for reliable validation
    const trimmedEmail = email.trim();
    const trimmedPassword = password.trim();

    // --- Validation Checks ---
    if (!trimmedEmail || !trimmedPassword) {
      setError(
        !trimmedEmail && !trimmedPassword
          ? "Email and password cannot be empty"
          : !trimmedEmail
          ? "Email cannot be empty"
          : "Password cannot be empty"
      );
      return;
    }

    // Check if email exists
    const user = credentials.find((cred) => cred.email === trimmedEmail);
    if (!user) {
      setError("Email does not exist");
      return;
    }

    // Password criteria check
    const passwordRegex =
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]).{8,16}$/;
    if (!passwordRegex.test(trimmedPassword)) {
      setError(
        "Password must be 8–16 characters, include uppercase, lowercase, number, and symbol"
      );
      return;
    }

    // Verify password
    if (user.password !== trimmedPassword) {
      setError("Incorrect password");
      return;
    }

    // --- Successful Login ---
    setHideForm(true);
    setError(""); // clear error

    toast.success(`Welcome, ${trimmedEmail}!`, {
      duration: 3000,
      position: "top-center",
    });
  };

  // Handle logout
  const handleLogout = () => {
    // Toggle form visibility and reset fields
    setHideForm(false);
    setEmail("");
    setPassword("");
    toast('Logged out successfully.', {
        icon: '👋', // A friendly icon for logout
        position: 'top-center'
    });
  };

  // Handles form reset by resetting all fields and errors
  const handleReset = () => {
  setEmail("");
  setPassword("");
  setError("");
  }
  // Renders the login form or welcome message based on state

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

            <button
             type="button"
             className={styles.button}
             onClick={handleReset}
             >
             Reset
            </button>

          </form>
        )}
      </main>
    </div>
  );
}