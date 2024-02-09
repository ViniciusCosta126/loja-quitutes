from sitedoces.models import models, Categoria


class Doce(models.Model):

    CHOICES = (
        (1, 'Kg'),
        (2, 'g')
    )

    nome = models.CharField(max_length=200, null=False)
    ativo = models.BooleanField(default=True)
    peso = models.IntegerField(null=False)
    unidade = models.IntegerField(choices=CHOICES)
    categoria = models.ForeignKey(
        'Categoria', on_delete=models.CASCADE, related_name='categoria')
    quantidade = models.IntegerField(default=1)
    valor = models.DecimalField(max_digits=1000, decimal_places=2)
    descricao = models.TextField()
    imagem = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome
