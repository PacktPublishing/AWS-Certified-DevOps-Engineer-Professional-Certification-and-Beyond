import boto3
import random 

logging.basicConfig(level=os.environ.get('LOG_LEVEL', 'INFO'))

# Resources 
events = boto3.client('events')
cw = boto3.client('cloudwatch')

#logger = logging.getLogger(__name__)
# The Lambda handler 
def lambda_handler(event, context):
    put_metric = custom_metric()
    put_event = eb()
    return put_metric 

###################################
# Create CW Custom Metric 
###################################

def custom_metric():
    create_metric = cw.put_metric_data(
        Namespace='custom_metric',
        MetricData = [
            {
                'MetricName': 'Signups',
                'Dimensions': [
                    {
                        'Name': 'EMAIL_CAMPAIGN',
                        'Value': 'cableTV_spot2'
                    },
                    {

                    },
                ],
                'Unit': 'None',
                'Value': random.randint(1,100)
            },
        ],
    )
    return create_metric

###################################
# Create EventBridge event
###################################
def eb():
    action_list = ['SUBSCRIBE', 'UNSUBSCRIBE', 'PURCHASE']
    fname_list = ['Joe', 'Jane', 'Jack','Jessica', 'James', 'Josh', 'Jade']
    lname_list = ['Smith', 'Jones', 'Miller', 'Davis', 'Garcia', 'Brown', 'Moore']
    create_event = events.put_events(
        Entries=[
            {
                'Action': random.choice(action_list),
                'Subscriber': random.choice(fname_list) + " " + random.choice(lname_list),
                'Source': 'cableTV_spot2',
                'EventBusName': 'chapter15'
            }
        ]
    )
