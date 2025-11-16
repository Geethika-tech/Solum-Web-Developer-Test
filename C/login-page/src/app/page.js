"use client";

import { useState } from "react";
import styles from "./page.module.css";
// Import icons to display in input fields
import { MdEmail } from "react-icons/md";
import { RiLock2Fill } from "react-icons/ri";
// Import toast for notifications
import toast from "react-hot-toast";
import { handleLogin } from "./utils/loginHandler";

// Sample credentials for demonstration
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
  const handleSubmit = (e) => {
      handleLogin({
        e,
        email,
        password,
        credentials, // Pass the credentials
        setError, // Pass the setter functions
        setHideForm, // Pass the setter functions
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
          <form className={styles.loginForm} onSubmit={handleSubmit}>
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
