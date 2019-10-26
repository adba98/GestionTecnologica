from behave import *
from bj import *

@given('Un Dealer' ) 
def step_impl( context ):
    context.dealer = Dealer()

@given('La mano {total:d}') 
def step_impl(context, total): 
    context.dealer = Dealer() 
    context.total = total 

@given('Una {mano}') 
def step_impl(context, mano): 
    context.dealer = Dealer() 
    context.dealer.mano = mano.split(',')
# -----------------------------------------------
@when('Inicie una ronda')
def step_impl( context ):
    context.dealer.rondaSig() 

@when('El dealer suma las cartas') 
def step_impl(context): 
    context.dealer_total = context.dealer.get_manoTotal()

@when('El dealer determina') 
def step_impl(context): 
    context.dealer_jugada = context.dealer.determinar(context.total)
# -----------------------------------------------
@then('El dealer reparte dos cartas')
def step_impl(context):
    assert( len(context.dealer.mano) == 2 )

@then('El Dealer elige una jugada') 
def step_impl(context): 
    assert (context.dealer.make_play() in ['quedarse', 'pedir']) 
    
# :d trata el valor como entero
@then('El {total:d} es correcto') 
def step_impl(context, total):
    assert (context.dealer_total == total)
  
@then('La opcion {jugada} es correcta') 
def step_impl(context, jugada): 
    assert (context.dealer_jugada == jugada)


