import boto3

def get_vol_arn_from_vol_arn(volume_arn):
    
    #Split the arn using colon (':') separator
    
    arn_part = volume_arn.split(':')
    
    #We want to extract the volume id which is the last part in the resource string
    
    volume_id = arn_part[-1].split('/')[-1]
    
    return volume_id

def lambda_handler(event, context):
    
    volume_arn = event['resources'][0]
    volume_id  = get_vol_arn_from_vol_arn(volume_arn)
    
    ec2_client = boto3.client('ec2')
    
    resource = ec2_client.modify_volume(
        VolumeId   = volume_id,
        VolumeType = 'gp3',
        
    )
    
