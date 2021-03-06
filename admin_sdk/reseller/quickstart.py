# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START admin_sdk_reseller_quickstart]
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/apps.order'

def main():
    """Calls the Admin SDK Reseller API. Prints the customer ID, SKU ID,
    and plan name of the first 10 subscriptions managed by the domain.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('reseller', 'v1', http=creds.authorize(Http()))

    # Call the Admin SDK Reseller API
    print('Getting the first 10 subscriptions')
    results = service.subscriptions().list(maxResults=10).execute()
    subscriptions = results.get('subscriptions', [])
    if not subscriptions:
        print('No subscriptions found.')
    else:
        print('Subscriptions:')
        for subscription in subscriptions:
            print(u'{0} ({1}, {2})'.format(subscription['customerId'],
                subscription['skuId'], subscription['plan']['planName']))

if __name__ == '__main__':
    main()
# [END admin_sdk_reseller_quickstart]
