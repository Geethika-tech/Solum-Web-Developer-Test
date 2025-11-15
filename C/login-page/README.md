# Simple Login Page

A responsive login page built using **HTML, CSS, and JavaScript** (with React and Next.js support).  
This project demonstrates client-side form validation and conditional rendering for a mock authentication flow — no backend required.


## Project Structure

(login-page/src/app)
1. **layout.js**:Main layout component
2. **page.module.css**:Styling for layout and responsiveness
3. **Page.js**:Form logic, validation, and login handling
4. **globals.css**:Global styles

## Setup Instructions

Clone or Download:
1. Clone the code using the command: **git clone https://github.com/Geethika-tech/Solum-Web-Developer-Test.git** or download the code from github repo and extract the zip files and open it in any code editor.
2. Navigate to the project folder using: **cd C/login-page** (After navigating to Solumn-Web-Developer-Test folder)
3. Install the necessary dependencies using the command: **pnpm install** or **npm install** based on package manager being used.

## Run Instructions
Run a local server:
1. Use the following command: **pnpm dev** or **npm run dev**.
2. Then visit **http://localhost:3000** in web browser. A login form is displayed in the center of the webpage.

## How It Works
The app checks the entered email against a small list of valid emails:

const credentials = [{ email: "test@example.com", password: "Test@1234" or email:"user@example.com", password: "User@5678" }].
Passwords are validated using a regex for length and complexity.

On success, the form hides and displays a welcome message:

Welcome, test@example.com!
Clicking “Logout” resets the form and shows the login page again.

Responsive Design
Uses CSS Flexbox and media queries for smooth resizing.

Layout and font sizes automatically adapt for large, medium and smaller screens.

## Features

- **Simple layout:** Centered login form with email and password inputs.
- **Responsive design:** Works smoothly on both desktop and mobile screens.
- **Validation rules:**
    - Email must not be empty and must exist in a simulated list (e.g. `["test@example.com"]`).
    - Password must:
        - Be between **8–16 characters**
        - Contain **one uppercase**, **one lowercase**, **one number**, and **one symbol**
    - Displays error messages for invalid input or incorrect credentials.
- **Successful login:** Displays a personalized welcome message with a Logout button.
- **Notifications:** Notifies users of successful login and logout.
- **Logout:** Returns to the login form.


