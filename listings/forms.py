from django import forms

from property_collections.models import PropertyCollection

from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ["owner", "created_at"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.label_suffix = ""


        for field in self.fields.values():
            widget = field.widget
            base_class = widget.attrs.get("class", "")

            if isinstance(widget, forms.CheckboxInput):
                widget.attrs["class"] = f"{base_class} form-checkbox".strip()
            elif isinstance(widget, forms.Textarea):
                widget.attrs["class"] = f"{base_class} form-textarea".strip()
                widget.attrs.setdefault("rows", 4)
                widget.attrs.setdefault("placeholder", field.label)
            elif isinstance(widget, forms.ClearableFileInput):
                widget.attrs["class"] = f"{base_class} form-file".strip()
            elif isinstance(widget, forms.Select):
                widget.attrs["class"] = f"{base_class} form-select".strip()
                widget.attrs.setdefault("placeholder", field.label)
            else:
                widget.attrs["class"] = f"{base_class} form-input".strip()
                widget.attrs.setdefault("placeholder", field.label)


class CollectionForm(forms.ModelForm):
    class Meta:
        model = PropertyCollection
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input"}),
            "description": forms.Textarea(
                attrs={"class": "form-textarea", "rows": 3}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.label_suffix = ""
