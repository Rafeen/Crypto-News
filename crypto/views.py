from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
import requests
import json


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Grab Crypto News
        news_api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
        context['news'] = json.loads(news_api_request.content)

        # Grab Crypto Price Data
        price_api_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,LINK,ETC,SXP&tsyms=USD')
        context['price'] = json.loads(price_api_request.content)

        return context


class PriceView(View):
    template_name = 'search_prices.html'

    def get(self,request,*args,**kwargs):
        prices_api_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,LINK,ETC,SXP,LINK,VET,&tsyms=USD,EUR,JPY,BDT')

        context = {
            'crypto': json.loads(prices_api_request.content),
        }
        return render(request, "all_prices.html", context)

    def post(self,request,*args,**kwargs):
        if request.POST['quote']:
            quote = (request.POST['quote']).upper()
            quote_api_request = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote}&tsyms=USD,BDT')

            context = {
                'crypto':  json.loads(quote_api_request.content),
                'quotes':  quote,
            }
            return render(request, self.template_name, context)

        else:
            context = {
                "message": "Enter a valid crypto currency short name"
            }
            return render(request, self.template_name, context)



