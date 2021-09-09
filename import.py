import boto3

client = boto3.client('cloudformation')

accounts = [1,2,3]


# expect standard cloudformation template name, so the only thing
stacks = {
        'stackset_name': 'stack_name'
        }

for account in accounts:
    for stack_arn, stackset_name in stacks:
        get_stack_arn(account, stack)
        import_stack(stack_arn, stackset_name)


def import_stack(stack_arn, stackset_name):

    response = client.import_stacks_to_stack_set(
        StackSetName=stackset_name,
        StackIds=[ stack_arn,
        ],
        OperationPreferences={
            'RegionConcurrencyType': 'PARALLEL',
            'FailureTolerancePercentage': 10,
            'MaxConcurrentPercentage': 100
        },
        OperationId='ImportStackToStackSet',
        CallAs='SELF'
    )

def get_stack_arn(account_id, stackname):
    assume_role_into_account(account_id)
    response = client.describe_stacks(
        StackName=stackname,
)

def assume_role_into_account(account_id):

    response = client.describe_stack(params)


print(response)
