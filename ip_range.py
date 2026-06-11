import ipaddress


# enumerable class ip for easy iteration through ip range
class ip_range:
    def __init__(self, start_ip, end_ip):
        self.start = int(start_ip)
        self.end = int(end_ip)

    def __iter__(self):
        for ip_int in range(self.start, self.end + 1):
            yield ipaddress.IPv4Address(ip_int)

    def __repr__(self):
        return f"ip_range({ipaddress.IPv4Address(self.start)}-{ipaddress.IPv4Address(self.end)})"


def parse_targets(arg) -> ip_range:

    # 1. CIDR
    if "/" in arg:
        net = ipaddress.ip_network(arg, strict=False)
        hosts = list(net.hosts())

        if not hosts:
            raise ValueError("empty network")

        return ip_range(hosts[0], hosts[-1])

    # 2. range A-B
    if "-" in arg:
        start, end = arg.split("-", 1)

        start_ip = ipaddress.IPv4Address(start.strip())
        end_ip = ipaddress.IPv4Address(end.strip())

        if int(start_ip) > int(end_ip):
            raise ValueError("invalid range")

        return ip_range(start_ip, end_ip)

    # 3. single IP
    ip = ipaddress.IPv4Address(arg)
    return ip_range(ip, ip)

