from rest_framework import generics, status
from rest_framework.response import Response

from apps.core.authorisations import CsrfExemptSessionAuthentication
from apps.sender.mixin import BaseSendMixin


class ApiSendView(BaseSendMixin, generics.GenericAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def get_data(self, ser):
        attrs = ser._validated_data
        data = {}
        for rdata in attrs:
            data[rdata] = attrs[rdata]
        return data

    def post(self, request):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            self.send(reffer_user_id=ser.reffer_id, email=ser.email, template=ser.get_lang_template(),
                      data=self.get_data(ser))
            return Response({'ok': True}, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
