Switch-Security-Configuration-Port-Security

A Python-based automation tool designed to secure Cisco network switch ports using the Netmiko library. This script automates the process of hardening network interfaces, helping administrators save time and ensure consistent security policies across their infrastructure.

Overview

Managing manual security configurations on switch ports can be tedious and prone to errors. This tool connects to a Cisco IOS device and automatically applies Port Security settings, such as limiting MAC addresses and setting violation responses, to protect your network from unauthorized access.

Key Features

Automated Hardening: Quickly applies security settings to any specified interface.

Sticky MAC Support: Enables sticky learning to dynamically secure connected devices.

Violation Protection: Configured to automatically shut down the port if a security policy is violated.

Easy to Use: A simple script structure that is easy to read and modify.

Prerequisites

Before running the script, ensure you have:

Python 3.x installed.

The Netmiko library:
pip install netmiko

How to Use

Clone the repository:
git clone https://github.com/your-username/Switch-Security-Configuration-Port-Security.git

Configure your device: Open the script and update the device dictionary with your specific switch IP, credentials, and secret password.

Run the script:
python SecurePort-Automator

Safety Warning

This script is intended for lab and educational purposes. Always test your automation scripts in a safe, non-production environment before applying them to live switches to prevent accidental network disruption.
