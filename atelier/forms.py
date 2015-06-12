from django import forms
from atelier.models import ArtworkClass

class SearchClassForm(forms.Form):

    aw_classes = ArtworkClass.objects.all().order_by('class_id_number')

    choices = []
    for aw_class in aw_classes:
        choices.append((aw_class.class_id_number,aw_class.class_id))

    class_id_number_from = forms.ChoiceField(choices)
    class_id_number_to   = forms.ChoiceField(choices)
#    only_rank_top = forms.BooleanField(required=False)
