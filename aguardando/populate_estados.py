from .models import Estado

def populate():
    estados_count = Estado.objects.count()
    if estados_count == 0:
        estados = ['Desistência', 'Reserva', 'Container', 'Desistência do Container', 'Faturado', 'Cancelado', 'Controle', 'Verificação']
        
        for i, e in enumerate(estados, 1):
            Estado.objects.create(ordem=i, nome=e)
            print("Created", nome)
