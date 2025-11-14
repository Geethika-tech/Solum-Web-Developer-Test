# Simple Login Page

A responsive login page built using **HTML, CSS, and JavaScript** (with React and Next.js support).  
This project demonstrates client-side form validation and conditional rendering for a mock authentication flow — no backend required.

---

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

---

## 🛠️ Project Structure

(login-page/src/app)
│
├── layout.js # Main layout component
├── page.module.css # Styling for layout and responsiveness
├── Page.js # Form logic, validation, and login handling
├── Public/ # Images
└── globals.css # Global styles

---

## ⚙️ Setup Instructions

### 1. Clone or Download
```bash
git clone https://github.com/Geethika-tech/Solum-Web-Developer-Test.git
cd C/login-page
2. Open in Browser
You can open the project directly without any build tools:

Run a local server:

bash
Copy code
npx serve .
Then visit http://localhost:3000.

💡 How It Works
The app checks the entered email against a small list of valid emails:

js
Copy code
const credentials = [{ email: "test@example.com", password: "Test@1234" }];
Passwords are validated using a regex for length and complexity.

On success, the form hides and displays a welcome message:

bash
Copy code
Welcome, test@example.com!
Clicking “Logout” resets the form and shows the login page again.

📱 Responsive Design
Uses CSS Flexbox and media queries for smooth resizing.

Layout and font sizes automatically adapt for smaller screens (< 400px).

🧩 Technologies Used
HTML5 for structure

CSS3 (with gradients, shadows, and responsive media queries)

JavaScript (ES6) for validation logic and dynamic UI updates

🧪 Validation Example
Test Case	Expected Result
Empty email or password	Show error message
Invalid email	"Email does not exist"
Weak password	"Password must be 8–16 characters, include uppercase, lowercase, number, and symbol"
Wrong password	"Incorrect password"
Valid credentials	Show welcome message

👩‍💻 Author
Geethika Pidikiti
Feel free to reach out for any questions or suggestions!