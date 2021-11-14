import urllib.request,json
from .models import Quote


def get_quote():
    '''
    Function that gets the random quotes
    '''
    get_article_details_url = 'http://quotes.stormconsultancy.co.uk/random.json'.format()
    with urllib.request.urlopen(get_article_details_url) as url:
        quote_data = url.read()
        quote_data_response = json.loads(quote_data)
        
        quote_results = None
        
        if quote_data_response["quotes"]:
            quote_results_list = quote_data_response["quotes"]
            quote_results = process_results(quote_results_list)
    return quote_results




def process_results(quote_list):
    
    quote_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        author = quote_item.get('author')
        quote = quote_item.get('quote')
   
        quote_object=quote.Quote(id,author,quote)
        quote_results.append(quote_object)
        
    return quote_results    

