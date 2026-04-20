<p align="center">
  <img src="banner.png" alt="Pyrus Banner" width="100%">
</p>

<p align="center">
  <a href="https://security-labor.github.io/pyrus/">
    <img src="https://img.shields.io/badge/docs-security--labor.github.io%2Fpyrus-8b5cf6" alt="Official Docs">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python: 3.8+">
  </a>
  <a href="https://github.com/Security-Labor/Pyrus">
    <img src="https://img.shields.io/badge/status-pre--alpha-red" alt="Status: Pre-Alpha">
  </a>
</p>

# 🏺 Pyrus Programming Language (v0.1.0.0 Alpha)


**Pyrus** is a systems-oriented programming language designed for engineers and automation experts. It bridges the gap between the rapid prototyping of Python and the strict, safe execution required for industrial and security applications.



---

## 🚀 The Core Vision
Pyrus was born within the **Security-Labor** ecosystem to provide a tool that is:
- **Predictable:** Strict syntax with mandatory semicolons.
- **Math-Heavy:** High-precision handling for engineering calculations (Flow, Pressure, Network Load).
- **Concurrent:** Designed from the ground up for `spawn` operations and asynchronous tasks.
- **Extensible:** Seamless integration with Python-based tools and future LLVM compilation.

## ✨ Features (v0.1.0.0)
- **Hybrid Type System:** Automatic detection of `String`, `Int`, and `Float`.
- **Recursive Math Engine:** Support for complex expressions like `var x = (a + b) * (c / d);`.
- **Developer CLI:** A robust command-line interface for running `.pyu` files.
- **Comments Support:** Integrated `//` syntax for code documentation.

## 🛠️ Quick Start

### 1. Installation
Pyrus requires the **Lark** parsing engine. Install it via terminal (Termux, CMD, or Linux):

```bash
pip install lark
```

2. Your First Script (main.pyu)
Create a file with the .pyu extension:
// Pyrus Automation Example
```bash
var target = "192.168.1.1";
var base_freq = 60;
var multiplier = 1.5;

var final_freq = base_freq * multiplier;

print("Target System:");
print(target);
print("Calibrated Frequency:");
print(final_freq);
```

3. Running the Code
Navigate to the src folder and execute:
```bash
python pyrus.py run ../examples/main.pyu
```

🗺️ Roadmap to \pi
 * [x] v0.0.0.0: Lexer/Parser Proof of Concept.
 * [x] v0.1.0.0: Math Engine & Numeric Types.
 * [ ] v0.2.0.0: Logic Flow (if/else) and Boolean Algebra.
 * [ ] v0.3.0.0: Loops (while, for) and List structures.
 * [ ] v0.5.0.0: Memory Ownership & Borrowing System.
 * [ ] v1.0.0.0: Native LLVM Backend Integration.

🛡️ Security & Labor
Pyrus is an open-source project maintained by the Security-Labor Foundation. We believe in tools that empower the user through transparency and performance.

 * Website: AAD-Systems.github.io/pyrus
 * Organization: github.com/AAD-Sytems

Developed in Alagoas, Brazil. 🇧🇷
