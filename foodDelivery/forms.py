from django import forms
# width: 100%
# height: 40px
# padding: 5px 10px
# border: 2px solid
# border-radius: 5px
# outline: none


class CheckoutForm(forms.Form):
    name = forms.CharField(label="الاسم بالكامل *",
                           required=True, widget=forms.TextInput)
    address = forms.CharField(
        label="العنوان *", required=True, widget=forms.TextInput)
    city = forms.CharField(
        label="المحافظة*", required=True, widget=forms.TextInput)
    phone = forms.CharField(
        label="الموبيل*", required=True, widget=forms.NumberInput)
    email = forms.EmailField(
        label="الايميل*", required=True, widget=forms.EmailInput)
    notes = forms.CharField(
        label="ملاحظات *", widget=forms.Textarea, required=False)
