# START_PORT - 1 + GRAND_TOTAL_NODES has to be <= 65535
START_PORT = 50000

START_RACK = 1
END_RACK = 91

START_CHASSIS = 0
END_CHASSIS = 21

START_NODE = 1
END_NODE = 4

TOTAL_RACKS = END_RACK - START_RACK + 1
TOTAL_CHASSIS = END_CHASSIS - START_CHASSIS + 1
TOTAL_NODES = END_NODE - START_NODE + 1

GRAND_TOTAL_NODES = TOTAL_RACKS * TOTAL_CHASSIS * TOTAL_NODES


def get_port(rack, chassis, node):
    return (TOTAL_CHASSIS * TOTAL_NODES) * (rack - 1) + (TOTAL_NODES * chassis) + node + (START_PORT - 1)


last_port = START_PORT - 1 + GRAND_TOTAL_NODES
if last_port > 65535:
    raise OverflowError('Starting port is too large. Won\'t have room for all the nodes!\n'
                        f'Total nodes: {GRAND_TOTAL_NODES}\n'
                        f'Highest possible port starting position: {65535 - GRAND_TOTAL_NODES + 1}')

idempotent_nodes = {}
for rack in range(START_RACK, END_RACK + 1):
    for chassis in range(START_CHASSIS, END_CHASSIS + 1):
        for node in range(START_NODE, END_NODE + 1):
            port = get_port(rack, chassis, node)
            idempotent_nodes[port] = None
            print(f'c1{rack:02}-{chassis:02}{node} -> port: {port}')

if len(idempotent_nodes) == GRAND_TOTAL_NODES:
    print('No port collisions detected!')
else:
    print('ERROR: Ports aren\'t 1 to 1')