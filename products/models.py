from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel


class ProductIndex(Page):
    """
    Index page for all products
    """
    subpage_types = ('products.Product', 'products.ProductIndex')


class Product(Page):
    parent_page_types = ['products.ProductIndex']
    description = RichTextField()
    featured_product = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('featured_product'),
        InlinePanel('images', label='Product images')
    ]

    @property
    def first_image(self):
        return self.images.first()

    @property
    def image_list(self):
        return self.images.get_queryset()


# class ProductVariant(ProductVariantBase):
#     """Represents a 'variant' of a product
#     """
#     # You *could* do away with the 'Product' concept entirely - e.g. if you only
#     # want to support 1 'variant' per 'product'.
#     product = ParentalKey(Product, related_name='variants')
#
#     slug = AutoSlugField(separator='', populate_from=('product', 'ref'))
#
#     # Enter your custom product variant fields here
#     # e.g. colour, size, stock and so on.
#     # Remember, ProductVariantBase provides 'price', 'ref' and 'stock' fields
#     description = RichTextField(blank=True)


class ProductImage(Orderable):
    """Example of adding images related to a product model
    """
    product = ParentalKey(Product, related_name='images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=255)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption')
    ]
