from django import forms
from atelier.models import ArtworkClass

class SearchClassForm(forms.Form):

    aw_classes = ArtworkClass.objects.all().order_by('class_id_number')

    choices = []
    for aw_class in aw_classes:
        choices.append((aw_class.class_id_number,aw_class.class_id + ':' + aw_class.name))

    class_id_from   = forms.ChoiceField(choices)
    class_id_to     = forms.ChoiceField(choices)
    rank_threshold  = forms.ChoiceField([(1,1),(2,2),(3,3)])
    score_threshold = forms.CharField(initial='0.20')
    omit_zero_count = forms.BooleanField(required=False,initial=True)
