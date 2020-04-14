import argparse
import json

from requests import get


def generate_totals(dict):
    dict['TOTAL_RACKS'] = dict['END_RACK'] - dict['START_RACK'] + 1
    dict['TOTAL_CHASSIS'] = dict['END_CHASSIS'] - dict['START_CHASSIS'] + 1
    dict['TOTAL_NODES'] = dict['END_NODE'] - dict['START_NODE'] + 1
    dict['GRAND_TOTAL_NODES'] = dict['TOTAL_RACKS'] * dict['TOTAL_CHASSIS'] * dict['TOTAL_NODES']


def get_port(dict, start_port, tank, chassis, node):
    port = (dict['TOTAL_CHASSIS'] * dict['TOTAL_NODES']) * (tank - dict['START_RACK'])\
           + (dict['TOTAL_NODES'] * (chassis - dict['START_CHASSIS'])) \
           + node - dict['START_NODE'] + start_port
    if port > 65535:
        raise OverflowError('ERROR: Starting port is too large and resulting port is out of bounds!\n'
                            f'Desired port: {port}\n'
                            'Max port: 65535')
    return port


def get_compute_node_info(hpc, arch, compute_node):
    rack = int(compute_node[2:4])
    if not (HPCs[hpc][arch]['START_RACK'] <= rack <= HPCs[hpc][arch]['END_RACK']):
        raise ValueError(f'ERROR: Rack number {rack} doesn\'t fit within bounds of {compute_arch} on {hpc}.\n'
                         f'Range: ' + str(HPCs[hpc][arch]['START_RACK']) + ' - ' + str(HPCs[hpc][arch]['END_RACK']))
    chassis = int(compute_node[5:7])
    if not (HPCs[hpc][arch]['START_CHASSIS'] <= chassis <= HPCs[hpc][arch]['END_CHASSIS']):
        raise ValueError(f'ERROR: Chassis number {chassis} doesn\'t fit within bounds of {compute_arch} on {hpc}.\n'
                         f'Range: ' + str(HPCs[hpc][arch]['START_CHASSIS']) + ' - ' + str(HPCs[hpc][arch]['END_CHASSIS']))
    node = int(compute_node[7:])
    if not (HPCs[hpc][arch]['START_NODE'] <= node <= HPCs[hpc][arch]['END_NODE']):
        raise ValueError(f'ERROR: Node number {node} doesn\'t fit within bounds of {compute_arch} on {hpc}.\n'
                         f'Range: ' + str(HPCs[hpc][arch]['START_NODE']) + ' - ' + str(HPCs[hpc][arch]['END_NODE']))
    return rack, chassis, node


def available_hpcs():
    hpc_list = []
    hpc_list.append('{:<15s} {:<15s}\n'.format('HPC', 'Compute Architectures'))
    for hpc in HPCs:
        hpc_list.append(f'{hpc:<15s} {str([compute for compute in HPCs[hpc]]):<15s}\n')
    return ''.join(hpc_list)


response = get('https://raw.githubusercontent.com/TACC/tapis-hpc-jupyter/master/hpcs1.json')
HPCs = json.loads(response.content)

parser = argparse.ArgumentParser(prog='python3 get_port.py',
                                 description='Find a unique port on your HPCs login nodes suitable for use within a '
                                             'public facing application',
                                 epilog=
                                 f'''available HPCs and architectures:\n{available_hpcs()}\nexample:\npython3 get_port.py frontera gpu 45000 c196-112''',
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('hpc', metavar='HPC', type=str, help='HPC name (eg: frontera, stampede2, etc)')
parser.add_argument('compute_arch', metavar='COMPUTEARCH', type=str, help='Compute node architecture (eg: x86, gpu)')
parser.add_argument('start_port', metavar='STARTPORT', type=int, help='Port number range starts here')
parser.add_argument('compute_node', metavar='COMPUTENODE', type=str, help='Compute node formatted as c###-###')
args = parser.parse_args()

# c1RR-CCN: 1 (frontera racks all start with 1), R (rack), C (chassis), N (node)
try:
    hpc, compute_arch = args.hpc.lower(), args.compute_arch.lower()
    compute = HPCs[hpc][compute_arch]
    start_port = args.start_port
    compute_node = args.compute_node

    rack, chassis, node = get_compute_node_info(hpc, compute_arch, compute_node)
    generate_totals(compute)
    print(get_port(compute, start_port, rack, chassis, node))
except KeyError:
    if hpc not in HPCs:
        print(f'ERROR: HPC named "{hpc}" not found')
    else:
        print(f'ERROR: Compute architecture named "{compute_arch}" not found in HPC "{hpc}"')
    print('Available HPCs and architectures:')
    print(available_hpcs())
except OverflowError as oe:
    print(oe)
except ValueError as ve:
    print(ve)
except Exception:
    print('ERROR: Cannot parse invalid compute_node value')