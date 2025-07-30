# 🏠  REE⎯LLY PROJECT – END-TO-END AUTOMATION FRAMEWORK 

> 📲 **Mobile & Web Automation** &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 🧪 **Cross-Browser + Cloud Testing** &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 🧠 **Dynamic Locator Handling**

---

This automation framework validates core real estate workflows on the **Reelly** platform using:

**`Python` + `Selenium` + `Behave (BDD)`**

💻 Simulates **Desktop** and **Mobile** environments using **Chrome Emulation** and **BrowserStack** real devices.

---

## 🚀 FEATURES AT A GLANCE

✨ **BDD-style tests** with `Behave`  
🧩 **Page Object Model (POM)` structure**  
📱 **Mobile emulation** (iPhone SE, Nexus 5, etc.)  
📲 **Real-device testing** via `BrowserStack`  
🌐 **Multi-browser support**: Chrome, Firefox, Edge  
👻 **Headless mode** for CI/CD pipelines  
🧠 **Dynamic selectors** for React-driven UI  
📸 **Auto-screenshots** on failure  

---

## 📁 PROJECT STRUCTURE

Reelly-Project/
├── .venv/ → Python virtual environment
├── app/ → App-level config
├── features/ → Feature files + step definitions
├── pages/ → Page Object classes (POM)
├── screenshots/ → Failure screenshots
├── support/ → Hooks, logger, utilities
├── test_results/ → JSON result logs
├── requirements.txt → Project dependencies
├── test_automation.log → Automation logs
├── README.md → You’re looking at it ✅

yaml
Copy
Edit

---

## 🧪 TEST COVERAGE

### 💻 Desktop Web
- ✅ Validate **`Announced`** tags  
- ✅ Navigate + verify **Off-Plan** properties  
- ✅ Scroll-to-click in dynamic React components  
- ✅ Capture screenshots for all key flows  

### 📱 Mobile Web
- ✅ Emulate devices using `ChromeOptions`  
- ✅ Run real Android tests on **BrowserStack**  
- ✅ Validate responsive layout & visibility  

### 🌐 Cross-Browser Support
- ✅ Chrome (desktop + mobile)  
- ✅ Firefox  
- ✅ Edge  
- ✅ Headless  

---

## 🧱 ROADBLOCKS & CREATIVE FIXES

| ⚠️ Issue | ✅ Solution |
|---------|-------------|
| Off-Plan tab hidden on mobile/headless | Used `scrollIntoView()` + `execute_script()` |
| Static locators failed | Built dynamic XPath w/ `aria-labels` & indexing |
| Headless rendering issues | Set fixed window size + added visibility waits |
| Mobile mismatch in BrowserStack | Tuned emulation for pixel-perfect parity |
| Firefox layout quirks | Added flexible universal selector logic |

---

## ⚙️ HOW TO RUN THIS PROJECT

### 📦 1. Install Dependencies

```bash
pip install -r requirements.txt
💻 2. Run in Chrome (Desktop)
Uncomment the Chrome section in environment.py:

bash
Copy
Edit
behave -i features/verify_announced.feature
🦊 3. Run in Firefox
Uncomment the Firefox driver section:

bash
Copy
Edit
behave -i features/verify_announced.feature
👤 4. Run in Headless Mode
Uncomment the headless Chrome block:

bash
Copy
Edit
behave -i features/verify_announced.feature
📲 5. Run Chrome Mobile Emulation
Uncomment the mobile emulation block (e.g. iPhone SE):

bash
Copy
Edit
behave -i features/mobile_off_plan.feature
☁️ 6. Run on BrowserStack (Real Device)
✅ Already pre-configured in environment.py
🧪 Device: Samsung Galaxy S22 Ultra
🔐 Credentials embedded via URL config

bash
Copy
Edit
behave -i features/mobile_off_plan.feature

🧠 FINAL THOUGHTS
The Reelly Automation Framework blends:

✅ Cloud testing
✅ Real-device validation
✅ Mobile emulation
✅ Multi-browser support
✅ React UI interaction

Into one powerful, scalable automation suite.

This simulates a true end-user journey across platforms — making it ready for the real world.


