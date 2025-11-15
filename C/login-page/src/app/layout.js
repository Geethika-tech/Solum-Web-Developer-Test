// app/layout.js
import './globals.css';
//Import Toaster for notifications
import { Toaster } from 'react-hot-toast';

export const metadata = {
  title: 'My App',
  description: 'Login page',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
     <body>
      <Toaster
       position="top-center"
       reverseOrder={false}
       />
      {children}
     </body>
    </html>
  );
}
