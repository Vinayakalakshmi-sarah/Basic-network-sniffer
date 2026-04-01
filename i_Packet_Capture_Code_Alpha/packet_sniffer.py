import socket

def main():
    try:
        host = socket.gethostbyname(socket.gethostname())
        print("Your IP:", host)

        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sniffer.bind((host, 0))

        print("Sniffing started... (ICMP packets only)")
        print("Press Ctrl + C to stop\n")

        while True:
            raw_data, addr = sniffer.recvfrom(65535)
            print("Packet received from:", addr)
            print("Raw Data:", raw_data[:50])
            print("-" * 50)

    except KeyboardInterrupt:
        print("\nSniffing stopped.")

if __name__ == "__main__":
    main()
