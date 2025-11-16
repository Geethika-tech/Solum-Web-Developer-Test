// src/utils/loginHandler.js

import { toast } from "react-hot-toast"; // Assuming you import toast in your original file


// Regular expression for password validation
const passwordRegex =
  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]).{8,16}$/;

/**
 * Handles the login logic.
 * @param {Object} params
 * @param {Event} params.e - The form submission event.
 * @param {string} params.email - The current email input value.
 * @param {string} params.password - The current password input value.
 * @param {Array<Object>} params.credentials - The list of user credentials.
 * @param {function} params.setError - State setter for error message.
 * @param {function} params.setHideForm - State setter to hide the form on success.
 */
export const handleLogin = ({
  e,
  email,
  password,
  credentials,
  setError,
  setHideForm,
}) => {
  e.preventDefault();

  setError(""); // Clear previous errors

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

  // Password criteria check using regular expression
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