# Aadhar-token-desk

Aadhaar Card Portal - Flask Application This project is a simple Aadhaar Card Assistance web application built using Python (Flask), MySQL, and JavaScript. It allows users to:

✔ Sign up with their name and email ✔ Submit update requests with document upload ✔ Get a token and downloadable receipt ✔ Interact with a built-in AI Chatbot for quick Aadhaar-related FAQs

🖥️ Project Screenshots

Home Page

Sign-up Confirmation
![AADHAR](https://github.com/user-attachments/assets/d78e799d-4a6d-446a-9d66-867395963722)

My-Sql Dashboard when Signed-up
![AADHAR 2](https://github.com/user-attachments/assets/9da0aba9-0ff0-4d94-a67a-562ecab9fc37)

Token Generation Section
![AADHAR](https://github.com/user-attachments/assets/69c2bf14-b64a-474f-a3df-b99a7af2563d)

AI Chatbot

✅ Replace the images above with your actual site screenshots saved in an images folder in your project.

⚙️ Technologies Used Python 3.9+

Flask

Flask-CORS

MySQL

HTML, CSS, JavaScript

AI Chatbot powered by OpenRouter API

🚀 Setup Instructions Follow these steps to run the project locally:

Clone the Repository git clone https://github.com/your-username/aadhaar-card-portal.git cd aadhaar-card-portal

Install Python Dependencies Make sure you have Python installed. Then run:

pip install -r requirements.txt

MySQL Database Setup Create a MySQL database named: Aadhar Card
Run the following SQL to create the users table:

CREATE TABLE users ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL );

Update your database credentials inside app.py:

db_config = { 'host': 'localhost', 'user': 'root', 'password': 'YourPassword', 'database': 'Aadhar Card' }

Run the Flask Application python app.py
The app will be available at: http://127.0.0.1:5000

🧩 Project Structure app.py → Flask backend

templates/ → HTML files

static/ → CSS, JS, Images

requirements.txt → Python dependencies

render.yaml → Deploy configuration for Render

images/ → Screenshots for README

🌐 Deployment This project is ready to be deployed on Render or similar platforms. Make sure to update your render.yaml with correct environment variables.

💡 Notes The AI Chatbot requires a valid OpenRouter API key. Replace it in the JavaScript code.

Token generation is done on the client side for demonstration purposes.

This project is for educational/demo use and not production-grade security.
