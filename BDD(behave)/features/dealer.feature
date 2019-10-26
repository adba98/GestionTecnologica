# Dado » inicializa estado
# Cuando » Describe una accion
# Entonces » Resultado esperado

Feature: Dealer para el juego 21
    Scenario: Repartir cartas iniciales
        Given Un Dealer
        When Inicie una ronda
        Then El dealer reparte dos cartas
    
    Scenario Outline: Obtener total de la mano
        Given Una <mano> 
        When El dealer suma las cartas
        Then El <total> es correcto

        Examples: Manos 
        | mano  | total | 
        | 5,7   | 12    | 
        | 5,Q   | 15    | 
        | Q,Q,A | 21    |
        | Q,A   | 21    |
        | A,A,A | 13    |

    Scenario Outline: Reglas del Dealer 
        Given La mano <total> 
        When El dealer determina
        Then La opcion <jugada> es correcta 
        
        Examples: Hands 
        | total | jugada| 
        | 10    | pedir   | 
        | 15    | pedir   | 
        | 16    | pedir   | 
        | 17    | quedarse | 
        | 18    | quedarse | 
        | 19    | quedarse | 
        | 20    | quedarse | 
        | 21    | quedarse | 
        | 22    | quedarse |
    
    Scenario: El Dealer puede juagar 
        Given Un Dealer
        When Inicie una ronda
        Then El Dealer elige una jugada
    