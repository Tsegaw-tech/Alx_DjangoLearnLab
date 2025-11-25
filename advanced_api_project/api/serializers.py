from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer handles serialization of all Book fields.
# Includes validation to prevent future publication years.
class BookSerializer(serializers.ModelSerializer):

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value

    class Meta:
        model = Book
        fields = '__all__'



class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']