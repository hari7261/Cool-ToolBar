# **Cool ToolBar**

The **Cool ToolBar** is a sleek, modern, and fully-featured desktop application designed to keep you organized and informed. Built with Python and Tkinter, this floating toolbar stays always on top of your desktop, providing quick access to essential tools like date display, weather updates, task reminders, text-to-speech functionality, and countdown timers. Whether you're managing your daily tasks or planning for future events, the Cool ToolBar is your go-to productivity companion.

---

## **Features**

### **1. Show Current Date**
- Displays the current date in a clean and readable format (e.g., "Monday, October 30, 2023").
- Automatically updates in real-time.

### **2. Weather Updates**
- Fetches real-time weather information for your city using the **OpenWeatherMap API**.
- Displays weather conditions (e.g., "Sunny, 25°C") in a user-friendly format.
- Automatically refreshes every minute to keep you updated.

### **3. Task Reminders**
- Add and manage task reminders directly from the toolbar.
- Never miss an important task or deadline again.

### **4. Text-to-Speech (Read Aloud)**
- Uses a built-in text-to-speech engine to read the current date aloud.
- Perfect for quick updates without needing to look at the screen.

### **5. Countdown Timer**
- Set countdown timers for important events or deadlines.
- Displays the time remaining in a clear and easy-to-read format.

### **6. Always-On-Top Floating Toolbar**
- The toolbar stays always on top of your desktop, ensuring quick and easy access.
- Compact and minimalistic design to avoid cluttering your workspace.

---

## **Why Cool ToolBar?**
- **All-in-One Tool**: Combines multiple productivity features into a single, easy-to-use interface.
- **Customizable**: Change the city for weather updates, customize the appearance, and more.
- **Lightweight**: Built with Python and Tkinter, it’s lightweight and runs smoothly on any system.
- **Open Source**: Fully open-source, so you can customize and extend it to suit your needs.

---

## **Requirements**
To run the Cool ToolBar, you need the following:
- **Python 3.x**
- **Required Python Libraries**:
  ```bash
  pip install tkinter requests pyttsx3
  ```
- **OpenWeatherMap API Key**: Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).

---

## **Installation**
1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/yourusername/cool-toolbar.git
   cd cool-toolbar
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Your API Key**:
   - Open the `cool_toolbar.py` file.
   - Replace `"your_openweathermap_api_key"` with your actual API key.

4. **Run the Application**:
   ```bash
   python cool_toolbar.py
   ```

---

## **How to Use**
1. **Floating Toolbar**:
   - The toolbar will appear as a small, always-on-top window on your desktop.

2. **Access Features**:
   - **Show Date**: Click to display the current date in a pop-up.
   - **Show Weather**: Click to fetch and display the current weather.
   - **Add Task Reminder**: Add and manage tasks directly from the toolbar.
   - **Read Date Aloud**: Click to hear the current date read aloud.
   - **Set Countdown Timer**: Set a countdown for any event or deadline.


3. **Customization**:
   - Change the city for weather updates by editing the `city` variable in the script.
   - Customize the appearance (colors, fonts, etc.) by modifying the Tkinter styles in the code.

---


## **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Contact**
- **GitHub**: [yourusername](https://github.com/hari7261)

---

## **Enjoy the Cool ToolBar!**
Stay organized, informed, and productive with the Cool ToolBar. Give it a try and let us know what you think! 🚀
