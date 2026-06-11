#!/usr/bin/env python3
import sys  

from printing import print_header, print_usage, print_scan_results
from parser import parse_args
from scanner import network_scanner


def main():
    if (len(sys.argv)) < 2:
        print_usage()
        return 1
    
    if sys.argv[1] == "--help":
        print_usage()
        return 0

    try:
        scan_configs = parse_args(sys.argv)
    except Exception:
        print_usage()
        return 1

    results = network_scanner(scan_configs)

    print_header()
    print_scan_results(results)

    return 0

if __name__ == "__main__":
    main()