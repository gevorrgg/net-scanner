class ports_range:
    def __init__(self, ranges=None, ports_set=None):
        self.ranges = ranges
        self.ports_set = ports_set

    def __iter__(self):
        if self.ports_set is not None:
            for p in sorted(self.ports_set):
                yield p
            return

        for start, end in self.ranges:   # expects list of (start, end) tuples
            for p in range(start, end + 1):
                yield p

def valid(port):
    return 0 <= port <= 65535

def parse_ports(arg) -> ports_range:
    parts = [p.strip() for p in arg.split(" ")]

    has_range = any("-" in p for p in parts)

    # MODE 1: SET (if no range)
    if not has_range:
        ports = set()
        for p in parts:
            val = int(p)
            if not valid(val):
                raise ValueError("port out of range")
            ports.add(val)
        return ports_range(ports_set=ports)

    # MODE 2: RANGE(S) — each token is "start-end"
    ranges = []
    for token in parts:
        endpoints = token.split("-")
        
        if len(endpoints) != 2:
            raise ValueError(f"invalid range token: {token!r}")
        
        start, end = int(endpoints[0]), int(endpoints[1])
        
        if not valid(start) or not valid(end):
            raise ValueError(f"port out of range: {start}-{end}")
        if start > end:
            raise ValueError(f"range start exceeds end: {start}-{end}")
        
        ranges.append((start, end))   # store as tuple, matching __iter__

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