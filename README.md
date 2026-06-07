⚠️ Legal & Ethical Disclaimer
This repository is published exclusively for educational purposes, academic research, and authorized penetration testing exercises. Utilizing this code to gain unauthorized access to target environments without explicit, written consent is strictly illegal and subject to criminal prosecution.



# leader-ssh-vic
# Interactive Reverse SSH Shell Client (Firewall Bypass)

A specialized Python-based **Reverse SSH Shell Client** utilizing the **Paramiko** library and native system processes (`subprocess`). This tool is engineered to demonstrate advanced post-exploitation techniques, specifically focusing on **Outbound Traffic Exploitation** to bypass strict inbound firewall rules.

---

## 🚀 Features

* **Firewall Evasion (Outbound Connection):** Instead of waiting for an incoming connection (which is usually blocked by firewalls), this script initiates a secure connection from inside the victim's network back to the attacker's listener.
* **Full Interactive Shell:** Establishes a persistent `while True` loop, transforming the SSH tunnel into a live, interactive command-line interface.
* **Robust Error Resilience (Anti-Crash):** Wrapped in a multi-layered `try-except` architecture. If an invalid OS command is executed, the script catches the execution error, safely transfers the error log back to the attacker, and keeps the shell alive.
* **Automated Key Caching:** Implements `AutoAddPolicy` for seamless, non-interactive host key validation.

---

## 🧠 Architectural Logic & Data Flow



1. **The Outbound Request:** The client script executes on the target machine (e.g., Windows Host) and actively connects to the attacker’s remote listening server (e.g., Kali Linux).
2. **Channel Promotion:** Once authenticated, it triggers `open_session()` to spawn a dedicated sub-channel inside the encrypted SSH Transport layers.
3. **The Command Loop:** The script enters an infinite listening state (`session.recv`).
4. **Local Execution:** Upon receiving an encrypted payload (command string), it utilizes `shlex.split()` to safely parse the arguments, then feeds them to `subprocess.check_output(shell=True)`.
5. **Dynamic Feedback:** * **On Success:** The standard command output (`stdout`) is captured and sent back through the secure channel.
   * **On Failure:** The exception text is stringified, encoded into raw bytes, and sent back, ensuring the shell does not drop or crash.
6. **Volatile Cleanup:** Upon receiving the custom string `'exit'`, the execution loop breaks, and the `finally` block gracefully terminates the socket connection.

---

## 🛠️ Prerequisites & Dependencies

The target system requires Python 3.x and the Paramiko library installed:

```bash
pip install paramiko


