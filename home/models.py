from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
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
    section_two_item_one_title = models.CharField(max_length=255, default="")
    section_two_item_one_body = RichTextField(blank=True)
    section_two_item_two_title = models.CharField(max_length=255, default="")
    section_two_item_two_body = RichTextField(blank=True)
    section_two_item_three_title = models.CharField(max_length=255, default="")
    section_two_item_three_body = RichTextField(blank=True)
    section_two_item_four_title = models.CharField(max_length=255, default="")
    section_two_item_four_body = RichTextField(blank=True)
    section_two_item_five_title = models.CharField(max_length=255, default="")
    section_two_item_five_body = RichTextField(blank=True)
    section_two_item_six_title = models.CharField(max_length=255, default="")
    section_two_item_six_body = RichTextField(blank=True)
    
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
        FieldPanel('section_two_item_one_title', classname="full"),
        FieldPanel('section_two_item_one_body', classname="full"),
        FieldPanel('section_two_item_two_title', classname="full"),
        FieldPanel('section_two_item_two_body', classname="full"),
        FieldPanel('section_two_item_three_title', classname="full"),
        FieldPanel('section_two_item_three_body', classname="full"),
        FieldPanel('section_two_item_four_title', classname="full"),
        FieldPanel('section_two_item_four_body', classname="full"),
        FieldPanel('section_two_item_five_title', classname="full"),
        FieldPanel('section_two_item_five_body', classname="full"),
        FieldPanel('section_two_item_six_title', classname="full"),
        FieldPanel('section_two_item_six_body', classname="full"),
        FieldPanel('section_three_title', classname="full"),
        FieldPanel('section_three_body', classname="full"),
    ]
