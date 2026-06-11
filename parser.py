import ipaddress
from ip_range import parse_targets
from ports import ports_range, parse_ports, primary_ports 

def set_ports(configs, arg):
    ports_range = parse_ports(arg)

    configs["ports"] = ports_range


def set_mode(configs, arg):
    available_mods = {"deep", "fast"}

    if arg not in available_mods:
        raise Exception

    configs["mode"] = arg

    if arg == "deep":
        configs["ports"] = parse_ports("0-65535")

flag_setters = {"--ports" : set_ports, 
                  "--mode"  : set_mode}

def is_flag(arg):
    return arg.startswith("--")

def is_available_flag(arg):
    return arg in flag_setters

def parse_args(args):
    scan_configs = { "targets" : list(parse_targets("127.0.0.1")),
                     "ports"   : ports_range(ports_set=primary_ports),
                     "mode"    : "fast"   
                    }

    i = 1

    target_ranges = []

    while i < len(args):
        arg = args[i]
        
        if is_flag(args[i]):
            if not is_available_flag(arg):
                print(f"network scanner: unknown flag '{arg}'")
                i += 1
                continue

            flag_setter = flag_setters[arg]

            if i == len(args) - 1:
                print("network scanner: unexpected value")
                return scan_configs

            i += 1

            values = []

            while i < len(args) and not is_flag(args[i]):
                values.append(args[i])
                i += 1

            next_args = " ".join(values)

            try:
                flag_setter(scan_configs, next_args)
            except Exception:
                print(f"network scanner: unexpected value '{next_args}'")
                raise ValueError
        else: # targets
            
            try:
                target_ranges.append(parse_targets(args[i]))
            except Exception:
                print(f"network scanner: unexpected value '{args[i]}'")
                raise ValueError

            i += 1

    if len(target_ranges) > 0 :
        scan_configs["targets"] = target_ranges

    return scan_configs