from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from product.models import fashion_collection
from django.urls import reverse

class latest_feed(Feed):
    title="Trialshop"
    link="/drcomments/"
    description="its an amazing fashion site for latest products"

    def items(self):
        return fashion_collection.objects.all()[:4]

    def item_title(self, item):
        return item.name

    def item_desc(self,item):
        return truncatewords( item.desc,20)

    def item_link(self,item):
        return reverse('home')