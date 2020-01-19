from matplotlib import pyplot as plt
import pandas

def weighted_by_color(stay_len, num_dogs, total_dogs, scale = 1):
    return scale*stay_len*num_dogs/total_dogs

# determine scale factor

def get_scale_factor(stay_df, num_df, colors, total_dogs):

    max_len_stay = stay_df["avg_stay_len"].max()

    max_len_stay_weighted = []
    for color in colors:
        max_len_stay_weighted.append(
            weighted_by_color(
                stay_df.loc[color]["avg_stay_len"], 
                num_df.loc[color]["avg_stay_len"], 
                total_dogs
            )
        )
    
    return max_len_stay/max(max_len_stay_weighted)


def plot_bars(df, ax, color_order, color_dict, weighted=False,*, num_df=[], total_dogs=[], scale_factor=1):   
    """Plots bars on ax depending on weighted or unweighted scale"""
    if weighted:
        
        for color in color_order:
        
            if color == "Tricolor": 
                plt.rcParams["hatch.linewidth"] = 5
                plt.rcParams['hatch.color'] = "#CD853F"
                ax.bar(color,
                       weighted_by_color(df.loc[color]["avg_stay_len"], num_df.loc[color]["avg_stay_len"], total_dogs, scale=scale_factor),
                       color = color_dict[color], 
                       hatch="//", 
                       linewidth=2, 
                       ecolor=color_dict["Black"]
                      )
        
            elif color == "White":
                ax.bar(color, 
                       weighted_by_color(df.loc[color]["avg_stay_len"], num_df.loc[color]["avg_stay_len"], total_dogs, scale=scale_factor),
                       color = color_dict[color], 
                       edgecolor=color_dict["Black"]
                      )
                
            else:
                try:
                    ax.bar(color,
                           weighted_by_color(df.loc[color]["avg_stay_len"], num_df.loc[color]["avg_stay_len"], total_dogs, scale=scale_factor),
                           color = color_dict[color], 
                           edgecolor=color_dict["Black"]
                          )
                except KeyError:
                    ax.bar(color,
                           0,
                           color = color_dict[color], 
                           edgecolor=color_dict["Black"]
                          )
    
    else:
        for color in color_order:
        
            if color == "Tricolor": 
                plt.rcParams["hatch.linewidth"] = 5
                plt.rcParams['hatch.color'] = "#CD853F"
                ax.bar(color, 
                       df.loc[color]["avg_stay_len"],
                       color = color_dict[color], 
                       hatch="//", 
                       linewidth=2, 
                       ecolor=color_dict["Black"]
                      )
        
            elif color == "White":
                ax.bar(color, 
                       df.loc[color]["avg_stay_len"],
                       color = color_dict[color], 
                       edgecolor=color_dict["Black"]
                      )
                
            else:
                try:
                    ax.bar(color, 
                           df.loc[color]["avg_stay_len"],
                           color = color_dict[color], 
                           edgecolor=color_dict["Black"]
                          )
                except KeyError:
                    ax.bar(color, 
                           0,
                           color = color_dict[color], 
                           edgecolor=color_dict["Black"]
                          )