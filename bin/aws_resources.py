import boto3

regions = ('us-east-1', 'us-west-2')

def client_config(region):
    return(boto3.client('ec2', region_name=region))

def get_instances():

    ec2_instances = []

    for region in regions:

        ec2_client = client_config(region)
        ec2_list = ec2_client.describe_instances()['Reservations']
        for ec2_group in ec2_list:
            for instance in ec2_group['Instances']:
                ec2_instances.append(instance)
        
    return (ec2_instances)

def get_network_interfaces():
    network_interfaces = []

    for region in regions:
        ec2_client = client_config(region)
        eni_list = ec2_client.describe_network_interfaces()['NetworkInterfaces']

        for eni in eni_list:
            network_interfaces.append(eni)

    return (network_interfaces)

def get_security_groups():
    security_groups = []

    for region in regions:
        ec2_client = client_config(region)
        sg_list = ec2_client.describe_security_groups()['SecurityGroups']

        for sg in sg_list:
            security_groups.append(sg)

    return (security_groups)

def get_subnets():
    subnets = []

    for region in regions:
        ec2_client = client_config(region)
        subnet_list = ec2_client.describe_subnets()['Subnets']

        for subnet in subnet_list:
            subnets.append(subnet)

    return (subnets)

def get_volumes():
    volumes = []

    for region in regions:
        ec2_client = client_config(region)
        volume_list = ec2_client.describe_volumes()['Volumes']

        for volume in volume_list:
            volumes.append(volume)

    return (volumes)

def get_vpcs():
    vpcs = []

    for region in regions:
        ec2_client = client_config(region)
        vpc_list = ec2_client.describe_vpcs()['Vpcs']

        for vpc in vpc_list:
            vpcs.append(vpc)

    return (vpcs)
