from django import http

def home(request):
    return http.HttpResponse("""

    <img src="https://cdn.shopify.com/s/files/1/0249/5224/products/20150407_102829_large.jpg?v=1429097409"
    Hello App Engine and Django World!!!


    """)
