# enumerable class
class ports_range:
    def __init__(self, ranges=None, ports_set=None):
        self.ranges = ranges
        self.ports_set = ports_set

    def __iter__(self):
        if self.ports_set is not None:
            for p in sorted(self.ports_set):
                yield p
            return

        for start, end in self.ranges:
            for p in range(start, end + 1):
                yield p

def parse_ports(arg) -> ports_range:
    parts = [p.strip() for p in arg.split(" ")] 

    has_range = any("-" in p for p in parts)

    # MODE 1: SET (если нет диапазонов)
    if not has_range:
        ports = set()

        for p in parts:
            val = int(p)

            if val < 0 or val > 65535:
                raise ValueError("port out of range")

            ports.add(val)

        return ports_range(ports_set=ports)

    # MODE 2: RANGE
    ranges = []


    for p in parts:
        if "-" in p:
            start, end = p.split("-", 1)

            start = int(start.strip())
            end = int(end.strip())

            if start > end:
                raise ValueError("invalid range")

            if start < 0 or end > 65535:
                raise ValueError("port out of range")

            ranges.append((start, end))

        else:
            val = int(p)

            if val < 0 or val > 65535:
                raise ValueError("port out of range")

            ranges.append((val, val))

    return ports_range(ranges=ranges)


primary_ports = {
    20,   # FTP data
    21,   # FTP control
    22,   # SSH
    23,   # Telnet
    25,   # SMTP
    53,   # DNS
    80,   # HTTP
    110,  # POP3
    111,  # RPC
    135,  # MS RPC
    139,  # NetBIOS
    143,  # IMAP
    443,  # HTTPS
    445,  # SMB
    3389, # RDP
    5900, # VNC
    8080  # HTTP proxy / alt
}    