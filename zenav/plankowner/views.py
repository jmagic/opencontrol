from plankowner.models import Driver, Device, Talent
from plankowner.serializers import DriverSerializer, DeviceSerializer, TalentSerializer
from rest_framework import generics, permissions
from plankowner.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.views.generic import TemplateView
from django.shortcuts import render
from .models import PanelStyle


def view_panel(request, pk):
    my_panel = PanelStyle.objects.filter(id=pk).first()
    button_names = ['one', 'two', 'three', 'four', 'five', 'six']
    print(my_panel.talents.all())
    context = {'buttons': [], 'button_names': [], 'button_ids': [], 'devices': [], 'drivers': []}
    for i, talent in enumerate(my_panel.talents.all()):
        context['buttons'].append(button_names[i])
        context['button_names'].append(talent.name)
        context['button_ids'].append(talent.pk)
        context['devices'].append(talent.device.pk)
        context['drivers'].append(talent.device.driver.pk)
    print(context)
    return render(request, 'plankowner/panel.html', context)



# class PanelView(TemplateView):
#     template_name = "plankowner/panel.html"

#     def get_context_data(self, *args, **kwargs):
#         context = super(PanelView, self).get_context_data(*args, **kwargs)
#         context['buttons'] = ['one', 'two', 'three', 'four', 'five', 'six']
#         context['button_names'] = ['Lights']
#         return context


@api_view(['POST'])
def watchdog(request, pk):
    my_driver = Driver.objects.filter(id=pk).first()
    my_driver.update_watchdog()
    my_driver.save()
    # my_resp = DriverSerializer(request, my_driver).is_valid()
    return Response({'update': 'success'})


class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TalentList(generics.ListCreateAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TalentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
