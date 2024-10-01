import json

def leggi_file(nome_file):
    variabili = {}
    with open(nome_file, 'r') as file:
        for linea in file:
            linea = linea.strip()
            if linea and not linea.startswith('#'):
               chiave, valore = linea.split('=')
               if chiave.startswith('*'):
                   chiave = chiave[1:]  # Rimuovi il carattere '*'
                   variabili[chiave] = valore
                   print("ARRAY", variabili[chiave])
               elif not chiave.startswith('*'):
                   variabili[chiave] = valore.split(',')
                   print("LISTA", variabili[chiave])
    return variabili

def crea_json(variabili):
    node_settings = {
                "display_name": variabili.get('display_name', ''),
                "host_switch_spec": {
                    "host_switches": [
                        {
                            "host_switch_name": "nsxHostSwitch",
                            "host_switch_type": "NVDS",
                            "host_switch_mode": "STANDARD",
                            "host_switch_profile_ids": [
                                {
                                    "key": "UplinkHostSwitchProfile",
                                    "value": variabili.get('value', '')
                                }
                            ],
                            "pnics": [
                                {
                                    "device_name": "fp-eth0",
                                    "uplink_name": "uplink-1"
                                }
                            ],
                            "is_migrate_pnics": False,
                            "ip_assignment_spec": {
                                "ip_pool_id": variabili.get('ip_pool_id', ''),
                                "resource_type": "StaticIpPoolSpec"
                            },
                            "cpu_config": [],
                            "transport_zone_endpoints": [
                                {
                                    "transport_zone_id": variabili.get('transport_zone_id', ''),
                                    "transport_zone_profile_ids": [
                                        {
                                            "resource_type": "BfdHealthMonitoringProfile",
                                            "profile_id": "52035bb3-ab02-4a08-9884-18631312e50a"
                                        }
                                    ]
                                }
                            ],
                            "not_ready": False
                        }
                    ],
                    "resource_type": "StandardHostSwitchSpec"
                },
                "maintenance_mode": "DISABLED",
                "node_deployment_info": {
                    "deployment_type": "VIRTUAL_MACHINE",
                    "deployment_config": {
                        "vm_deployment_config": {
                            "vc_id": variabili.get('vc_id', ''),
                            "compute_id": variabili.get('compute_id', ''),
                            "storage_id": variabili.get('storage_id', ''),
                            "management_network_id": variabili.get('management_network_id', ''),
                            "management_port_subnets": [
                                {
                                    "ip_addresses": [
                                        variabili.get('ip_addresses', '')
                                    ],
                                    "prefix_length": variabili.get('prefix_length', '')
                                }
                            ],
                            "default_gateway_addresses": [
                                "10.111.0.1"
                            ],
                            "data_network_ids": [
                                "dvportgroup-6938"
                            ],
                            "reservation_info": {
                                "memory_reservation": {
                                    "reservation_percentage": 100
                                },
                                "cpu_reservation": {
                                    "reservation_in_shares": "HIGH_PRIORITY",
                                    "reservation_in_mhz": 0
                                                            }
                                },
                                                    "resource_allocation" : {
                                    "cpu_count" : 4,
                                    "memory_allocation_in_mb" : 8192
                                },
                            "placement_type": "VsphereDeploymentConfig"
                        },
                        "form_factor": variabili.get('form_factor', ''),
                        "node_user_settings": {
                            "cli_username": variabili.get('cli_username', ''),
                                            "root_password":variabili.get('root_password', ''),
                                            "cli_password":variabili.get('cli_password', '')
                        }
                    },
                    "node_settings" : {
                    "hostname" : variabili.get('hostname', ''),
                    "search_domains" : variabili.get('search_domains', ''),
                    "ntp_servers" : variabili.get('ntp_servers', ''),
                    "dns_servers" : variabili.get('dns_servers', ''),
                    "enable_ssh" : True,
                    "allow_ssh_root_login" : True,
                    "enable_upt_mode" : False
                    },
                    "resource_type": "EdgeNode",
                    "ip_addresses":
                        variabili.get('ip_addresses', '')
                    
                }
    }

    json_string = json.dumps(node_settings, indent=4, separators=(',', ': '))
    return json_string

variabili = leggi_file('variables.txt')
json_string = crea_json(variabili)

with open('out.json', 'w') as file:
    file.write(json_string)
