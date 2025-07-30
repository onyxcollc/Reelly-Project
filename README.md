🏙️ Reelly Project – End-to-End Automation Framework
📲 Mobile & Web Automation | 🧪 Cross-Browser + Cloud Testing | 🧠 Dynamic Locator Handling
This automation framework validates core real estate workflows on the Reelly platform using Python, Selenium, 
and Behave (BDD). Tests simulate both desktop and mobile environments via Chrome Mobile Emulation and BrowserStack.

🚀 Features at a Glance
✅ BDD-style tests with Behave

✅ Modular design using the Page Object Model (POM)

✅ Chrome mobile emulation (e.g., iPhone SE, Nexus 5)

✅ Real device testing with BrowserStack

✅ Multi-browser compatibility (Chrome, Firefox, Edge)

✅ Headless mode support for CI/CD

✅ Dynamic selectors for React-driven UI

✅ Screenshots on failure for visual debugging


📁 Project Structure
<details> <summary>Click to expand</summary>
bash
Copy
Edit
Reelly-Project/
├── .venv/                  # Python virtual environment
├── app/                   # Application-level setup
├── features/              # .feature files + step definitions
├── pages/                 # Page Object Model classes
├── screenshots/           # Saved screenshots on failure
├── support/               # Hooks, logger, and utilities
├── test_results/          # JSON logs from executed runs
│   └── c2324d3f-*.json     # Dynamic result files
├── .gitignore             # Files to exclude from Git
├── README.md              # This file 👋
├── requirements.txt       # Python dependencies
├── test_automation.log    # Runtime logs from test executions
</details>
🧪 Test Coverage
💻 Desktop Web
✅ Validate "Announced" tags on property cards

✅ Navigate and verify "Off-Plan" properties

✅ Scroll-to-click in React-rendered elements

✅ Screenshot validation on all key flows

📱 Mobile Web
✅ Simulate mobile view with ChromeOptions

✅ Test on real Android devices via BrowserStack

✅ Check responsive layout + mobile element visibility

🌐 Cross-Browser Support
✅ Chrome (desktop + mobile emulation)

✅ Firefox

✅ Edge

✅ Headless execution

🧱 Roadblocks & Creative Fixes
🚧 Issue	💡 Solution
Off-Plan tab hidden in mobile/headless	Used execute_script() + scrollIntoView()
Dynamic tag elements failed with static locators	Built indexed + aria-label-based dynamic XPath
Inconsistent headless rendering	Applied fixed window size + visibility wait
Mobile viewport mismatch in BrowserStack	Tuned emulation settings for device parity
Firefox layout discrepancies	Added universal selector logic with waits

⚙️ How to Run the Project
📦 1. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🖥️ 2. Run in Chrome (Desktop)
🔧 In environment.py: Uncomment local Chrome block

bash
Copy
Edit
behave -i features/verify_announced.feature
🦊 3. Run in Firefox
🔧 Uncomment the Firefox driver section:

bash
Copy
Edit
behave -i features/verify_announced.feature
🧑‍💻 4. Run in Headless Mode
🔧 Uncomment the headless Chrome section:

bash
Copy
Edit
behave -i features/verify_announced.feature
📲 5. Run in Chrome Mobile Emulation
🔧 Uncomment the mobile emulation block (e.g. deviceName = "iPhone SE"):

bash
Copy
Edit
behave -i features/mobile_off_plan.feature
☁️ 6. Run on BrowserStack (Cloud Mobile Device)
✅ Already set up in environment.py
🧪 Device: Samsung Galaxy S22 Ultra | Platform: Android | Browser: Chrome
🔐 Credentials built into the URL config

bash
Copy
Edit
behave -i features/mobile_off_plan.feature
No extra flags needed.

🧠 Final Thoughts
The Reelly Automation Project combines cloud testing, dynamic UI validation,
and multi-device compatibility into a clean, scalable framework. 
With emulation, cross-browser support, and real-device runs on BrowserStack—this project
simulates the real-world user journey from discovery to verification.