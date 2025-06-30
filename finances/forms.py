from django import forms
from .models import CashOutFlow, Revenue

class CashOutFlowForm(forms.ModelForm):
    class Meta:
        model = CashOutFlow
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get("payment_method")
        payment_type = cleaned_data.get("payment_type")
        installments = cleaned_data.get("installments")

        # Regra 1: se não for crédito, não pode ser parcelado
        if payment_type == 'installment' and payment_method != 'Crédito':
            raise forms.ValidationError("Somente pagamentos no crédito podem ser parcelados.")

        # Regra 2: pagamentos a vista a parcela tem que ser 1.
        if payment_type == 'single':
            if installments == 1:
                pass
            else:
                raise forms.ValidationError("Para pagamentos à vista o número de parcelas tem que ser igual a 1.")
            

        return cleaned_data

class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get("source")
        value = cleaned_data.get("value")



        return cleaned_data