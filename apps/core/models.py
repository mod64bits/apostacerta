from django.db import models
from apps.users.models import User


class Grupo(models.Model):
    nome = models.CharField("Nome do Grupo", max_length=150, unique=True)
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return self.nome


class Concurso(models.Model):
    numero = models.IntegerField("Concurso", unique=True)
    data = models.DateField("Data do sorteio")
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return f"Concurso: {self.numero}"


class JogosGrupo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name="Grupo",
                              help_text="concurso dos Jogos")
    membros = models.ManyToManyField(User, verbose_name='Membros', related_name="membros_grupo", null=True, blank=True)
    concurrso_jogos = models.ForeignKey(Concurso, on_delete=models.CASCADE, verbose_name="Concurso",
                                        help_text="concurso dos Jogos")
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return f"{self.grupo.nome}"


class Jogo(models.Model):
    numeros = models.CharField("Jogos", max_length=100, help_text="Exemplo 1, 2, 3, 4")
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE, verbose_name="Concurso",
                                 help_text="Concurso dos jogos")
    grupo = models.ForeignKey(JogosGrupo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return self.numeros


class Resultado(models.Model):
    resultado = models.CharField("Resultado", max_length=150, help_text="Exemplo 1, 2, 3, 4")
    concurso_resultado = models.ForeignKey(Concurso, on_delete=models.CASCADE, verbose_name="Concurso",
                                           help_text="Concuros dos jogos")
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return self.resultado
