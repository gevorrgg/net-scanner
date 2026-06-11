def alive(scan_result):
    return (
        scan_result.get("icmp_reachable", False) or
        scan_result.get("arp_reachable", False) or
        scan_result.get("tcp_reachable", False)
    )

def print_header():
    print("=================================")
    print("      NETWORK SCANNER")
    print("=================================")

def print_scan_results(results):
    for target, res in results.items():
        print("\n-----------------------------")
        print(f"Target  : {target}")

        alive_state = alive(res)

        print(f"Alive   : {alive_state}")

        #print(f"  ARP  : {res['arp_reachable']}")
        print(f"  ICMP  : {res['icmp_reachable']}")
        print(f"  TCP   : {res['tcp_reachable']}")

        if res["open_ports"]:
            print(f"  Open ports: {', '.join(map(str, res['open_ports']))}")
        else:
            print("  Open ports: none")


def print_usage():
    print("""
network_scanner usage:

    python scanner.py <targets> [options]

Targets:
    192.168.1.1
    192.168.1.0/24
    10.0.0.1-10.0.0.50

Options:
    --ports <ports>
        examples:
            --ports 22
            --ports 22,80,443
            --ports 1-1024
            --ports 22,80-90,443

    --mode <mode>
        available:
            fast   - scan primary ports only
            deep   - scan full port range (0-65535)

Examples:
    python scanner.py 192.168.1.0/24 --ports 22,80,443
    python scanner.py 10.0.0.1-10.0.0.50 --mode fast
    python scanner.py 192.168.1.10 --mode deep
""")