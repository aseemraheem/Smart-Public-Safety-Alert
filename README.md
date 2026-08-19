# 🚦 Smart Public Safety Alert — AI Traffic Control System

A Python-based console application that simulates an **intelligent 4-way traffic light controller**, capable of handling normal AI-driven traffic flow, emergency vehicle overrides, and priority vehicle overrides — complete with live countdown timers and color-coded terminal output.

![Demo](assets/demo-terminal-output.png)

---

## 📖 Overview

Traffic congestion and emergency response delays are real public safety concerns. **Smart Public Safety Alert** models how a smart traffic junction could dynamically respond to real-world conditions:

- 🚑 Instantly clear a path for **emergency vehicles** (ambulance, fire, police)
- 🚓 Give right-of-way to **priority vehicles**
- 🤖 Let an **AI controller** decide which direction gets the green light during normal operation, based on live traffic density

The entire simulation runs in the terminal with color-coded signals (via `colorama`) and real-time countdown timers.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **AI-Based Decision Making** | `AIController` analyzes vehicle counts from all four directions and grants green light to the busiest lane |
| 🚨 **Emergency Override** | Instantly sets all lights to red and gives the emergency direction a 15-second green window |
| ⭐ **Priority Vehicle Handling** | Grants a 12-second green light to a chosen direction for priority traffic |
| ⏱️ **Live Countdown Timer** | Real-time, self-updating countdown displayed in the terminal for every green signal |
| 🎨 **Color-Coded Console UI** | Green, red, cyan, and magenta terminal colors (via `colorama`) for instant visual feedback |
| 🧭 **4-Way Junction Simulation** | Independently modeled `North`, `South`, `East`, and `West` traffic lights |
| 📋 **Interactive Menu** | Simple CLI menu to switch between Normal, Emergency, and Priority modes |

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Library:** [`colorama`](https://pypi.org/project/colorama/) — cross-platform colored terminal text
- **Paradigm:** Object-Oriented Programming (OOP)

---

## 🏗️ Project Architecture

```
project.py
├── countdown(seconds)          # Reusable countdown timer utility
│
├── class TrafficLight
│   ├── __init__(direction)     # Initializes a light for a given direction
│   ├── set_green(duration)     # Turns light green + starts countdown
│   └── set_red()               # Turns light red
│
├── class AIController
│   └── decide_priority(data)   # Picks the direction with highest traffic count
│
└── class TrafficController
    ├── lights{}                # Dict of all 4 TrafficLight objects
    ├── ai                      # AIController instance
    ├── reset_all()             # Sets every light to red
    ├── handle_emergency()      # 15s override for emergency vehicles
    ├── handle_priority()       # 12s override for priority vehicles
    ├── normal_operation()      # Collects traffic data → AI decides
    └── run()                   # Main menu loop
```

### 🔄 How It Works

1. **`TrafficController`** initializes four `TrafficLight` objects — one per direction — all starting at **RED**.
2. The **main menu** (`run()`) lets the user choose one of four modes:
   - `1` → Normal Operation (AI)
   - `2` → Emergency Vehicle
   - `3` → Priority Vehicle
   - `4` → Exit
3. In **Normal Operation**, the user enters live vehicle counts for each direction. The `AIController` picks the direction with the maximum count using `max(traffic_data, key=traffic_data.get)` and turns it green.
4. In **Emergency** or **Priority** mode, all lights reset to red, and the chosen direction turns green for a fixed duration (15s / 12s respectively) while a live countdown runs in the console.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### Installation

```bash
# 1. Clone or download the project
git clone <your-repo-url>
cd smart-public-safety-alert

# 2. Install dependencies
pip install colorama
```

### Run the Application

```bash
python project.py
```

---

## 💻 Usage

Once launched, you'll be greeted with the main menu:

```
===== TRAFFIC CONTROL MENU =====
1. Normal Operation (AI)
2. Emergency Vehicle
3. Priority Vehicle
4. Exit
Enter your choice:
```

**Example — Emergency Mode:**

```
Enter your choice: 2
Enter direction for Emergency (North/South/East/West): South

🚨 Emergency Activated!
North light is RED
South light is RED
East light is RED
West light is RED
South light is GREEN for 15 seconds
Time remaining: 9 seconds
```

---

## 📸 Screenshots

> ℹ️ Make sure the `assets/` folder sits in the **same directory** as this `README.md` (i.e. project root) when you upload to GitHub — the images below are linked relatively.

<table>
<tr>
<td width="50%">

**Traffic Light & AI Controller Logic**
![Traffic Light Class](assets/code-traffic-light-class.png)

</td>
<td width="50%">

**Traffic Controller — Emergency & Priority Handling**
![Traffic Controller](assets/code-traffic-controller.png)

</td>
</tr>
<tr>
<td width="50%">

**Main Menu Loop**
![Menu Loop](assets/code-menu-loop.png)

</td>
<td width="50%">

**Live Demo Output**
![Demo Output](assets/demo-terminal-output.png)

</td>
</tr>
</table>

---

## 🗺️ Roadmap / Future Enhancements

- [ ] Add GUI using Tkinter or Pygame for visual traffic light simulation
- [ ] Log all events (emergency triggers, AI decisions) to a file for auditing
- [ ] Integrate real sensor / camera data instead of manual input
- [ ] Add pedestrian crossing signals
- [ ] Support multi-junction networks
- [ ] Unit tests for `AIController` decision logic

---

## 👤 Author

**Aseem Raheem**

Built as part of a **Smart Public Safety Alert** initiative — exploring how simple AI logic can improve traffic management and emergency response times.

---

## 📄 License

This project is open-source and available for educational and personal use. Feel free to fork, modify, and build upon it.

---

<p align="center">Made with 🚦 and Python</p>
