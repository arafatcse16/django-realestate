import random
import string

from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from apps.common.models import TimeStampUUIDModel

User=get_user_model()

class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super(PropertyPublishedManager, self).get_queryset().filter(is_published=True)
            )

class Property(TimeStampUUIDModel):
    class AdveertType(models.TextChoices):
        FOR_SALE="For Sale", _("For Sale")
        FOR_RENT="For Rent", _("For Rent")
        AUCTION="Auction", _("Auction")
    
    class PropertyType(models.TextChoices):
        APARTMENT="Apartment", _("Apartment")
        HOUSE="House", _("House")
        VILLA="Villa", _("Villa")
        COMMERCIAL="Commercial", _("Commercial")
        OFFICE="Office", _("Office")
        WAREHOUSE="Warehouse", _("Warehouse")
        OTHER = "Other", _("Other")

    user = models.ForeignKey(User, verbose_name=_("Agent, Seller, Buyer"),
                             on_delete=models.DO_NOTHING, related_name="agent_buyer",)
    title=models.CharField(max_length=250, verbose_name=_("Property Title"))
    slug=AutoSlugField(populate_from="title", unique=True, always_update=True)
    ref_code=models.CharField(
        verbose_name=_("Property Reference Code"),
        max_length=255, unique=True, blank=True
    )
    description=models.TextField(verbose_name=_("Description"), default="Default Description....update me plase...")
    country=CountryField(verbose_name=_("Country"),default="BD",blank_label="(Select Country)")
    city=models.CharField(verbose_name=_("City"), max_length=100,default="Dhaka")
    postal_code=models.CharField(verbose_name=_("Postal Code"), max_length=180, default="1212")
    street_address=models.CharField(verbose_name=_("Street Address"), max_length=255, default="Dhaka")
    property_number=models.CharField(
        verbose_name=_("Property Number"), 
        validators=[MinValueValidator(1)],
        default="Dhaka"
    )
    price=models.DecimalField(verbose_name=_("Price"), max_digits=8, decimal_places=2, default=0.00)
    tax=models.DecimalField(
        verbose_name=_("Property Tax"),
        max_digits=6,
        decimal_places=2,
        default=0.15,
        help_text="15% tax on property price"
    )
    plot_area=models.DecimalField(
        verbose_name=_("Plot Area(m^2)"),
        max_digits=8,
        decimal_places=2,
        default=0.00,
        help_text="in square feet"
    )
    total_floors=models.IntegerField(
        verbose_name=_("Number of Floors"),default=0)
    bedrooms=models.IntegerField(verbose_name=_("Bedrooms"), default=1)
    bathrooms=models.DecimalField(
        verbose_name=_("Bathrooms"),
        max_digits=4,
        decimal_places=2,
        default=1.00
    )
    advert_type=models.CharField(
        verbose_name=_("Advert Type"),
        max_length=50,
        choices=AdveertType.choices,
        default=AdveertType.FOR_SALE
    )
    property_type=models.CharField(
        verbose_name=_("Property Type"),
        max_length=50,
        choices=PropertyType.choices,
        default=PropertyType.OTHER
    )
    cover_photo=models.ImageField(
        verbose_name=_("Main Photo"),
        default="/house_sample.jpg",
        blank=True,
        null=True
    )
    photo1=models.ImageField(
        default="/interior_sample.jpg",
        null=True,blank=True,)
    photo2=models.ImageField(
        default="/interior_sample.jpg",
        null=True,blank=True,)
    photo3=models.ImageField(
        default="/interior_sample.jpg",
        null=True,blank=True,)
    photo4=models.ImageField(
        default="/interior_sample.jpg",
        null=True,blank=True,)
    published_status=models.BooleanField(
        verbose_name=_("Published Status"),
        default=False,
    )
    views=models.IntegerField(verbose_name=_("Total Views"), default=0)
    objects=models.Manager()
    published=PropertyPublishedManager()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name=_("Property")
        verbose_name_plural=_("Properties")
    def save(self, *args, **kwargs):
        self.title=str.title(self.title)
        self.description=str.capitalize(self.description)
        self.ref_code="".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=10
            )
        )
        super(Property, self).save(*args, **kwargs)
    
    @property
    def final_property_price(self):
        tax_percentage=self.tax
        property_price=self.price
        tax_amount=round((property_price * tax_percentage), 2)
        price_after_tax=float(round((property_price + tax_amount), 2))
        return price_after_tax
    
class PropertyViews(TimeStampUUIDModel):
    ip=models.CharField(verbose_name=_("IP Address"), max_length=255)
    property=models.ForeignKey(
        Property,
        verbose_name=_("Property"),
        on_delete=models.CASCADE,
        related_name="property_views"
    )
    
    def __str__(self):
        return (
            f"Total Views on - {self.property.title} is - {self.property.views} view(s)"
        )
    class Meta:
        verbose_name="Total Views on Property"
        verbose_name_plural="Total Property Views"
        
     