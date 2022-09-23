
class MultiSerializerViewSetMixin:
    """
    source: https://stackoverflow.com/a/58987011

    this class enable us to use multiple serializer in different REST action
    example:
    list: SerializerA
    retrieve: SerializerB

    by providing:
    serializer_action_classes = {
        'list': SerializerA,
        'retrieve': SerializerB,
        ...
    }
    inside the view class
    """

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
