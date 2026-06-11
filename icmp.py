import ping3

def is_icmp_reachable(target):
    return ping3.ping(str(target), timeout=1) is not None