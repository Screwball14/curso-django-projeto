import math


def make_pagination_range(qty_pages_shown, current_page, pg_range=[]): 
    #pagination_range = o quanto de paginas mostrara ao
    #usuario, qty_pages = a quantidade de paginas, current_pag = a pagina em que o usuario está
    
    #current_page é 1
    middle = math.ceil(qty_pages_shown/2) # se é 4 então middle é *2*
    start = current_page - middle # *-1*
    stop = current_page + middle # *3*

    start_offset = abs(start) if start < 0 else 0

    total_pages = len(pg_range)

    if start < 0:
        start = 0
        stop += start_offset

    
    if stop > total_pages:
        start -= abs(total_pages - stop) # serve para diminuir o start para o stop ser menor com a diferenca entre stop e total_pages


    if current_page > total_pages:
        raise ValueError()
        
        
    

    return pg_range[start:stop] 