import pandas as pd
import numpy as np
import ipywidgets as widgets
from ipywidgets import *
from IPython.display import *
import random

def run_prisoners_dilemma(player1, player2, output_df, summary_df):
    if player2 == "Copy":
        player_2_stat = player1
    if player2 == "Random":
        player_2_stat = random.choice(["Cooperate","Defect"])
    player_1_strat=player1
    player_2_strat=player2
    

    if (player_1_strat == "Cooperate") and (player_2_strat == "Cooperate"):
        output_df.loc[len(output_df.index)]=[3,3]
    elif (player_1_strat =="Cooperate") and (player_2_strat =="Defect"):
        output_df.loc[len(output_df.index)]=[1,4]
    elif (player_2_strat =="Cooperate") and (player_1_strat =="Defect"):
        output_df.loc[len(output_df.index)]=[4,1]
    else:
        output_df.loc[len(output_df.index)]=[2,2]
    summary_df.loc["Sum"]=[sum(output_df["Player 1 Payoff"]),sum(output_df["Player 2 Payoff"])]
    summary_df.loc["Mean"]=[np.mean(output_df["Player 1 Payoff"]),np.mean(output_df["Player 2 Payoff"])]
    
def play_pd(p1,p2, play_flag):
    if play_flag:
        print("Player 1 Played: "+p1)
        print("Player 2 Played: "+p2)
        print("\n")
        run_prisoners_dilemma(p1,p2, output_df, summary_df)
        display(output_df)
        display(summary_df)
    else:
        display(Markdown("<center><h2>Click the button above to play!</h2></center>"))
        display(Markdown("<center><h2>To play another round with the same options for " + \
                         "both Player 1 and Player 2, press the button twice!</h2></center>"))
        
    
output_df = pd.DataFrame(columns=["Player 1 Payoff", "Player 2 Payoff"])
summary_df = pd.DataFrame(columns=["Player 1", "Player 2"], index=["Sum", "Mean"])

p1 = widgets.Dropdown(options=["Cooperate","Defect"], value="Cooperate", description='Player 1', 
                        disabled=False)
p2 = widgets.Dropdown(options=["Cooperate", "Defect", "Copy", "Random"], value="Cooperate", description='Player 2', 
                        disabled=False)
play_flag = widgets.ToggleButton(value=False, description='Click to Start/Stop Play', 
                               disabled=False, button_style='', 
                               tooltip='Click to start/stop play',
                               layout=Layout(width='30%', height='30px'))