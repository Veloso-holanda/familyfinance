from django.db import models


class Revenue(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=20)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.source} - R${self.value}"


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)


    def __str__(self):
        return self.name


class CashOutFlow(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ("débito", "Débito"),
        ("crédito", "Crédito"),
        ("pix", "Pix"),
        ("dinheiro", "Dinheiro"),
    ]

    PAYMENT_TYPE_CHOICES = [
        ("single", "À Vista"),
        ("installment", "Parcelado"),
    ]

    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, verbose_name='Método de pagamento')
    payment_type = models.CharField(
        max_length=15,
        choices=PAYMENT_TYPE_CHOICES,
        default="single",
        verbose_name='Tipo de pagamento',
    )
    installments = models.IntegerField(default=1, verbose_name='Parcelas')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    date = models.DateField(verbose_name='Data')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.payment_method.capitalize()} - R${self.value}"
 