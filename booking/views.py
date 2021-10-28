from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required


from .models import Room, Guest, Stay
from .forms import GuestCreateForm, GuestUpdateForm, StayCreateForm


class GuestDelete(DeleteView):
   model = Guest
   template_name = 'booking/guest_delete_form.html'
   success_url = '/guestlist'

class GuestUpdate(UpdateView):
  model = Guest
  template_name = 'booking/guest_update_form.html'
  form_class = GuestUpdateForm

class GuestCreate(CreateView):
    model = Guest
    template_name = 'booking/guest_create_form.html'
    form_class = GuestCreateForm

class StayCreate(CreateView):
    model = Stay
    template_name = 'booking/templates/registration/stay_create_form.html'
    form_class = StayCreateForm
# Create your views here.
class RoomList(ListView):
    model = Room

    class Meta:
        ordering = ["room_num"]

class GuestList(ListView):
    model = Guest


@login_required
def home(request):
    # templates folder is already assumed b/c this app is reg'd in setting.py
    name = "Homer"
    loggedin=False
    ROOMS=['100','101','102']
    context = {"user_first_name": name, "rooms":ROOMS, "loggedin":loggedin}
    return render(request, 'booking/home.html', context=context )

@login_required
def about(request):
    return render(request, 'booking/about.html')
