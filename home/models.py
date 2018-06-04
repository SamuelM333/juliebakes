from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from hitcount.models import HitCount, HitCountMixin
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page, HitCountMixin):
    # parent_page_types = [] # TODO Only Root here

    # Hitcount
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    # Header
    header = models.CharField(max_length=255, blank=True)
    subheader = models.CharField(max_length=255, blank=True)
    
    # Section one
    section_one_title = models.CharField(max_length=255, default="")
    section_one_body = RichTextField(blank=True)
    section_one_item_one_title = models.CharField(max_length=255, default="")
    section_one_item_one_body = RichTextField(blank=True)
    section_one_item_two_title = models.CharField(max_length=255, default="")
    section_one_item_two_body = RichTextField(blank=True)
    section_one_item_three_title = models.CharField(max_length=255, default="")
    section_one_item_three_body = RichTextField(blank=True)
    
    # Section two
    section_two_title = models.CharField(max_length=255, default="")
    section_two_body = RichTextField(blank=True)
    
    # Section three
    section_three_title = models.CharField(max_length=255, default="")
    section_three_body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('header', classname="full"),
        FieldPanel('subheader', classname="full"),
        FieldPanel('section_one_title', classname="full"),
        FieldPanel('section_one_body', classname="full"),
        FieldPanel('section_one_item_one_title', classname="full"),
        FieldPanel('section_one_item_one_body', classname="full"),
        FieldPanel('section_one_item_two_title', classname="full"),
        FieldPanel('section_one_item_two_body', classname="full"),
        FieldPanel('section_one_item_three_title', classname="full"),
        FieldPanel('section_one_item_three_body', classname="full"),
        FieldPanel('section_two_title', classname="full"),
        FieldPanel('section_two_body', classname="full"),
        FieldPanel('section_three_title', classname="full"),
        FieldPanel('section_three_body', classname="full"),
    ]

class ProductsPage(Page):
    # subpage_types = ('products.ProductIndex') # TODO

    # Header
    header = models.CharField(max_length=255, blank=True)
    subheader = models.CharField(max_length=255, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('header', classname="full"),
        FieldPanel('subheader', classname="full"),
    ]
