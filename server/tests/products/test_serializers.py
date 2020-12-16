from products.serializers import ProductSerializer


def test_valid_movie_serializer():
    valid_serializer_data = {
        "naziv": "Test Proizvod",
        "kategorija": "test",
        "godina": 1987
    }
    serializer = ProductSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}

def test_invalid_movie_serializer():
    invalid_serializer_data = {
        "naziv": "Test Proizvod",
        "godina": 1987
    }
    serializer = ProductSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"kategorija": ["This field is required."]}