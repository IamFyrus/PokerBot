'''
Simple example pokerbot, written in Python.
'''
import random

from skeleton.actions import FoldAction, CallAction, CheckAction, RaiseAction
from skeleton.states import GameState, TerminalState, RoundState
from skeleton.states import NUM_ROUNDS, STARTING_STACK, BIG_BLIND, SMALL_BLIND
from skeleton.bot import Bot
from skeleton.runner import parse_args, run_bot

import eval7

class Player(Bot):
    '''
    A pokerbot.
    '''

    def __init__(self):
        '''
        Called when a new game starts. Called exactly once.

        Arguments:
        Nothing.

        Returns:
        Nothing.
        '''
        pass

    def handle_new_round(self, game_state, round_state, active):
        '''
        Called when a new round starts. Called NUM_ROUNDS times.

        Arguments:
        game_state: the GameState object.
        round_state: the RoundState object.
        active: your player's index.

        Returns:
        Nothing.
        '''
        #my_bankroll = game_state.bankroll  # the total number of chips you've gained or lost from the beginning of the game to the start of this round
        #game_clock = game_state.game_clock  # the total number of seconds your bot has left to play this game
        #round_num = game_state.round_num  # the round number from 1 to NUM_ROUNDS
        #my_cards = round_state.hands[active]  # your cards
        #big_blind = bool(active)  # True if you are the big blind
        pass

    def handle_round_over(self, game_state, terminal_state, active):
        '''
        Called when a round ends. Called NUM_ROUNDS times.

        Arguments:
        game_state: the GameState object.
        terminal_state: the TerminalState object.
        active: your player's index.

        Returns:
        Nothing.
        '''
        #my_delta = terminal_state.deltas[active]  # your bankroll change from this round
        #previous_state = terminal_state.previous_state  # RoundState before payoffs
        #street = previous_state.street  # 0, 3, 4, or 5 representing when this round ended
        #my_cards = previous_state.hands[active]  # your cards
        #opp_cards = previous_state.hands[1-active]  # opponent's cards or [] if not revealed
        pass

    def get_action(self, game_state, round_state, active):
        '''
        Where the magic happens - your code should implement this function.
        Called any time the engine needs an action from your bot.

        Arguments:
        game_state: the GameState object.
        round_state: the RoundState object.
        active: your player's index.

        Returns:
        Your action.
        
        suited = False
        pocket_pair = False
        good_pocket_pair = False
        fuckisthis = False
        flush = False
        my_cards_greater = True
        '''
        my_bankroll = game_state.bankroll
        legal_actions = round_state.legal_actions()

        my_cards = round_state.hands[active]
        my_cards = list(map(eval7.Card, my_cards))

        
        if round_state.street == 0:
            if my_cards[0].rank == my_cards[1].rank:
           #     pocket_pair = True
                if my_cards[0].rank > 9:
                   # good_pocket_pair = True
                    if(max_raise != min_raise):
                        return RaiseAction(3)
                    elif CallAction in legal_actions:
                        return CallAction()
                    else:
                        return CheckAction()
            elif my_cards[0].suit == my_cards[1].suit:
          #      suited = True
                if (my_cards[0].rank > 10) & (my_cards[1].rank > 10):
                    return RaiseAction(3)
                elif CheckAction in legal_actions:
                    return CheckAction()
                elif :
                    return CallAction()
            elif my_cards[0].rank < 10 & my_cards[1].rank < 10:
         #       fuckisthis = True
                if CheckAction in legal_actions:
                    return CheckAction()
                else:
                    return FoldAction()

        '''
        if round_state.street == 3:    
            if fuckisthis:
                if CheckAction in legal_actions:
                    return CheckAction()
                else:
                    return FoldAction()

            if suited:
                if round_state.street[0].suit == my_cards[0].suit:
                    if round_state.street[0].suit == round_state.street[1].suit:
                        flushdraw = True
                        if round_state.street[0].suit == round_state.street[2].suit:
                            flush = True
                            return RaiseAction(max_raise)
                        else:
                            return RaiseAction(max_raise/8)
                    elif CheckAction in legal_actions:
                        return CheckAction
                    elif bet_amt < (max_raise/16):
                        return CallAction()
            if pocket_pair:
                for i in round_state.street:
                    if round_state.street[i].rank == my_cards[0].rank:
                        return RaiseAction(max_raise/4)
                    if round_state.street[i].rank > my_cards[0].rank:
                        my_cards_greater = False
                if my_cards_greater:
                    return RaiseAction(max_raise/8)
                elif good_pocket_pair:
                    if CallAction in legal_actions:
                        return CallAction()
                    else:
                        return CheckAction()
'''
                
                    
            




            
            
        

        action = random.choice(tuple(legal_actions))
        if action is RaiseAction:
            min_raise, max_raise = round_state.raise_bounds()
            bet_amt = random.randint(min_raise, max_raise)
            return RaiseAction(bet_amt)
        return action()


if __name__ == '__main__':
    run_bot(Player(), parse_args())
