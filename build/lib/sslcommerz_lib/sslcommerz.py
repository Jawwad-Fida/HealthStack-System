#import requests
from pip._vendor import requests


class SSLCOMMERZ(object):
    store_id = None
    store_pass = None
    issandbox = None
    mode = None
    createSessionUrl = None
    validation_url = None
    transaction_url = None

    def __init__(self, config):
        self.store_id = config['store_id']
        self.store_pass = config['store_pass']
        self.mode = 'sandbox' if (config['issandbox']) else 'securepay'
        self.createSessionUrl = "https://" + self.mode + \
            ".sslcommerz.com/gwprocess/v4/api.php"
        self.validation_url = "https://" + self.mode + \
            ".sslcommerz.com/validator/api/validationserverAPI.php"
        self.transaction_url = "https://" + self.mode + \
            ".sslcommerz.com/validator/api/merchantTransIDvalidationAPI.php"

    def createSession(self, post_body):
        post_body['store_id'] = self.store_id
        post_body['store_passwd'] = self.store_pass
        return self.call_api('POST', self.createSessionUrl, post_body)

    def validationTransactionOrder(self, validation_id):
        params = {}
        params['val_id'] = validation_id
        params['store_id'] = self.store_id
        params['store_passwd'] = self.store_pass
        params['format'] = 'json'
        return self.call_api('GET', self.validation_url, params)

    def init_refund(self, bank_tran_id, refund_amount, refund_remarks):
        params = {}
        params['bank_tran_id'] = bank_tran_id
        params['refund_amount'] = refund_amount
        params['refund_remarks'] = refund_remarks
        params['store_id'] = self.store_id
        params['store_passwd'] = self.store_pass
        params['format'] = 'json'
        return self.call_api('GET', self.transaction_url, params)

    def query_refund_status(self, refund_ref_id):
        params = {}
        params['refund_ref_id'] = refund_ref_id
        params['store_id'] = self.store_id
        params['store_passwd'] = self.store_pass
        params['format'] = 'json'
        return self.call_api('GET', self.transaction_url, params)

    def transaction_query_session(self, sessionkey):
        params = {}
        params['sessionkey'] = sessionkey
        params['store_id'] = self.store_id
        params['store_passwd'] = self.store_pass
        params['format'] = 'json'
        return self.call_api('GET', self.transaction_url, params)

    def transaction_query_tranid(self, tran_id):
        params = {}
        params['tran_id'] = tran_id
        params['store_id'] = self.store_id
        params['store_passwd'] = self.store_pass
        params['format'] = 'json'
        return self.call_api('GET', self.transaction_url, params)

    def call_api(self, method, url, payload):

        try:
            if method == 'POST':
                response = requests.post(url, data=payload)

            elif method == 'delete':
                response = requests.delete(url)

            elif method == 'put':
                response = requests.put(url, data=payload)

            elif method == 'GET':
                response = requests.get(url, params=payload)

            else:
                response = {'response': 'Method is not valid'}
            return response.json()
        except:
            print("An exception occurred")
