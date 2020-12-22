import time, datetime, json, aws_resources, sys

#Splunk Enterprise SDK imports
import splunklib.client as client
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators

@Configuration()
class AwsSearch(GeneratingCommand):
    resource = Option(require=True)

    def generate(self):
        
        def datetime_handler(x):
            if isinstance(x, datetime.datetime):
                return x.isoformat()
            raise TypeError("Unknown type")

        if self.resource == "instances":
            resources = aws_resources.get_instances()
        elif self.resource == "interfaces":
            resources = aws_resources.get_network_interfaces()
        elif self.resource == "security_groups":
            resources = aws_resources.get_security_groups()
        elif self.resource == "subnets":
            resources = aws_resources.get_subnets()
        elif self.resource == "volumes":
            resources = aws_resources.get_volumes()
        elif self.resource == "vpcs":
            resources = aws_resources.get_vpcs()
        else:
            resources = ""

        for item in resources:
            if resources == "":
                yield {}
            else:
                yield {
                    '_raw': json.dumps(item, default=datetime_handler),
                    '_time': time.time(),
                    'sourcetype': 'aws:resource',
                    'source': self.resource
                }
# call below works to test code execution in CLI
#AwsSearch.generate(__name__)

# call below works to test command in splunk.
dispatch(AwsSearch, sys.argv, sys.stdin, sys.stdout, __name__)
