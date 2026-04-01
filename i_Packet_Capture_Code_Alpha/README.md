 i) Build a Python Program to Capture Network Traffic Packets (Code Alpha)

**Objective**

To develop a basic network packet sniffer using Python without external libraries.

**Tools Used**

* Python (Built-in socket module)
* Command Prompt (Admin mode)

**Description**

This program captures network traffic packets using raw sockets. Due to Windows security restrictions, the implementation captures only ICMP packets (ping traffic).

**How It Works**

* Uses `socket.SOCK_RAW` for low-level packet capture
* Uses `IPPROTO_ICMP` to capture ICMP packets
* `recvfrom()` receives incoming packets from the network

**How to Run**

1. Open Command Prompt as Administrator
2. Navigate to file location
3. Run:

   ```
   python packet_sniffer.py
   ```
4. Generate traffic using:

   ```
   ping google.com
   ```

**Limitations**

* Only ICMP packets are captured
* Requires administrator privileges
* Limited support on Windows OS
 Output

Displays source address and raw packet data.

Conclusion

A basic packet sniffer can be implemented using Python’s socket module, demonstrating low-level network programming.

