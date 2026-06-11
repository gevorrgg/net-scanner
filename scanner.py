from concurrent.futures import ThreadPoolExecutor, as_completed
from printing import print_usage, print_header, print_scan_results
from parser import parse_args
from icmp import is_icmp_reachable
from tcp import connect


def scan_ports(target, ports):
    open_ports = []

    for port in ports:
        if connect(target, port):
            open_ports.append(port)

    return open_ports


def scan(target, ports):   
    scan_results = {}

    scan_results["icmp_reachable"] = is_icmp_reachable(target)

    open_ports = scan_ports(target, ports)

    scan_results["tcp_reachable"] = len(open_ports) > 0

    scan_results["open_ports"] = open_ports

    return scan_results

def expand_targets(networks):
    for network in networks:
        yield from network

def network_scanner(scan_configs):
    networks = scan_configs["targets"]
    ports   = scan_configs["ports"]

    results = {}

    targets = expand_targets(networks)

    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_target = {
            executor.submit(scan, t, ports): (t)
            for t in targets
        }

        # collecting results of ready tasks
        for future in as_completed(future_to_target):
            target = future_to_target[future]
            results[target] = future.result()
            

    return dict(sorted(results.items(), key=lambda x: x[0]))