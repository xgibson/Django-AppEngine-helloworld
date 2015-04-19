from django import http

def home(request):
    return http.HttpResponse(("\n"
                              "\n"
                              "<img src=\"https://cdn.shopify.com/s/files/1/0249/5224/products/20150407_102829_large.jpg?v=1429097409\">\n"
                              "<br />\n"
                              "<h1>Hello App Engine and Django World!!!</h1\n"
                              "\n"
                              "\n"
                              "    "

                              ))
