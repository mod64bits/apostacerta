from django.contrib import admin
from .models import Concurso, JogosGrupo, Jogo, Resultado, Grupo
from .forms import JogosForm


class JogoInine(admin.TabularInline):
    model = Jogo
    extra = 0


# class JogoInine(admin.TabularInline):
#     model = Jogo

@admin.register(Grupo)
class ConcursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'created_at']
    list_display_links = 'nome', 'created_at',
    search_fields = 'nome', 'created_at',
    list_per_page = 10
    ordering = '-created_at',


@admin.register(Concurso)
class ConcursoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'data']
    list_display_links = 'numero', 'data',
    search_fields = 'numero', 'created_at',
    list_per_page = 10
    ordering = '-created_at',


@admin.register(JogosGrupo)
class JogosGrupoAdmin(admin.ModelAdmin):
    list_display = ['grupo', 'concurrso_jogos']
    list_display_links = 'grupo',
    search_fields = 'grupo', 'created_at',
    list_per_page = 10
    ordering = '-created_at',

    inlines = [
        JogoInine,
    ]
    filter_horizontal = (
        "membros",

    )



@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ['numeros', 'concurso', 'created_at']
    list_display_links = 'numeros', 'created_at',
    search_fields = 'numeros',
    list_per_page = 15
    ordering = '-created_at',




