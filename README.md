# 🔥 Pyrus Programming Language (v0.0.0.0)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-0.0.0.0--alpha-red)

**Pyrus** is an emerging systems programming language designed to combine the ergonomics of high-level scripting with the memory safety and performance of low-level languages.

---

## 🚀 The Vision
Pyrus was born from the need for a language that feels like Python but behaves like Go/Rust. 
- **Extension:** `.pyu`
- **Core Philosophy:** If it's not safe, it shouldn't compile.

## ✨ Key Features (Roadmap)
* **Memory Safety:** Ownership system without a Garbage Collector (GC).
* **Concurrency:** Native `spawn` keyword for green-threads.
* **Interoperability:** Easy C/Python FFI (Foreign Function Interface).
* **Engine:** Built on top of LLVM for aggressive optimization.

## 🛠️ Installation (Preview)

Currently in **Pre-Alpha (v0.0.0.0)**. To test the core interpreter:

```bash
# Clone the repository
git clone [https://github.com/pyrus-lang/pyrus.git](https://github.com/pyrus-lang/pyrus.git)

# Install dependencies
pip install lark

# Run a sample script
python pyrus.py run examples/hello_world.pyu
