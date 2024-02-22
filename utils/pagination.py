import math

def make_pagination_range(qty_pages_shown, current_page, pg_range=[]): 
    #pagination_range = o quanto de paginas mostrara ao
    #usuario, qty_pages = a quantidade de paginas, current_pag = a pagina em que o usuario está
    # if current_page >= 3:
    #     return [3,4,5,6]
    middle = math.ceil(qty_pages_shown/2)

    start = current_page - middle
    stop = current_page + middle

    return pg_range[start:stop]