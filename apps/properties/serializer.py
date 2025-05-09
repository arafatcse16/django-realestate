from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from .models import Property, PropertyViews

class PropertySerializer( serializers.ModelSerializer):
    user=serializers.SerializerMethodField()
    country=CountryField(name_only=True)
    cover_photo=serializers.SerializerMethodField()
    profile_photo=serializers.SerializerMethodField()
    photo1=serializers.SerializerMethodField()
    photo2=serializers.SerializerMethodField()
    photo3=serializers.SerializerMethodField()
    photo4=serializers.SerializerMethodField()
    
    class Meta:
        model=Property
        fields = [
            "id",
            "user",
            "profile_photo",
            "title",
            "slug",
            "ref_code",
            "description",
            "country",
            "city",
            "postal_code",
            "street_address",
            "property_number",
            "price",
            "tax",
            "final_property_price",
            "plot_area",
            "total_floors",
            "bedrooms",
            "bathrooms",
            "advert_type",
            "property_type",
            "cover_photo",
            "photo1",
            "photo2",
            "photo3",
            "photo4",
            "published_status",
            "views",
        ]
    def get_user(self, obj):
        return obj.user.username

    def get_cover_photo(self, obj):
        return obj.cover_photo.url if obj.cover_photo else None
    
    def get_photo1(self, obj):
        return obj.photo1.url if obj.photo1 else None
    
    def get_photo2(self, obj):
        return obj.photo2.url if obj.photo2 else None
    
    def get_photo3(self, obj):
        return obj.photo3.url if obj.photo3 else None
    
    def get_photo4(self, obj):
        return obj.photo4.url if obj.photo4 else None
    
    def get_profile_photo(self, obj):
        return obj.user.profile.profile_photo.url
    
class PropertyCreateSerializer(serializers.ModelSerializer):
    country=CountryField(name_only=True)
    class Meta:
        model=Property
        fields = ["update_at","pkid"]
        
class PropertyViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PropertyViews
        fields = ["update_at","pkid"]