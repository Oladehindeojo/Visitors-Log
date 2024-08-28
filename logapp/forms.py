from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = [
            'name', 'purpose_of_visit', 'host', 'id_verified', 'safety_briefing_acknowledged', 'ppe_issued', 'badge_number',
        ]
