import os
import athena
import ddb


# for lambda
# region = os.environ['AWS_REGION']

# for code level
region = 'us-west-2'



database = 'pinpoint_campaign'
s3_output = 's3://di-jjinso/1206/'


def logic():
    query = 'SELECT * FROM "pinpoint_campaign"."pinpoint_1127" where event_type = \'_campaign.opened_notification\' and attributes.campaign_id in (\'13b810509ee04a4ea28c5217d95b60c5\', \'be65c6eda66d4a538e7242eb68aa0a4e\')'
    
    #a = athena.Athena(database)
    #a.run_query(query, s3_output)
    
    d = ddb.Ddb('OrderTable')
    item = {
        'Name':'Minjae',
        'Timestamp':1234
    }
    print(d.put_item(item))

    pass



if __name__ == "__main__":
    logic()
    pass