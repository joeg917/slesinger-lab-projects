import os
import pyabf
import matplotlib.pyplot as plt
import numpy as np
import itertools
from perfusionInfo import valvePlotter as vp
from drugDictionaries import drug_dictionaries
#functions
def get_abfs(folder_path):
    abfs = []
    files = os.listdir(folder_path)
    for filename in files:
        full_path = os.path.join(folder_path, filename)
        abf = pyabf.ABF(full_path)
        print(f"Loaded: {abf.abfID}")
        abfs.append(abf)
    return abfs
def sweep_numbers(abf):
    sweep_numbers = []
    for r in range(abf.sweepCount):
        sweep_numbers.append(r)
    return sweep_numbers    
def current_calculator(t1, t2, abf):
    #t1, t2 should be 0.0097, 0.01346 respectively for -100 mv, 0.001, 0.003 for strongest Kir4.1 signal
    current_values = []
    idx1 = int(t1 * abf.sampleRate)
    idx2 = int(t2 * abf.sampleRate)
    for r in range(abf.sweepCount):
        abf.setSweep(r)
        dataChunk = abf.sweepY[idx1:idx2]
        current_values.append(np.mean(dataChunk))
    return current_values
def plotter(abf, sweeps, currents):
    fig, ax = plt.subplots(figsize = (8,5))
    ax.plot(sweeps, currents, 'o-', color='black', markersize = 2, linewidth = 1) 
    ax.axhline(0, color = 'black', ls = '--', alpha = 0.3)
    ax.set_xlabel("Sweep Number")
    ax.set_ylabel("Current(pA)")
    ax.set_title(abf.abfID)
    return fig, ax
def valve_events(abf):
    valveDictionary = vp(abf)
    all_events = []
    for valve, sweeps in valveDictionary.items():
        if not sweeps: continue
        for _, g in itertools.groupby(enumerate(sweeps), lambda x: x[0] - x[1]):
            group = [x[1] for x in g]
            start_sweep = group[0]
            end_sweep = group[-1]
            all_events.append((start_sweep, end_sweep, valve))
    all_events.sort(key=lambda x: x[0])
    return all_events
def plot_valve_states(ax, events, colors):
    for start, end, valve in events:
        ax.axvline(x=start, color=colors[valve % len(colors)], linestyle='-', linewidth = 1.5)
def build_log_text(abf_id, events, drug_map):
    log_entries = [abf_id, "Drug Application Log"]
    for start, end, v_idx in events:
        drug_name = drug_map.get(v_idx, f"Valve {v_idx}")
        log_entries.append(f"{drug_name}: {start} to {end}")          
    return "\n".join(log_entries)
def add_log_text(fig, log_text):
    fig.text(0.78, 0.5, log_text, fontsize = 8, family='monospace', va='center', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
def color_bank():
    colors = ["#919e9c", "#0ee3ff", "#12db12f9", "#d8ee11e6", "#e47c1a", "#e22f0cea", "#92943fd6", "#eb17a4"]
    return colors
def save_plot(fig, save_folder, abf_id):
    save_name = f"{abf_id}_plot.png"
    full_save_path = os.path.join(save_folder, save_name)
    fig.savefig(full_save_path, bbox_inches='tight')
    return full_save_path
#execution block
def main():
    abfs = get_abfs(#INPUT FOLDER PATH HERE#)
    drug_map = drug_dictionaries()
    for file in abfs:
        sweeps = sweep_numbers(file)
        currents = current_calculator(0.0097, 0.01346, file)
        fig, ax = plotter(file, sweeps, currents)
        tagged_events = valve_events(file)
        colors = color_bank()
        plot_valve_states(ax, tagged_events, colors)
        log_text = build_log_text(file.abfID, tagged_events, drug_map)
        add_log_text(fig, log_text)
        plt.tight_layout(rect=[0, 0, 0.75, 1])
        save_plot(fig, #OUTPUT FOLDER PATH HERE#, file.abfID)
        print(f"Processed {file.abfID}")
if __name__ == "__main__":
    main()
        
    

